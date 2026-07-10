/* AFER Greens — cinema.js (shared, zero-dependency) */
(function () {
    'use strict';

    document.documentElement.classList.add('js');

    var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // --- Header scroll state ---
    var header = document.querySelector('.site-header');
    if (header) {
        var onScroll = function () {
            header.classList.toggle('scrolled', window.scrollY > 40);
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

    // --- Scroll reveals ---
    var revealEls = document.querySelectorAll('.rv, .clip-rv');
    if (revealEls.length && 'IntersectionObserver' in window && !prefersReduced) {
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('in');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
        revealEls.forEach(function (el) { observer.observe(el); });
    } else {
        revealEls.forEach(function (el) { el.classList.add('in'); });
    }

    // --- Ticker pause (WCAG 2.2.2) ---
    var ticker = document.querySelector('.ticker');
    var pauseBtn = document.querySelector('.ticker-pause');
    if (ticker && pauseBtn) {
        pauseBtn.addEventListener('click', function () {
            var paused = ticker.classList.toggle('paused');
            pauseBtn.setAttribute('aria-pressed', String(paused));
        });
    }

    // --- Quote form: preselect product from ?producto= ---
    var select = document.getElementById('producto');
    if (select) {
        var wanted = new URLSearchParams(window.location.search).get('producto');
        if (wanted) {
            var map = {
                'chiltepin': 'Chiltepín seco',
                'jalapeno': 'Jalapeño fresco',
                'chipotle': 'Chipotle ahumado con mezquite',
                'melon': 'Melón Gran Torino'
            };
            var value = map[wanted.toLowerCase()];
            if (value) select.value = value;
        }
    }
})();
