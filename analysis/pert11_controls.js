// analysis/pert11_controls.js
(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var n = slides.length, i = 0;
  var cur = document.getElementById('cur');
  var progress = document.getElementById('progress');
  var overview = document.getElementById('overview');

  function show(idx) {
    i = Math.max(0, Math.min(n - 1, idx));
    slides.forEach(function (s, k) { s.classList.toggle('active', k === i); });
    cur.textContent = (i + 1);
    progress.style.width = ((i + 1) / n * 100) + '%';
    var thumbs = overview.querySelectorAll('.thumb');
    thumbs.forEach(function (t, k) { t.classList.toggle('current', k === i); });
  }
  function next() { show(i + 1); }
  function prev() { show(i - 1); }

  // Thumbnail overview (clone each slide's svg once).
  slides.forEach(function (s, k) {
    var t = document.createElement('div');
    t.className = 'thumb';
    var svg = s.querySelector('svg');
    if (svg) t.appendChild(svg.cloneNode(true));
    t.addEventListener('click', function () { closeOverview(); show(k); });
    overview.appendChild(t);
  });
  function toggleOverview() { overview.classList.toggle('open'); }
  function closeOverview() { overview.classList.remove('open'); }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { if (overview.classList.contains('open')) closeOverview(); return; }
    if (e.key === 'o' || e.key === 'O') { toggleOverview(); return; }
    if (overview.classList.contains('open')) return;
    switch (e.key) {
      case 'ArrowRight': case 'PageDown': case ' ': next(); e.preventDefault(); break;
      case 'ArrowLeft': case 'PageUp': prev(); e.preventDefault(); break;
      case 'Home': show(0); break;
      case 'End': show(n - 1); break;
      case 'f': case 'F':
        if (!document.fullscreenElement) document.documentElement.requestFullscreen();
        else document.exitFullscreen();
        break;
    }
  });

  // Click zones (left half = prev, right half = next), ignored over overview.
  document.getElementById('stage').addEventListener('click', function (e) {
    if (overview.classList.contains('open')) return;
    if (e.clientX < window.innerWidth / 2) prev(); else next();
  });

  show(0);
})();
