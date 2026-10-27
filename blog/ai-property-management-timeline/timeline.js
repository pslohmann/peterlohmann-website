/* =============================================================================
   AI IN PROPERTY MANAGEMENT: A COMPREHENSIVE TIMELINE  (/blog/ai-property-management-timeline/)
   A vertical "story" timeline. Everything is drawn from two files:
     data/events.json     one object per event (see CLAUDE.md for the fields)
     data/companies.json  slug -> company name + logo file
   Adding an event = adding a row to events.json. No changes needed here.
   Desktop: one line down the center, AI model releases branch left, the property
   management industry branches right, years are chapter markers on the line.
   Phones: the line moves to the left and every card sits on its right.
   ========================================================================== */
(function () {
  'use strict';

  var BASE = '/blog/ai-property-management-timeline/';
  var SOON = 'coming-soon';

  // Lanes (colors live in timeline.css as --lane-<key>). "up" lanes sit on the left (AI models).
  var LANES = [
    { key: 'frontier', label: 'Frontier AI models', short: 'Frontier AI', up: true },
    { key: 'pm_software', label: 'Property management software', short: 'PM software' },
    { key: 'leasing', label: 'Leasing, showings and CRM', short: 'Leasing' },
    { key: 'maintenance', label: 'Maintenance and inspections', short: 'Maintenance' },
    { key: 'risk', label: 'Screening, fraud and insurance', short: 'Screening and risk' },
    { key: 'data_pricing', label: 'Data and pricing', short: 'Data and pricing' },
    { key: 'plm', label: 'Peter Lohmann Media', short: 'Peter Lohmann Media' }
  ];
  // Event types: the tag people read, and which of the three marker shapes it gets.
  var TYPES = [
    { key: 'frontier_model', tag: 'Frontier model', shape: 'star' },
    { key: 'api_access', tag: 'API', shape: 'diamond' },
    { key: 'mcp_connector', tag: 'MCP or connector', shape: 'diamond' },
    { key: 'platform_launch', tag: 'AI platform', shape: 'dot' },
    { key: 'product_release', tag: 'AI feature', shape: 'dot' },
    { key: 'ai_agent', tag: 'AI agent', shape: 'dot' },
    { key: 'acquisition', tag: 'Acquisition', shape: 'dot' },
    { key: 'funding', tag: 'Funding', shape: 'dot' },
    { key: 'access_cutoff', tag: 'Access cut-off', shape: 'dot' },
    { key: 'report', tag: 'Report', shape: 'dot' }
  ];
  var LANE = {}, TYPE = {};
  LANES.forEach(function (l) { LANE[l.key] = l; });
  TYPES.forEach(function (t) { TYPE[t.key] = t; });
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  // ---------- small helpers ----------
  function $(sel, root) { return (root || document).querySelector(sel); }
  function $all(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function reducedMotion() { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; }
  function plural(n, word) { return n + ' ' + word + (n === 1 ? '' : 's'); }

  var ICONS = {
    down: '<path d="m6 9 6 6 6-6"/>',
    back: '<path d="M19 12H5M12 19l-7-7 7-7"/>',
    ext: '<path d="M15 3h6v6M10 14 21 3M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
    link: '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>'
  };
  function icon(name, cls) {
    return '<svg class="tl-ico' + (cls ? ' ' + cls : '') + '" viewBox="0 0 24 24" aria-hidden="true" focusable="false">' + ICONS[name] + '</svg>';
  }

  // Marker shapes, drawn on a 14x14 grid at roughly equal visual weight.
  var STAR = (function () {
    var pts = [];
    for (var i = 0; i < 10; i++) {
      var r = i % 2 ? 3.3 : 7.4, a = (-90 + i * 36) * Math.PI / 180;
      pts.push((7 + r * Math.cos(a)).toFixed(2) + ' ' + (7.6 + r * Math.sin(a)).toFixed(2));
    }
    return 'M' + pts.join('L') + 'Z';
  })();
  var SHAPES = {
    star: '<path class="f" d="' + STAR + '"/>',
    diamond: '<path class="f" d="M7 .7 13.3 7 7 13.3.7 7Z"/>',
    dot: '<circle class="f" cx="7" cy="7" r="5.6"/>'
  };
  function markerSvg(ev) {
    var shape = (TYPE[ev.type] || {}).shape || 'dot';
    var cls = 'tl-m lane-' + ev.lane + (ev.soon ? ' announced' : '') + (ev.confidence !== 'high' ? ' conf-' + ev.confidence : '');
    return '<svg class="' + cls + '" style="--c:var(--lane-' + ev.lane + ')" viewBox="0 0 14 14" aria-hidden="true" focusable="false">' + SHAPES[shape] + '</svg>';
  }
  function keyMarker(shape, announced) {
    return '<svg class="tl-m' + (announced ? ' announced' : '') + '" style="--c:var(--navy)" viewBox="0 0 14 14" aria-hidden="true" focusable="false">' + SHAPES[shape] + '</svg>';
  }

  // Logo tiles. A missing or broken file turns into a monogram (never a broken image).
  function monogram(slug) {
    var c = data.companies[slug];
    return '<span class="mono">' + esc(((c && c.name) || slug || '?').charAt(0).toUpperCase()) + '</span>';
  }
  function logos(ev) {
    return '<span class="tl-logos" aria-hidden="true">' + ev.companies.slice(0, 2).map(function (slug) {
      var c = data.companies[slug];
      return '<span class="tl-logo">' + (c && c.logo
        ? '<img src="' + esc(BASE + c.logo) + '" alt="" data-slug="' + esc(slug) + '" loading="lazy" decoding="async" />'
        : monogram(slug)) + '</span>';
    }).join('') + '</span>';
  }
  document.addEventListener('error', function (e) {
    var img = e.target;
    if (img && img.tagName === 'IMG' && img.closest && img.closest('.tl-logo')) img.parentNode.innerHTML = monogram(img.getAttribute('data-slug'));
  }, true);

  // ---------- data ----------
  var data = { events: [], byId: {}, companies: {}, redirects: {}, chapters: [] };
  function sortKey(d) {
    d = String(d);
    if (/^\d{4}$/.test(d)) return d + '-12-31';
    if (/^\d{4}-\d{2}$/.test(d)) return d + '-15';
    return d;
  }
  function prepare(events, companies, redirects) {
    companies.forEach(function (c) { data.companies[c.slug] = c; });
    data.redirects = redirects || {};
    events.forEach(function (ev, i) {
      ev._i = i;
      // "Coming soon" items with no date at all (expected starts "No date") sort after the dated ones
      ev.key = (ev.status === 'announced' && /^no date/i.test(ev.expected || '')) ? '9999-12-31' : sortKey(ev.date);
      ev.year = ev.key.slice(0, 4);
      ev.month = +ev.key.slice(5, 7);
      ev.soon = ev.status === 'announced';
      ev.up = !!(LANE[ev.lane] && LANE[ev.lane].up);
      ev.chapter = ev.soon ? SOON : ev.year;
      ev.companies = (ev.companies && ev.companies.length) ? ev.companies : [];
      data.byId[ev.id] = ev;
    });
    events.sort(function (a, b) { return a.key < b.key ? -1 : a.key > b.key ? 1 : a._i - b._i; });
    data.events = events;
    var years = [];
    events.forEach(function (e) { if (!e.soon && years.indexOf(e.year) < 0) years.push(e.year); });
    data.chapters = years.concat([SOON]);
  }

  // ---------- filters: nothing picked = show everything; picking narrows ----------
  // Event-type buttons are the same four groups as the marker key. The dropdown picks one exact type
  // instead; choosing one clears the other so the two never fight.
  var GROUPS = [
    { key: 'frontier', label: 'Frontier model', shape: 'star', test: function (ev) { return ev.type === 'frontier_model'; } },
    { key: 'apimcp', label: 'API or MCP', shape: 'diamond', test: function (ev) { return ev.type === 'api_access' || ev.type === 'mcp_connector'; } },
    { key: 'other', label: 'Everything else', shape: 'dot', test: function (ev) { return (TYPE[ev.type] || {}).shape === 'dot'; } },
    { key: 'announced', label: 'Announced', shape: 'dot', announced: true, test: function (ev) { return ev.soon; } }
  ];
  var filters = { lanes: {}, groups: {}, type: '' };
  function lanesPicked() { return LANES.some(function (l) { return filters.lanes[l.key]; }); }
  function groupsPicked() { return GROUPS.some(function (g) { return filters.groups[g.key]; }); }
  function typeOk(ev) {
    if (filters.type) return filters.type === ev.type;
    if (!groupsPicked()) return true;
    return GROUPS.some(function (g) { return filters.groups[g.key] && g.test(ev); });
  }
  function visible(ev) { return (!lanesPicked() || !!filters.lanes[ev.lane]) && typeOk(ev); }
  function filtersActive() { return lanesPicked() || groupsPicked() || !!filters.type; }
  function clearFilters() { filters.lanes = {}; filters.groups = {}; filters.type = ''; }
  function eventsIn(ch) { return data.events.filter(function (e) { return e.chapter === ch && visible(e); }); }

  // "Previously:" = the most recent notable event before this year starts.
  function previously(ch) {
    var cutoff = ch === SOON ? '9999' : ch + '-01-01', found = null;
    data.events.forEach(function (e) { if (!e.soon && e.notable && visible(e) && e.key < cutoff) found = e; });
    return found;
  }
  function ariaFor(ev) {
    return ev.company + ', ' + (TYPE[ev.type] || {}).tag + ', ' + ev.display_date + ': ' + ev.title + (ev.soon ? ' (announced, not shipped)' : '');
  }

  var REVIEW = /[?&]review(=|&|$)/.test(location.search);
  var el = {};

  // ---------- filters and key ----------
  function renderControls() {
    $('#tl-controls-body').innerHTML =
      '<h2 class="tl-filter-title">Filter</h2>' +
      '<div class="tl-row" role="group" aria-label="Show only these lanes"><span class="tl-row-label">Show only:</span><span class="tl-chips">' +
      LANES.map(function (l) {
        return '<button type="button" class="tl-chip" data-lane="' + l.key + '" aria-pressed="false" style="--c:var(--lane-' + l.key + ')"><span class="sw" aria-hidden="true"></span>' + esc(l.short) + '</button>';
      }).join('') + '</span></div>' +
      '<div class="tl-row tl-row-2" role="group" aria-label="Filter by event type"><span class="tl-row-label">Filter by event type:</span><span class="tl-chips">' +
      GROUPS.map(function (g) {
        return '<button type="button" class="tl-chip" data-group="' + g.key + '" aria-pressed="false">' + keyMarker(g.shape, g.announced) + esc(g.label) + '</button>';
      }).join('') +
      '<span class="tl-or">or</span>' +
      '<label class="tl-select"><span class="sr-only">One specific event type</span><select id="tl-type">' +
      '<option value="">A specific type</option>' +
      TYPES.map(function (t) { return '<option value="' + t.key + '">' + esc(t.tag) + '</option>'; }).join('') +
      '</select>' + icon('down', 'tl-sel-chev') + '</label>' +
      '<button type="button" class="tl-reset" data-reset hidden>Clear filters</button></span></div>';
  }
  function syncControls() {
    $all('[data-lane]', el.controls).forEach(function (b) { b.setAttribute('aria-pressed', !!filters.lanes[b.dataset.lane]); });
    $all('[data-group]', el.controls).forEach(function (b) { b.setAttribute('aria-pressed', !!filters.groups[b.dataset.group]); });
    $('#tl-type').value = filters.type;
    $('[data-reset]', el.controls).hidden = !filtersActive();
    $('.tl-controls-toggle span', el.controls).textContent = filtersActive() ? 'Filters (on)' : 'Filters and key';
  }

  // ---------- the timeline ----------
  // Lays out one month's cards in date order. A card may share a row with the card before it when
  // they sit on opposite sides of the line; the later one then drops a little so the two dots on
  // the line never overlap and earlier always reads as higher up.
  function monthHtml(list) {
    var next = { up: 1, dn: 1 }, prevRow = 0;
    return list.map(function (ev) {
      var side = ev.up ? 'up' : 'dn', row = Math.max(next[side], prevRow), shared = row === prevRow;
      next[side] = row + 1;
      prevRow = row;
      return cardHtml(ev, row, shared);
    }).join('');
  }

  function cardHtml(ev, row, shifted) {
    var t = TYPE[ev.type] || { tag: ev.type }, lane = LANE[ev.lane] || { label: ev.lane };
    var did = 'tl-d-' + ev.id, open = ev.notable && !ev.soon;
    return '<article class="tl-ev lane-' + ev.lane + (ev.up ? ' up' : '') + (open ? ' notable' : '') + (ev.soon ? ' is-announced' : '') + (shifted ? ' shifted' : '') + '" id="tl-e-' + esc(ev.id) + '" data-id="' + esc(ev.id) + '" style="--c:var(--lane-' + ev.lane + ');--r:' + (row || 'auto') + '" aria-label="' + esc(ariaFor(ev)) + '">' +
      '<div class="tl-ev-top">' + markerSvg(ev) + logos(ev) + '<span class="co">' + esc(ev.company) + '</span><span class="date">' + esc(ev.display_date) + '</span></div>' +
      '<h3>' + esc(ev.title) + '</h3>' +
      '<div class="tl-meta"><span class="tl-tag">' + esc(t.tag) + '</span>' +
      (ev.soon ? '<span class="tl-tag status">Announced, not shipped</span>' : '') +
      (REVIEW ? '<span class="tl-tag conf ' + esc(ev.confidence) + '">Confidence: ' + esc(ev.confidence) + '</span>' : '') +
      '<span class="lane"><i aria-hidden="true"></i>' + esc(lane.label) + '</span>' +
      '<button type="button" class="tl-more" aria-expanded="false" aria-controls="' + esc(did) + '">' + (open ? 'Source' : 'Details') + icon('down') + '</button></div>' +
      (open ? '<p class="sum">' + esc(ev.summary) + '</p>' : '') +
      '<div class="tl-details" id="' + esc(did) + '" hidden>' +
      (open ? '' : '<p class="sum">' + esc(ev.summary) + '</p>') +
      (ev.soon && ev.expected ? '<p class="sum exp">Expected: ' + esc(ev.expected) + '</p>' : '') +
      (ev.source_url ? '<a class="tl-src" href="' + esc(ev.source_url) + '" target="_blank" rel="noopener">Read the announcement' + icon('ext') + '</a>' +
        '<span class="srcl">Source: ' + esc(ev.source_label) + '</span>' : '') +
      '<button type="button" class="tl-copy" data-copy="' + esc(ev.id) + '">' + icon('link') + '<span>Copy link</span></button></div>' +
      '</article>';
  }

  function render() {
    var h = '';
    data.chapters.forEach(function (ch, ci) {
      var list = eventsIn(ch), p = ci > 0 ? previously(ch) : null;
      h += '<section class="tl-chapter' + (ci === 0 ? ' first' : '') + (ch === SOON ? ' soon' : '') + '" id="tl-' + ch + '" data-ch="' + ch + '" aria-labelledby="tl-h-' + ch + '">' +
        '<div class="tl-ch-head"><h2 class="tl-ch-year" id="tl-h-' + ch + '">' + (ch === SOON ? 'Coming soon' : ch) + '</h2>' +
        '<span class="tl-ch-count">' + (ch === SOON ? list.length + ' announced' : plural(list.length, 'event')) + '</span>' +
        (p ? '<button type="button" class="tl-prev" data-goto="' + esc(p.id) + '">' + icon('back') + '<span>Previously: <b>' + esc(p.title) + '</b> (' + esc(p.display_date) + ')</span></button>' : '') +
        '</div>';
      if (ch === SOON) h += '<p class="tl-soon-note">These have been announced but aren\'t generally available yet. I\'ll move them onto the timeline when they ship (and only if there\'s real availability and pricing).</p>';
      if (!list.length) h += '<p class="tl-empty">Nothing here with the current filters.</p>';
      else if (ch === SOON) h += '<div class="tl-month">' + monthHtml(list) + '</div>';
      else {
        var months = [];
        list.forEach(function (e) {
          if (!months.length || months[months.length - 1][0].month !== e.month) months.push([]);
          months[months.length - 1].push(e);
        });
        months.forEach(function (m) {
          h += '<div class="tl-month"><span class="tl-mo">' + MONTHS[m[0].month - 1] + '</span>' + monthHtml(m) + '</div>';
        });
      }
      if (ch === SOON) h += '<p class="tl-missing"><a href="https://www.peterlohmann.com/contact" target="_blank" rel="noopener">Something missing? Let me know.</a></p>';
      h += '</section>';
    });
    el.tl.innerHTML = h;
    el.yearbar.innerHTML = data.chapters.map(function (ch) {
      return '<button type="button" class="tl-yb' + (ch === SOON ? ' soon' : '') + '" data-jump="' + ch + '">' + (ch === SOON ? 'Coming soon' : ch) +
        '<small>' + eventsIn(ch).length + '</small></button>';
    }).join('');
    observe();
  }

  // ---------- the year bar follows the reader ----------
  var io = null, current = null, quietHash = false;
  function setCurrent(ch, fromScroll) {
    if (ch === current) return;
    current = ch;
    $all('.tl-yb', el.yearbar).forEach(function (b) { b.setAttribute('aria-current', b.dataset.jump === ch ? 'true' : 'false'); });
    var cur = $('.tl-yb[aria-current="true"]', el.yearbar), bar = el.yearbar;
    if (cur && bar.scrollWidth > bar.clientWidth) bar.scrollLeft = cur.offsetLeft - 16;
    // keep the address pointing at the year being read (no back-button spam)
    if (fromScroll && !quietHash && !/^#e\//.test(location.hash)) setHash(ch);
  }
  // The year being read = the last chapter whose top has scrolled up past the sticky bar.
  var ticking = false;
  function chapterInView() {
    var bar = el.yearbar.closest('nav'), line = (bar ? bar.getBoundingClientRect().bottom : 120) + 40, cur = data.chapters[0];
    $all('.tl-chapter', el.tl).forEach(function (s) { if (s.getBoundingClientRect().top <= line) cur = s.dataset.ch; });
    return cur;
  }
  function onScroll() {
    if (ticking) return;
    ticking = true;
    setTimeout(function () { ticking = false; setCurrent(chapterInView(), true); }, 60);
  }
  function observe() {
    current = null;
    setCurrent(chapterInView());
    if (!io) { window.addEventListener('scroll', onScroll, { passive: true }); io = true; }
  }
  function jump(ch, instant) {
    var s = $('[data-ch="' + ch + '"]', el.tl);
    if (!s) return;
    s.scrollIntoView({ block: 'start', behavior: instant || reducedMotion() ? 'instant' : 'smooth' });
    setCurrent(ch);
    setHash(ch);
  }

  // Opens one event: scrolls it into view, expands it and gives it one soft highlight.
  function goto(ev, opts) {
    opts = opts || {};
    if (!visible(ev)) { clearFilters(); syncControls(); render(); }
    var node = document.getElementById('tl-e-' + ev.id);
    if (!node) return;
    node.scrollIntoView({ block: 'center', behavior: opts.instant || reducedMotion() ? 'instant' : 'smooth' });
    toggleDetails($('.tl-more', node), true);
    node.classList.remove('flash'); void node.offsetWidth; node.classList.add('flash');
    setHash('e/' + ev.id);
  }
  function toggleDetails(btn, open) {
    if (!btn) return;
    var d = document.getElementById(btn.getAttribute('aria-controls'));
    btn.setAttribute('aria-expanded', open);
    if (d) d.hidden = !open;
  }

  // ---------- URL ----------
  function setHash(key) {
    var url = location.pathname + location.search + (key ? '#' + key : '');
    if (url !== location.pathname + location.search + location.hash) history.replaceState(null, '', url);
  }
  function shareUrl(id) { return location.origin + BASE + 'e/' + encodeURIComponent(id) + '/'; }
  function resolveId(id) {
    var seen = 0;
    while (id && !data.byId[id] && data.redirects[id] && seen++ < 5) id = data.redirects[id];
    return data.byId[id] || null;
  }
  // Accepts /blog/ai-property-management-timeline/e/<id>/ and #e/<id> (open that event), #2025 or #coming-soon (jump to it).
  function route() {
    var id = null;
    var m = location.pathname.match(/\/ai-property-management-timeline\/e\/([^/]+)\/?/);
    if (m) {
      id = decodeURIComponent(m[1]);
      history.replaceState(null, '', BASE + location.search + '#e/' + encodeURIComponent(id));
    }
    var h = decodeURIComponent(location.hash.replace(/^#/, ''));
    if (!id && h.indexOf('e/') === 0) id = h.slice(2);
    quietHash = true;
    if (id) {
      var ev = resolveId(id);
      if (ev) {
        goto(ev, { instant: true });
        // fonts and logos can shift the page as they load: settle on the card once they have
        var settle = function () { var n = document.getElementById('tl-e-' + ev.id); if (n) n.scrollIntoView({ block: 'center', behavior: 'instant' }); };
        if (document.fonts && document.fonts.ready) document.fonts.ready.then(settle);
        setTimeout(settle, 400);
      }
      else setHash(null);   // unknown id: quietly show the timeline from the top
    } else if (data.chapters.indexOf(h) >= 0) {
      jump(h, true);
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { jump(h, true); });
    }
    setTimeout(function () { quietHash = false; }, 800);
  }

  function copyLink(btn) {
    var url = shareUrl(btn.getAttribute('data-copy'));
    var swap = function () {
      var s = $('span', btn);
      s.textContent = 'Link copied';
      setTimeout(function () { if (document.contains(s)) s.textContent = 'Copy link'; }, 2000);
    };
    var fallback = function () {
      var f = $('.tl-copy-field', btn.parentNode);
      if (!f) { f = document.createElement('input'); f.className = 'tl-copy-field'; f.readOnly = true; f.setAttribute('aria-label', 'Link to this event'); btn.parentNode.appendChild(f); }
      f.value = url; f.focus(); f.select();
    };
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(url).then(swap, fallback);
      else fallback();
    } catch (e) { fallback(); }
  }

  // ---------- review mode (?review) ----------
  function renderReview() {
    if (!REVIEW) return;
    document.documentElement.classList.add('tl-review-on');
    var rank = { low: 0, med: 1 };
    var list = data.events.filter(function (ev) { return ev.confidence === 'low' || ev.confidence === 'med'; })
      .sort(function (a, b) { return rank[a.confidence] - rank[b.confidence] || (a.key < b.key ? -1 : 1); });
    var d = document.createElement('details');
    d.className = 'tl-review';
    d.innerHTML = '<summary>Review list (' + list.length + ')</summary><ol>' + list.map(function (ev) {
      return '<li><button type="button" data-review="' + esc(ev.id) + '">' + esc(ev.title) + '</button><span class="c">' + esc(ev.confidence) + '</span></li>';
    }).join('') + '</ol>';
    d.addEventListener('click', function (e) {
      var b = e.target.closest('[data-review]');
      if (b) goto(data.byId[b.getAttribute('data-review')]);
    });
    document.body.appendChild(d);
  }

  // ---------- events ----------
  function bind() {
    document.addEventListener('click', function (e) {
      var t = e.target, b;
      if ((b = t.closest('.tl-controls-toggle'))) {
        var open = !el.controls.classList.contains('open');
        el.controls.classList.toggle('open', open);
        b.setAttribute('aria-expanded', open);
        return;
      }
      if ((b = t.closest('[data-lane]'))) { filters.lanes[b.dataset.lane] = !filters.lanes[b.dataset.lane]; syncControls(); render(); return; }
      if ((b = t.closest('[data-group]'))) { filters.type = ''; filters.groups[b.dataset.group] = !filters.groups[b.dataset.group]; syncControls(); render(); return; }
      if ((b = t.closest('[data-reset]'))) { clearFilters(); syncControls(); render(); $('[data-lane]', el.controls).focus(); return; }
      if ((b = t.closest('[data-jump]'))) { jump(b.dataset.jump); return; }
      if ((b = t.closest('[data-goto]'))) { var ev = data.byId[b.dataset.goto]; if (ev) goto(ev); return; }
      if ((b = t.closest('.tl-more'))) {
        var opening = b.getAttribute('aria-expanded') !== 'true';
        toggleDetails(b, opening);
        var card = b.closest('.tl-ev');
        if (opening && card) setHash('e/' + card.dataset.id);
        else if (current) setHash(current);
        return;
      }
      if ((b = t.closest('[data-copy]'))) { copyLink(b); return; }
      // clicking anywhere else on a card opens or closes its details too
      if ((b = t.closest('.tl-ev')) && !t.closest('a, button, input')) {
        var more = $('.tl-more', b);
        if (more) more.click();
      }
    });
    document.addEventListener('change', function (e) {
      if (e.target.id !== 'tl-type') return;
      filters.type = e.target.value;
      if (filters.type) filters.groups = {};
      syncControls();
      render();
    });
    window.addEventListener('hashchange', route);
  }

  // ---------- start ----------
  function fetchJson(path, fallback) {
    return fetch(BASE + path, { credentials: 'same-origin' }).then(function (r) {
      if (!r.ok) throw new Error(path + ' ' + r.status);
      return r.json();
    }).catch(function (err) { if (fallback !== undefined) return fallback; throw err; });
  }
  function start() {
    el.tl = $('#tl');
    el.yearbar = $('#tl-yearbar');
    el.controls = $('#tl-controls');
    Promise.all([fetchJson('data/events.json'), fetchJson('data/companies.json'), fetchJson('data/redirects.json', {})])
      .then(function (r) {
        prepare(r[0], r[1], r[2]);
        renderControls();
        syncControls();
        render();
        bind();
        renderReview();
        route();
      })
      .catch(function () {
        el.tl.innerHTML = '<p class="tl-loading">Sorry, the timeline didn\'t load. Refresh the page to try again.</p>';
      });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
