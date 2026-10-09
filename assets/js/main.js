(function () {
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var els = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('visible'); });
  } else {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) e.target.classList.add('visible'); });
    }, { threshold: 0, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  var nav = document.querySelector('.nav');
  var btn = document.querySelector('.menu');
  function onScroll() { nav.classList.toggle('stuck', window.scrollY > 80); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open);
  });
  document.querySelectorAll('.nav nav a').forEach(function (a) {
    a.addEventListener('click', function () { nav.classList.remove('open'); btn.setAttribute('aria-expanded', false); });
  });

  var sel = document.getElementById('pub-filter');
  if (sel) {
    var items = document.querySelectorAll('.citation');
    var count = document.querySelector('.pub-count');
    var rules = {
      all: function () { return true; },
      first: function (p) { return p > 0 && p <= 1; },
      top2: function (p) { return p > 0 && p <= 2; },
      top3: function (p) { return p > 0 && p <= 3; },
      last: function (p, l) { return l; },
      firstlast: function (p, l) { return (p > 0 && p <= 1) || l; }
    };
    var apply = function () {
      var rule = rules[sel.value], shown = 0;
      items.forEach(function (li) {
        var ok = rule(+li.dataset.pos, li.dataset.last === '1');
        li.hidden = !ok; if (ok) shown++;
      });
      document.querySelectorAll('.year-block').forEach(function (b) {
        b.hidden = !b.querySelector('.citation:not([hidden])');
      });
      count.textContent = sel.value === 'all' ? '' : shown + ' of ' + items.length;
    };
    sel.addEventListener('change', apply);
  }

  var postSel = document.getElementById('post-filter');
  if (postSel) {
    postSel.addEventListener('change', function () {
      document.querySelectorAll('#post-grid .post-row').forEach(function (a) {
        a.hidden = postSel.value !== '' && a.dataset.author !== postSel.value;
      });
    });
  }

  // "first dot last at bristol.ac.uk" -> a working mailto link (built in the browser so crawlers don't see an address)
  document.querySelectorAll('.email-obf').forEach(function (el) {
    var addr = (el.dataset.email || '').trim().replace(/\s+dot\s+/gi, '.').replace(/\s+at\s+/i, '@');
    if (addr.indexOf('@') < 1) return;
    var a = document.createElement('a');
    a.href = 'mailto:' + addr;
    a.textContent = 'Email \u2197';
    el.replaceWith(a);
  });
})();
