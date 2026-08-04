(function() {
    'use strict';

    /* ===== NAVIGATION MOBILE ===== */
    const navToggle = document.querySelector('.nav-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (navToggle && mainNav) {
        navToggle.addEventListener('click', function() {
            mainNav.classList.toggle('open');
            navToggle.setAttribute('aria-expanded', mainNav.classList.contains('open'));
        });

        mainNav.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                mainNav.classList.remove('open');
            });
        });
    }

    /* ===== APPARITION AU SCROLL ===== */
    const sections = document.querySelectorAll('.section');
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.08 });
        sections.forEach(function(section) {
            observer.observe(section);
        });
    } else {
        sections.forEach(function(section) {
            section.classList.add('visible');
        });
    }

    /* ===== FILTRES GALERIE ===== */
    const filterBtns = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');

    filterBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            filterBtns.forEach(function(b) { b.classList.remove('active'); });
            btn.classList.add('active');

            const filter = btn.getAttribute('data-filter');
            galleryItems.forEach(function(item) {
                const category = item.getAttribute('data-category');
                if (filter === 'all' || category === filter) {
                    item.classList.remove('hidden');
                } else {
                    item.classList.add('hidden');
                }
            });
        });
    });

    /* ===== LIGHTBOX ===== */
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.getElementById('lightbox-image');
    const lightboxCaption = document.getElementById('lightbox-caption');
    const lightboxClose = document.querySelector('.lightbox-close');

    function openLightbox(src, caption) {
        if (!lightbox) return;
        lightboxImage.src = src;
        lightboxCaption.textContent = caption || '';
        lightbox.classList.add('active');
        lightbox.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
        if (!lightbox) return;
        lightbox.classList.remove('active');
        lightbox.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    }

    galleryItems.forEach(function(item) {
        item.addEventListener('click', function() {
            const img = item.querySelector('img');
            const caption = item.querySelector('figcaption');
            if (img) {
                openLightbox(img.src, caption ? caption.textContent : '');
            }
        });
    });

    if (lightboxClose) {
        lightboxClose.addEventListener('click', closeLightbox);
    }
    if (lightbox) {
        lightbox.addEventListener('click', function(e) {
            if (e.target === lightbox) closeLightbox();
        });
    }
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeLightbox();
    });

    /* ===== FORMULAIRE D'INSCRIPTION ===== */
    const form = document.getElementById('inscription-form');
    const formSuccess = document.getElementById('form-success');

    function buildMailto(data) {
        const subject = encodeURIComponent('Inscription Boxing Club SPDC - ' + (data.get('nom') || ''));
        const body = [
            'Nom : ' + (data.get('nom') || ''),
            'Email : ' + (data.get('email') || ''),
            'Téléphone : ' + (data.get('telephone') || ''),
            'Tranche d\'âge : ' + (data.get('age') || ''),
            'Niveau : ' + (data.get('niveau') || ''),
            'Objectif : ' + (data.get('objectif') || ''),
            '',
            'Message :',
            (data.get('message') || '')
        ].join('\n');
        return 'mailto:boxingclubspdc@gmail.com?subject=' + subject + '&body=' + encodeURIComponent(body);
    }

    if (form && formSuccess) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            const nom = document.getElementById('nom').value.trim();
            const email = document.getElementById('email').value.trim();
            const age = document.getElementById('age').value;

            if (!nom || !email || !age) {
                alert('Veuillez remplir tous les champs obligatoires (*)');
                return;
            }
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                alert('Veuillez entrer une adresse email valide');
                return;
            }

            const data = new FormData(form);
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            submitBtn.textContent = 'Ouverture de votre messagerie...';
            submitBtn.disabled = true;

            window.location.href = buildMailto(data);

            setTimeout(function() {
                form.style.display = 'none';
                formSuccess.style.display = 'block';
                formSuccess.scrollIntoView({ behavior: 'smooth', block: 'center' });
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;

                setTimeout(function() {
                    form.reset();
                    form.style.display = 'block';
                    formSuccess.style.display = 'none';
                }, 6000);
            }, 1000);
        });
    }

    /* ===== SERVICE WORKER (PWA) ===== */
    if ('serviceWorker' in navigator && location.protocol === 'https:') {
        window.addEventListener('load', function() {
            navigator.serviceWorker.register('service-worker.js').catch(function() {
                /* PWA optionnelle : pas bloquant */
            });
        });
    }
})();
