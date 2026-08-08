(function () {
    'use strict';

    var filterBtns = document.querySelectorAll('#filters .filter-btn');
    var items = document.querySelectorAll('.gallery-item');
    var lightbox = document.getElementById('lightbox');
    var lightboxImg = document.getElementById('lightbox-img');
    var lightboxCaption = document.getElementById('lightbox-caption');
    var lightboxClose = document.getElementById('lightbox-close');

    function applyFilter(filter) {
        items.forEach(function (item) {
            var show = filter === 'all' || item.getAttribute('data-category') === filter;
            item.classList.toggle('hidden', !show);
        });
        filterBtns.forEach(function (btn) {
            btn.classList.toggle('active', btn.getAttribute('data-filter') === filter);
        });
    }

    filterBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
            applyFilter(btn.getAttribute('data-filter'));
        });
    });

    function openLightbox(item) {
        var img = item.querySelector('img');
        var fig = item.querySelector('.gallery-caption');
        lightboxImg.src = img.getAttribute('src');
        lightboxImg.alt = img.getAttribute('alt') || '';
        lightboxCaption.textContent = fig ? fig.textContent.trim() : '';
        lightbox.classList.add('open');
        lightbox.setAttribute('aria-hidden', 'false');
    }

    function closeLightbox() {
        lightbox.classList.remove('open');
        lightbox.setAttribute('aria-hidden', 'true');
    }

    items.forEach(function (item) {
        item.addEventListener('click', function () {
            openLightbox(item);
        });
    });

    lightboxClose.addEventListener('click', closeLightbox);

    lightbox.addEventListener('click', function (event) {
        if (event.target === lightbox) closeLightbox();
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') closeLightbox();
    });
})();
