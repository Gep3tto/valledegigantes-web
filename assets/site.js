/* AFER Greens — shared behaviour. Everything degrades to a working page without JS. */
(function () {
    'use strict';
    var html = document.documentElement;
    html.classList.add('js');
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
    var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');

    /* --- Custom cursor: only with a fine pointer, only until the tab is hidden --- */
    var cursor = document.getElementById('cursor');
    var ring = document.getElementById('cursor-ring');
    if (cursor && ring && finePointer.matches && !reduce.matches) {
        var mx = 0, my = 0, rx = 0, ry = 0, started = false, rafId = 0;
        function loop() {
            rx += (mx - rx) * 0.14;
            ry += (my - ry) * 0.14;
            ring.style.transform = 'translate(' + rx + 'px,' + ry + 'px) translate(-50%,-50%)';
            rafId = requestAnimationFrame(loop);
        }
        document.addEventListener('mousemove', function (e) {
            mx = e.clientX; my = e.clientY;
            cursor.style.transform = 'translate(' + mx + 'px,' + my + 'px) translate(-50%,-50%)';
            if (!started) { started = true; html.classList.add('js-cursor'); rx = mx; ry = my; loop(); }
        }, { passive: true });
        document.addEventListener('mouseover', function (e) {
            html.classList.toggle('is-hovering', !!e.target.closest('a, button, summary, select'));
        });
        document.addEventListener('visibilitychange', function () {
            if (document.hidden) { cancelAnimationFrame(rafId); started = false; html.classList.remove('js-cursor'); }
        });
    }

    /* --- Header state --- */
    var header = document.getElementById('site-header');
    function onScroll() { header.classList.toggle('scrolled', window.scrollY > 24); }
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });

    /* --- Mobile menu --- */
    var toggle = document.querySelector('.nav-toggle');
    var navMain = document.querySelector('.nav-main');
    if (toggle && navMain) {
        function setMenu(open) {
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
            navMain.classList.toggle('open', open);
            document.body.style.overflow = open ? 'hidden' : '';
        }
        toggle.addEventListener('click', function () { setMenu(toggle.getAttribute('aria-expanded') !== 'true'); });
        navMain.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
        document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
        window.matchMedia('(min-width: 769px)').addEventListener('change', function (e) { if (e.matches) setMenu(false); });
    }

    /* --- Hero parallax (fine pointer, motion allowed): the field falls away, the copy drifts up and fades --- */
    var heroImg = document.getElementById('hero-parallax');
    var heroCopy = document.querySelector('.hero-content');
    if (heroImg && heroCopy && finePointer.matches && !reduce.matches) {
        var ticking = false;
        window.addEventListener('scroll', function () {
            if (ticking) return;
            ticking = true;
            requestAnimationFrame(function () {
                var s = window.scrollY, h = window.innerHeight;
                if (s < h) {
                    heroImg.style.transform = 'scale(1.06) translateY(' + (s * 0.2) + 'px)';
                    heroCopy.style.transform = 'translateY(' + (s * -0.12) + 'px)';
                    heroCopy.style.opacity = Math.max(0, 1 - s / (h * 0.7));
                }
                ticking = false;
            });
        }, { passive: true });
    }

    /* --- Order for staggered lists and for the month-by-month availability strips --- */
    document.querySelectorAll('.stagger').forEach(function (list) {
        Array.prototype.forEach.call(list.children, function (item, i) { item.style.setProperty('--i', i); });
    });
    document.querySelectorAll('.cal-table tbody tr, .season-months').forEach(function (row) {
        if (row.sectionRowIndex !== undefined) row.style.setProperty('--r', row.sectionRowIndex);
        row.querySelectorAll('span').forEach(function (cell, m) { cell.style.setProperty('--m', m); });
    });

    /* --- Headings rise line by line: mask each rendered line, let them rise, then restore the markup --- */
    function fontsReady() {
        var f = document.fonts;
        return !f || (f.check('300 1em "Cormorant Garamond"') && f.check('400 1em "Cormorant Garamond"') && f.check('italic 400 1em "Cormorant Garamond"'));
    }
    function riseLines(el) {
        var original = el.innerHTML, words = [];
        Array.prototype.slice.call(el.childNodes).forEach(function (n) {
            if (n.nodeType === 1) { words.push(n); return; }
            if (n.nodeType !== 3) return;
            var frag = document.createDocumentFragment();
            n.textContent.split(/(\s+)/).forEach(function (part) {
                if (!part) return;
                if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
                var w = document.createElement('span');
                w.textContent = part;
                frag.appendChild(w);
                words.push(w);
            });
            el.replaceChild(frag, n);
        });
        var half = (parseFloat(getComputedStyle(el).lineHeight) || 40) / 2, lines = [], top = -Infinity, wraps = false;
        words.forEach(function (w) {
            var rects = w.getClientRects();
            if (rects.length !== 1) { wraps = true; return; }   // e.g. an <em> broken across lines: leave the heading as it is
            if (rects[0].top > top + half) { lines.push(document.createElement('span')); top = rects[0].top; }
            w.lineIndex = lines.length - 1;
        });
        if (wraps || !lines.length) { el.innerHTML = original; return false; }
        var at = 0;
        Array.prototype.slice.call(el.childNodes).forEach(function (n) {
            if (n.lineIndex !== undefined) at = n.lineIndex;
            lines[at].appendChild(n);
        });
        lines.forEach(function (inner, i) {
            var mask = document.createElement('span');
            mask.className = 'ln';
            inner.style.setProperty('--ln', i);
            mask.appendChild(inner);
            el.appendChild(mask);
        });
        el.classList.add('split', 'visible');
        var delay = parseFloat(getComputedStyle(el).getPropertyValue('--d')) || 0;
        setTimeout(function () { el.innerHTML = original; el.classList.remove('split'); }, (delay + lines.length * 0.09 + 1.2) * 1000);
        return true;
    }

    /* A product page's h1 rises as one block in CSS; upgrade it to the line-by-line rise if its fonts arrive in time */
    var lead = document.querySelector('.ph-content h1');
    var leadRise = lead && !reduce.matches && document.fonts && lead.getAnimations && lead.getAnimations()[0];
    if (leadRise) {
        Promise.all([document.fonts.load('300 1em "Cormorant Garamond"'), document.fonts.load('italic 400 1em "Cormorant Garamond"')]).then(function () {
            var wait = leadRise.effect.getTiming().delay - (leadRise.currentTime || 0);
            if (wait < 50) return;   // the block rise has already begun: let it finish
            leadRise.cancel();
            lead.style.setProperty('--d', wait / 1000 + 's');
            if (!riseLines(lead)) leadRise.play();
        });
    }

    /* --- Scroll reveal --- */
    function reveal(el) {
        if (!(el.classList.contains('section-title') && fontsReady() && riseLines(el))) el.classList.add('visible');
    }
    var reveals = document.querySelectorAll('.reveal');
    if (reveals.length && 'IntersectionObserver' in window && !reduce.matches) {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (en.isIntersecting) { reveal(en.target); io.unobserve(en.target); }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
        reveals.forEach(function (el) { io.observe(el); });
    } else {
        reveals.forEach(function (el) { el.classList.add('visible'); });
    }

    /* --- WhatsApp button appears after the first screen --- */
    var wa = document.querySelector('.wa-float');
    if (wa) {
        function waCheck() { wa.classList.toggle('show', window.scrollY > window.innerHeight * 0.6); }
        waCheck();
        window.addEventListener('scroll', waCheck, { passive: true });
    }

    /* --- Page transitions: the on-screen photo of the product you open becomes that page's hero (see site.css) --- */
    function unnamePhotos() {
        document.querySelectorAll('[data-vt]').forEach(function (el) { el.style.viewTransitionName = ''; });
    }
    window.addEventListener('pageswap', function (e) {
        if (!e.viewTransition) return;
        unnamePhotos();
        var hero = document.querySelector('.ph-visual picture');
        if (hero) hero.style.viewTransitionName = 'none';   // leaving a product page: its hero just fades with the page
        var to = e.activation && e.activation.entry && e.activation.entry.url;
        var slug = to ? new URL(to).pathname.split('/')[1] : '';
        var photo = slug && document.querySelector('[data-vt="' + CSS.escape(slug) + '"]');
        if (!photo) return;
        var r = photo.getBoundingClientRect();
        if (r.bottom > 0 && r.top < window.innerHeight) photo.style.viewTransitionName = 'product-photo';
    });
    window.addEventListener('pageshow', function (e) {
        if (!e.persisted) return;   // back/forward cache: undo the names set when we left
        unnamePhotos();
        var hero = document.querySelector('.ph-visual picture');
        if (hero) hero.style.viewTransitionName = '';
    });

    /* --- Quote form: preselect product from ?producto=, submit via fetch, announce result --- */
    var form = document.getElementById('cotizacion-form');
    if (form) {
        var select = form.querySelector('#producto');
        var wanted = new URLSearchParams(location.search).get('producto');
        if (select && wanted) {
            for (var i = 0; i < select.options.length; i++) {
                if (select.options[i].value === wanted) { select.selectedIndex = i; break; }
            }
        }
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            var btn = form.querySelector('.btn-submit');
            var err = document.getElementById('form-error');
            var ok = document.getElementById('form-success');
            btn.textContent = 'Enviando…';
            btn.disabled = true;
            err.classList.remove('show');
            fetch(form.action, { method: 'POST', headers: { 'Accept': 'application/json' }, body: new FormData(form) })
                .then(function (r) { return r.json(); })
                .then(function (data) {
                    if (data.success === 'true' || data.success === true) {
                        form.hidden = true;
                        ok.hidden = false;
                        var h = ok.querySelector('h3');
                        if (h) { h.setAttribute('tabindex', '-1'); h.focus(); }
                    } else { throw new Error(data.message || 'error'); }
                })
                .catch(function () {
                    btn.textContent = 'Solicitar cotización';
                    btn.disabled = false;
                    err.classList.add('show');
                });
        });
    }
})();
