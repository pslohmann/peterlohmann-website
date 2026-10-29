/* =============================================================================
   FREE COURSES: video player + "Watch this part" links + analytics events.
   Loaded on course pages and the /courses/ hub (built by build-courses.py).
   Without JavaScript every link still works: the video and each "Watch this part"
   link open on YouTube at the right moment.
   ========================================================================== */
(function () {
  "use strict";
  var root = document.querySelector("[data-course]");
  if (!root) return;
  var slug = root.getAttribute("data-course");

  /* Google Analytics events (gtag only reports on the live site; elsewhere this is a no-op) */
  function track(name, params) {
    params = params || {};
    params.course_slug = slug;
    try { if (typeof window.gtag === "function") window.gtag("event", name, params); } catch (e) {}
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("[data-track]");
    if (a) track(a.getAttribute("data-track"));
  });

  /* ---- the player: thumbnail until clicked, then YouTube's player ---- */
  var box = document.getElementById("course-video");
  if (!box) return;
  var facade = box.querySelector("a.course-player");
  var id = facade && facade.getAttribute("data-id");
  var frame = null;
  var smooth = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function load(start) {
    if (frame) return;
    frame = document.createElement("iframe");
    frame.src = "https://www.youtube.com/embed/" + id + "?autoplay=1&rel=0&playsinline=1&enablejsapi=1" +
      (start ? "&start=" + start : "");
    frame.title = facade.getAttribute("aria-label") || "Course video";
    frame.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
    frame.referrerPolicy = "strict-origin-when-cross-origin";
    frame.setAttribute("allowfullscreen", "");
    var holder = document.createElement("div");
    holder.className = "course-player";
    holder.appendChild(frame);
    facade.parentNode.replaceChild(holder, facade);
  }

  /* YouTube's player takes commands by message once it's running (enablejsapi=1 above) */
  function command(func, args) {
    if (frame && frame.contentWindow) {
      frame.contentWindow.postMessage(JSON.stringify({ event: "command", func: func, args: args || [] }), "*");
    }
  }

  function seek(t) {
    if (!frame) { load(t); return; }
    command("seekTo", [t, true]);
    command("playVideo");
  }

  if (facade && id) {
    facade.addEventListener("click", function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey) return;   // let "open in new tab" work
      e.preventDefault();
      load(0);
    });
  }

  /* ---- "Watch this part (12:34)": scroll up to the video and play from that moment ---- */
  document.querySelectorAll("a.course-jump").forEach(function (a) {
    a.addEventListener("click", function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey || !id) return;
      e.preventDefault();
      var t = parseInt(a.getAttribute("data-t"), 10) || 0;
      var label = (a.textContent.match(/\(([\d:]+)\)/) || [])[1] || String(t);
      track("course_chapter_jump", { timestamp: label, seconds: t });
      box.scrollIntoView({ behavior: smooth ? "smooth" : "auto", block: "start" });
      seek(t);
    });
  });

  /* ---- sidebar module list: highlight the module you're reading ---- */
  var side = document.querySelector(".course-toc-side");
  var heads = Array.prototype.slice.call(document.querySelectorAll("h2.course-module"));
  if (side && heads.length) {
    var links = {};
    side.querySelectorAll("a").forEach(function (a) { links[a.getAttribute("href").slice(1)] = a; });
    var current = null, queued = false;
    function update() {
      queued = false;
      var pick = null;
      heads.forEach(function (h) { if (h.getBoundingClientRect().top < window.innerHeight * 0.35) pick = h; });
      if (pick === current) return;
      if (current && links[current.id]) links[current.id].classList.remove("current");
      if (pick && links[pick.id]) links[pick.id].classList.add("current");
      current = pick;
    }
    window.addEventListener("scroll", function () {
      if (!queued) { queued = true; setTimeout(update, 60); }
    }, { passive: true });
    update();
  }
})();
