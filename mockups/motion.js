/* Mockup motion toolkit — vanilla, ~2KB, degrades gracefully */
(function () {
    'use strict';
    var doc = document.documentElement;
    doc.classList.add('js');
    var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
    var finePointer = matchMedia('(hover: hover) and (pointer: fine)').matches;

    // --- Load ceremony: .is-loaded fires the hero timeline ---
    if (document.readyState === 'complete') doc.classList.add('is-loaded');
    else addEventListener('load', function () { doc.classList.add('is-loaded'); });

    // --- Triggered reveals (fallback + default): .io -> .in ---
    var ios = document.querySelectorAll('.io');
    if (ios.length && 'IntersectionObserver' in window && !reduced) {
        var obs = new IntersectionObserver(function (es) {
            es.forEach(function (e) {
                if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
        ios.forEach(function (el) { obs.observe(el); });
    } else {
        ios.forEach(function (el) { el.classList.add('in'); });
    }

    // --- Scroll scrub: [data-scrub] gets --p (0..1) over its own traversal ---
    var scrubs = Array.prototype.slice.call(document.querySelectorAll('[data-scrub]'));
    if (scrubs.length && !reduced) {
        var ticking = false;
        var update = function () {
            ticking = false;
            var vh = innerHeight;
            scrubs.forEach(function (el) {
                var r = el.getBoundingClientRect();
                var total = r.height + vh;
                var p = (vh - r.top) / total;
                p = Math.max(0, Math.min(1, p));
                el.style.setProperty('--p', p.toFixed(4));
            });
        };
        var onScroll = function () {
            if (!ticking) { ticking = true; requestAnimationFrame(update); }
        };
        addEventListener('scroll', onScroll, { passive: true });
        addEventListener('resize', onScroll);
        update();
    }

    // --- Magnetic elements: [data-magnetic] ---
    if (finePointer && !reduced) {
        document.querySelectorAll('[data-magnetic]').forEach(function (el) {
            var tx = 0, ty = 0, cx = 0, cy = 0, raf = null;
            var tick = function () {
                cx += (tx - cx) * 0.18;
                cy += (ty - cy) * 0.18;
                el.style.transform = 'translate(' + cx.toFixed(2) + 'px,' + cy.toFixed(2) + 'px)';
                if (Math.abs(tx - cx) > 0.1 || Math.abs(ty - cy) > 0.1) raf = requestAnimationFrame(tick);
                else raf = null;
            };
            el.addEventListener('mousemove', function (e) {
                var r = el.getBoundingClientRect();
                tx = (e.clientX - r.left - r.width / 2) * 0.35;
                ty = (e.clientY - r.top - r.height / 2) * 0.35;
                if (!raf) raf = requestAnimationFrame(tick);
            });
            el.addEventListener('mouseleave', function () {
                tx = 0; ty = 0;
                if (!raf) raf = requestAnimationFrame(tick);
            });
        });
    }

    // --- Image-follow cursor: container [data-float] + rows [data-float-src] ---
    var floatWrap = document.querySelector('[data-float]');
    if (floatWrap && finePointer && !reduced) {
        var fig = document.createElement('div');
        fig.className = 'float-img';
        var im = document.createElement('img');
        im.alt = '';
        fig.appendChild(im);
        document.body.appendChild(fig);
        var fx = 0, fy = 0, mx2 = 0, my2 = 0, active = false, rafF = null;
        var loop = function () {
            fx += (mx2 - fx) * 0.12;
            fy += (my2 - fy) * 0.12;
            fig.style.transform = 'translate(' + (fx + 24) + 'px,' + (fy - 120) + 'px)';
            rafF = active || Math.abs(mx2 - fx) > 0.5 ? requestAnimationFrame(loop) : null;
        };
        addEventListener('mousemove', function (e) { mx2 = e.clientX; my2 = e.clientY; });
        floatWrap.querySelectorAll('[data-float-src]').forEach(function (row) {
            row.addEventListener('mouseenter', function () {
                im.src = row.getAttribute('data-float-src');
                fig.classList.add('on');
                active = true;
                if (!rafF) rafF = requestAnimationFrame(loop);
            });
            row.addEventListener('mouseleave', function () {
                fig.classList.remove('on');
                active = false;
            });
        });
    }

    // --- Ticker pause button ---
    var ticker = document.querySelector('.ticker');
    var pauseBtn = document.querySelector('.ticker-pause');
    if (ticker && pauseBtn) {
        pauseBtn.addEventListener('click', function () {
            var p = ticker.classList.toggle('paused');
            pauseBtn.setAttribute('aria-pressed', String(p));
        });
    }
})();
