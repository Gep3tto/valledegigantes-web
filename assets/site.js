/* AFER Greens — site.js (shared, zero-dependency) */
(function () {
    'use strict';

    // JS flag: reveal animations only apply when JS is available
    document.documentElement.classList.add('js');

    var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // --- Sticky header state ---
    var header = document.querySelector('.site-header');
    if (header) {
        var onScroll = function () {
            header.classList.toggle('scrolled', window.scrollY > 24);
        };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    // --- Mobile menu ---
    var toggle = document.querySelector('.menu-toggle');
    var menu = document.getElementById('menu-movil');
    if (toggle && menu) {
        var closeMenu = function () {
            menu.classList.remove('open');
            toggle.setAttribute('aria-expanded', 'false');
            document.body.classList.remove('menu-open');
        };
        toggle.addEventListener('click', function () {
            var open = menu.classList.toggle('open');
            toggle.setAttribute('aria-expanded', String(open));
            document.body.classList.toggle('menu-open', open);
        });
        menu.addEventListener('click', function (e) {
            if (e.target.closest('a')) closeMenu();
        });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && menu.classList.contains('open')) {
                closeMenu();
                toggle.focus();
            }
        });
    }

    // --- Scroll reveal ---
    var revealEls = document.querySelectorAll('.reveal');
    if (revealEls.length && 'IntersectionObserver' in window && !prefersReduced) {
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
        revealEls.forEach(function (el) { observer.observe(el); });
    } else {
        revealEls.forEach(function (el) { el.classList.add('visible'); });
    }

    // --- Ticker pause toggle (WCAG 2.2.2) ---
    var strip = document.querySelector('.strip');
    var pauseBtn = document.querySelector('.strip-pause');
    if (strip && pauseBtn) {
        pauseBtn.addEventListener('click', function () {
            var paused = strip.classList.toggle('paused');
            pauseBtn.setAttribute('aria-pressed', String(paused));
        });
    }

    // --- Quote form: preselect product from ?producto= ---
    var select = document.getElementById('producto');
    if (select) {
        var params = new URLSearchParams(window.location.search);
        var wanted = params.get('producto');
        if (wanted) {
            var map = {
                'chiltepin': 'Chiltepín — El Oro Rojo',
                'jalapeno': 'Jalapeño de Primera',
                'chipotle': 'Chipotle Ahumado Artesanal',
                'melon': 'Melón Gran Torino'
            };
            var value = map[wanted.toLowerCase()];
            if (value) select.value = value;
        }
    }
})();
