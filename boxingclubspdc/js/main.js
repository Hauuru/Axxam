// Simplified Main Script with Error Handling
document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    // Check if elements exist before using them
    function safeQuery(selector) {
        try {
            return document.querySelector(selector);
        } catch (e) {
            console.warn('Element not found:', selector);
            return null;
        }
    }

    // Sticky Navigation
    const nav = safeQuery('nav');
    const scrollIndicator = safeQuery('.scroll-indicator');
    const menuToggle = safeQuery('.menu-toggle');
    const navLinks = document.querySelectorAll('nav ul li a');

    let lastScrollTop = 0;

    // Simplified scroll event handler
    function handleScroll() {
        try {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            // Update scroll indicator if it exists
            if (scrollIndicator) {
                const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
                const scrollPercent = (scrollTop / scrollHeight) * 100;
                scrollIndicator.style.transform = `scaleX(${scrollPercent / 100})`;
            }

            // Sticky navigation logic
            if (nav && scrollTop > 100) {
                nav.classList.add('sticky', 'scrolled');
                if (scrollIndicator) scrollIndicator.classList.add('active');
            } else if (nav) {
                nav.classList.remove('sticky', 'scrolled');
                if (scrollIndicator) scrollIndicator.classList.remove('active');
            }

        } catch (e) {
            console.warn('Scroll error:', e);
        }
    }

    // Debounced scroll event
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(handleScroll, 16); // ~60fps
    });

    // Initial scroll setup
    handleScroll();

    // Mobile menu toggle
    if (menuToggle && nav) {
        menuToggle.addEventListener('click', function() {
            nav.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });

        // Close mobile menu when clicking links
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                nav.classList.remove('active');
                menuToggle.classList.remove('active');
            });
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = nav.contains(event.target);
            const isClickOnToggle = menuToggle.contains(event.target);

            if (!isClickInsideNav && !isClickOnToggle && nav.classList.contains('active')) {
                nav.classList.remove('active');
                menuToggle.classList.remove('active');
            }
        });
    }

    // Smooth scroll for navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                const offsetTop = targetSection.offsetTop - 80; // Account for sticky nav
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Simple scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Observe all sections
    document.querySelectorAll('section').forEach(section => {
        section.classList.add('fade-in');
        observer.observe(section);
    });

    // Gallery Filter
    const categoryBtns = document.querySelectorAll('.category-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');

    if (categoryBtns.length > 0 && galleryItems.length > 0) {
        categoryBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                // Remove active class from all buttons
                categoryBtns.forEach(b => b.classList.remove('active'));
                // Add active class to clicked button
                this.classList.add('active');

                const category = this.getAttribute('data-category');

                galleryItems.forEach(item => {
                    if (category === 'all' || item.getAttribute('data-category') === category) {
                        item.style.display = 'block';
                        setTimeout(() => {
                            item.style.opacity = '1';
                            item.style.transform = 'scale(1)';
                        }, 10);
                    } else {
                        item.style.opacity = '0';
                        item.style.transform = 'scale(0.8)';
                        setTimeout(() => {
                            item.style.display = 'none';
                        }, 300);
                    }
                });
            });
        });
    }

    // Simple Lightbox Functionality
    const lightbox = safeQuery('#lightbox');
    const lightboxImage = safeQuery('#lightbox-image');
    const lightboxClose = safeQuery('#lightbox-close');

    if (lightbox && lightboxImage) {
        // Simple lightbox open
        galleryItems.forEach((item, index) => {
            item.addEventListener('click', function() {
                const imageSrc = item.getAttribute('data-image') || item.querySelector('img')?.src;
                const imageTitle = item.getAttribute('data-title') || item.querySelector('img')?.alt;
                
                if (imageSrc) {
                    lightboxImage.src = imageSrc;
                    lightboxImage.alt = imageTitle || 'Image';
                    lightbox.classList.add('active');
                    document.body.style.overflow = 'hidden';
                }
            });
        });

        // Close lightbox
        if (lightboxClose) {
            lightboxClose.addEventListener('click', function() {
                lightbox.classList.remove('active');
                document.body.style.overflow = '';
            });
        }

        // Click outside to close
        lightbox.addEventListener('click', function(e) {
            if (e.target === lightbox) {
                lightbox.classList.remove('active');
                document.body.style.overflow = '';
            }
        });

        // Keyboard navigation
        document.addEventListener('keydown', function(e) {
            if (lightbox.classList.contains('active')) {
                if (e.key === 'Escape') {
                    lightbox.classList.remove('active');
                    document.body.style.overflow = '';
                }
            }
        });
    }

    // Formspree Form Handler
    const form = safeQuery('#inscription-form');
    const formSuccess = safeQuery('#form-success');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Basic validation
            const nom = document.getElementById('nom').value.trim();
            const email = document.getElementById('email').value.trim();
            const age = document.getElementById('age').value;
            
            if (!nom || !email || !age) {
                alert('Veuillez remplir tous les champs obligatoires (*)');
                return;
            }
            
            // Email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                alert('Veuillez entrer une adresse email valide');
                return;
            }
            
            // Show loading state
            const submitButton = form.querySelector('.btn-primary');
            const originalText = submitButton.textContent;
            submitButton.textContent = 'Envoi en cours...';
            submitButton.disabled = true;
            
            // Simulate form submission
            setTimeout(function() {
                // Hide form and show success message
                form.style.display = 'none';
                formSuccess.style.display = 'block';
                
                // Scroll to success message
                formSuccess.scrollIntoView({ behavior: 'smooth', block: 'center' });
                
                // Reset button
                submitButton.textContent = originalText;
                submitButton.disabled = false;
                
                // Reset form after showing success
                setTimeout(function() {
                    form.reset();
                    form.style.display = 'block';
                    formSuccess.style.display = 'none';
                }, 5000);
                
            }, 2000);
        });
    }

    // Check for internet connectivity
    window.addEventListener('online', function() {
        console.log('Application is online');
        document.body.classList.remove('offline');
        document.body.classList.add('online');
    });

    window.addEventListener('offline', function() {
        console.log('Application is offline');
        document.body.classList.remove('online');
        document.body.classList.add('offline');
    });

    // Register service worker for PWA functionality
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
            navigator.serviceWorker.register('/service-worker.js')
                .then(function(registration) {
                    console.log('ServiceWorker registration successful with scope: ', registration.scope);
                })
                .catch(function(error) {
                    console.log('ServiceWorker registration failed: ', error);
                });
        });
    }
});