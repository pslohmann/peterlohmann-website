/* =============================================================================
   PETER LOHMANN - WEBSITE SHARED SCRIPT
   Handles: (1) the mobile menu button, (2) click-to-play podcast videos,
   (3) the sticky newsletter bar on phones, (4) scroll reveal animations.
   No dependencies, no build step. Loaded by every page.
   ========================================================================== */
(function () {
  "use strict";

  /* ---- 1. Mobile menu toggle ---- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector("nav.top .links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* ---- 2. Podcast episode cards: click thumbnail -> load the YouTube player inline ---- */
  document.querySelectorAll(".ep-player").forEach(function (p) {
    function play() {
      var id = p.getAttribute("data-id");
      if (!id || p.dataset.loaded) return;
      p.dataset.loaded = "1";
      var f = document.createElement("iframe");
      f.src = "https://www.youtube.com/embed/" + id + "?autoplay=1";
      f.title = "YouTube video player";
      f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
      f.referrerPolicy = "strict-origin-when-cross-origin";
      f.setAttribute("allowfullscreen", "");
      p.innerHTML = "";
      p.appendChild(f);
    }
    p.addEventListener("click", play);
    p.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); play(); }
    });
  });

  /* ---- 3. Sticky newsletter bar (phones only; CSS hides it on wider screens) ----
     Skipped on hidden utility pages (noindex), on PeterBot (its chat box types at the
     bottom of the screen) and on the M&A Report checkout page (its own buy buttons).
     Appears once the reader scrolls past the first screen, steps aside while the
     subscribe box itself is visible, and stays closed for the visit once dismissed. */
  (function () {
    var path = location.pathname.replace(/index\.html$/, "").replace(/\.html$/, "");
    var skip = ["/peterbot", "/report/"];
    var robots = document.querySelector('meta[name="robots"]');
    if (skip.indexOf(path) !== -1) return;
    if (robots && /noindex/i.test(robots.getAttribute("content") || "")) return;
    try { if (sessionStorage.getItem("plStickyCtaClosed")) return; } catch (e) {}

    var onNewsletter = path === "/newsletter";
    var bar = document.createElement("div");
    bar.className = "sticky-cta";
    bar.setAttribute("role", "region");
    bar.setAttribute("aria-label", "Newsletter signup");
    bar.innerHTML =
      '<div class="sc-text"><strong>Get the newsletter</strong><span>Twice a week. Free.</span></div>' +
      '<a class="btn btn-primary btn-sm" href="' + (onNewsletter ? "#subscribe" : "/newsletter#subscribe") + '">Subscribe free</a>' +
      '<button class="sc-close" type="button" aria-label="Close newsletter bar">&times;</button>';
    document.body.appendChild(bar);
    document.body.classList.add("has-sticky-cta");

    var box = document.getElementById("subscribe");
    function update() {
      var past = window.scrollY > window.innerHeight * 0.6;
      var boxVisible = false;
      if (box) {
        var r = box.getBoundingClientRect();
        boxVisible = r.top < window.innerHeight && r.bottom > 0;
      }
      bar.classList.toggle("show", past && !boxVisible);
    }
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();

    bar.querySelector(".sc-close").addEventListener("click", function () {
      bar.remove();
      document.body.classList.remove("has-sticky-cta");
      try { sessionStorage.setItem("plStickyCtaClosed", "1"); } catch (e) {}
    });
  })();

  /* ---- 4. Scroll reveal ---- */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var targets = document.querySelectorAll(".reveal, .stagger");
  if (reduce || !("IntersectionObserver" in window)) {
    targets.forEach(function (el) { el.classList.add("in"); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        io.unobserve(e.target);
      }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });
  targets.forEach(function (el) { io.observe(el); });
})();
