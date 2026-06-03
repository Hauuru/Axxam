// Sticky Navigation and Scroll Animations
document.addEventListener('DOMContentLoaded', function() {
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
    
    // Lazy loading for images
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img.lazy').forEach(img => {
            imageObserver.observe(img);
        });
    }
});