// Performance Optimized Main Script
document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    // Performance: Use requestAnimationFrame for scroll events
    let ticking = false;

    // Sticky Navigation
    // Sticky Navigation
    const nav = document.querySelector('nav');
    const scrollIndicator = document.querySelector('.scroll-indicator');
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelectorAll('nav ul li a');

    let lastScrollTop = 0;
    let isScrolling = false;

    // Scroll event handler
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = (scrollTop / scrollHeight) * 100;

        // Update scroll indicator
        scrollIndicator.style.transform = `scaleX(${scrollPercent / 100})`;

        // Sticky navigation logic
        if (scrollTop > 100) {
            nav.classList.add('sticky', 'scrolled');
            scrollIndicator.classList.add('active');
        } else {
            nav.classList.remove('sticky', 'scrolled');
            scrollIndicator.classList.remove('active');
        }

        // Hide/show navigation on scroll (optional)
        if (!isScrolling) {
            requestAnimationFrame(function() {
                if (scrollTop > lastScrollTop && scrollTop > 200) {
                    // Scrolling down - hide nav
                    nav.style.transform = 'translateY(-100%)';
                } else {
                    // Scrolling up - show nav
                    nav.style.transform = 'translateY(0)';
                }
                lastScrollTop = scrollTop;
                isScrolling = false;
            });
        }
        isScrolling = true;
    });

    // Mobile menu toggle
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

    // Scroll Animations
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');

                // Add stagger animation to cards
                if (entry.target.classList.contains('card')) {
                    const cards = entry.target.querySelectorAll('.card');
                    cards.forEach((card, index) => {
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        }, index * 100);
                    });
                }
            }
        });
    }, observerOptions);

    // Observe all sections and animated elements
    const animatedElements = document.querySelectorAll('section, .fade-in, .fade-in-left, .fade-in-right, .card, .gallery-item, .temoignage-card, .video-card');
    animatedElements.forEach(el => observer.observe(el));

    // Gallery Filter
    const categoryBtns = document.querySelectorAll('.category-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');

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

    // Lightbox Functionality
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.getElementById('lightbox-image');
    const lightboxTitle = document.getElementById('lightbox-title');
    const lightboxDescription = document.getElementById('lightbox-description');
    const lightboxClose = document.getElementById('lightbox-close');
    const lightboxPrev = document.getElementById('lightbox-prev');
    const lightboxNext = document.getElementById('lightbox-next');

    let currentImageIndex = 0;
    let allImages = [];

    // Collect all gallery items
    galleryItems.forEach((item, index) => {
        allImages.push({
            src: item.getAttribute('data-image'),
            title: item.getAttribute('data-title'),
            description: item.getAttribute('data-description'),
            element: item
        });
    });

    // Open lightbox
    function openLightbox(index) {
        currentImageIndex = index;
        const imageData = allImages[index];

        lightboxImage.src = imageData.src;
        lightboxTitle.textContent = imageData.title;
        lightboxDescription.textContent = imageData.description;

        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';

        // Update navigation buttons visibility
        updateNavigationButtons();
    }

    // Close lightbox
    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }

    // Show previous image
    function showPreviousImage() {
        if (currentImageIndex > 0) {
            openLightbox(currentImageIndex - 1);
        }
    }

    // Show next image
    function showNextImage() {
        if (currentImageIndex < allImages.length - 1) {
            openLightbox(currentImageIndex + 1);
        }
    }

    // Update navigation buttons visibility
    function updateNavigationButtons() {
        lightboxPrev.style.display = currentImageIndex === 0 ? 'none' : 'flex';
        lightboxNext.style.display = currentImageIndex === allImages.length - 1 ? 'none' : 'flex';
    }

    // Event listeners for gallery items
    galleryItems.forEach((item, index) => {
        item.addEventListener('click', function() {
            openLightbox(index);
        });
    });

    // Event listeners for lightbox controls
    lightboxClose.addEventListener('click', closeLightbox);
    lightboxPrev.addEventListener('click', showPreviousImage);
    lightboxNext.addEventListener('click', showNextImage);

    // Click outside to close
    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (lightbox.classList.contains('active')) {
            switch(e.key) {
                case 'Escape':
                    closeLightbox();
                    break;
                case 'ArrowLeft':
                    showPreviousImage();
                    break;
                case 'ArrowRight':
                    showNextImage();
                    break;
            }
        }
    });

    // Touch support for mobile
    let touchStartX = 0;
    let touchEndX = 0;

    lightbox.addEventListener('touchstart', function(e) {
        touchStartX = e.changedTouches[0].screenX;
    });

    lightbox.addEventListener('touchend', function(e) {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });

    function handleSwipe() {
        const swipeThreshold = 50;
        const diff = touchStartX - touchEndX;

        if (Math.abs(diff) > swipeThreshold) {
            if (diff > 0) {
                // Swipe left - next image
                showNextImage();
            } else {
                // Swipe right - previous image
                showPreviousImage();
            }
        }
    }

    // Formspree Form Handler
    const form = document.getElementById('inscription-form');
    const formSuccess = document.getElementById('form-success');
    
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
            
            // Simulate form submission (replace with actual Formspree URL)
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
    
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add scroll animations
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
    
    // Performance: Debounce scroll events
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Performance: Throttle resize events
    function throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }

    // Lazy loading for images with priority loading
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;

                    // Load image
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        delete img.dataset.src;
                    }

                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            });
        }, {
            rootMargin: '50px',
            threshold: 0.1
        });

        // Priority loading for above-the-fold images
        const priorityImages = document.querySelectorAll('img.priority');
        priorityImages.forEach(img => {
            if (!img.src && img.dataset.src) {
                img.src = img.dataset.src;
            }
            imageObserver.observe(img);
        });

        // Lazy load other images
        const lazyImages = document.querySelectorAll('img.lazy:not(.priority)');
        lazyImages.forEach(img => {
            imageObserver.observe(img);
        });
    }

    // Performance: Preload critical resources
    function preloadCriticalResources() {
        const criticalResources = [
            '/styles.css',
            '/js/main.js'
        ];

        criticalResources.forEach(url => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.href = url;
            link.as = url.includes('.css') ? 'style' : 'script';
            document.head.appendChild(link);
        });
    }

    // Performance: Remove unused CSS
    function removeUnusedCSS() {
        // This would typically be done during build process
        // Here we add a placeholder for CSS optimization
        console.log('CSS optimization: Remove unused styles in build process');
    }

    // Performance: Optimize font loading
    function optimizeFontLoading() {
        // Use font-display: swap for better performance
        const fontLink = document.createElement('link');
        fontLink.rel = 'stylesheet';
        fontLink.href = 'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Oswald:wght@500;700&display=swap';
        document.head.appendChild(fontLink);
    }

    // Initialize performance optimizations
    preloadCriticalResources();
    optimizeFontLoading();

    // Performance monitoring (optional)
    if ('performance' in window) {
        window.addEventListener('load', function() {
            setTimeout(function() {
                const perfData = performance.getEntriesByType('navigation')[0];
                console.log('Page load time:', perfData.loadEventEnd - perfData.loadEventStart, 'ms');
            }, 0);
        });
    }

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
});