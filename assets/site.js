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

    /* --- Hero parallax (fine pointer, motion allowed) --- */
    var heroImg = document.getElementById('hero-parallax');
    if (heroImg && finePointer.matches && !reduce.matches) {
        var ticking = false;
        window.addEventListener('scroll', function () {
            if (ticking) return;
            ticking = true;
            requestAnimationFrame(function () {
                var s = window.scrollY;
                if (s < window.innerHeight) heroImg.style.transform = 'scale(1.06) translateY(' + (s * 0.2) + 'px)';
                ticking = false;
            });
        }, { passive: true });
    }

    /* --- Scroll reveal --- */
    var reveals = document.querySelectorAll('.reveal');
    if (reveals.length && 'IntersectionObserver' in window && !reduce.matches) {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (en.isIntersecting) { en.target.classList.add('visible'); io.unobserve(en.target); }
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
