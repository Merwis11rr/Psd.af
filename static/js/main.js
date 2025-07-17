// Persian Design Portfolio JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initializeAnimations();
    
    // Initialize smooth scrolling
    initializeSmoothScrolling();
    
    // Initialize contact form
    initializeContactForm();
    
    // Initialize portfolio tabs
    initializePortfolioTabs();
    
    // Initialize navbar behavior
    initializeNavbar();
    
    // Initialize lazy loading for placeholder images
    initializeLazyLoading();
});

// Animation on scroll
function initializeAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);
    
    // Observe all cards and sections
    const animatedElements = document.querySelectorAll(
        '.service-card, .portfolio-card, .archive-item, .testimonial-card, .contact-form-wrapper, .contact-info'
    );
    
    animatedElements.forEach(element => {
        observer.observe(element);
    });
}

// Smooth scrolling for anchor links
function initializeSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Contact form enhancements
function initializeContactForm() {
    const contactForm = document.querySelector('.contact-form');
    
    if (contactForm) {
        // Add form validation
        contactForm.addEventListener('submit', function(e) {
            const name = this.querySelector('#name').value.trim();
            const email = this.querySelector('#email').value.trim();
            const message = this.querySelector('#message').value.trim();
            
            if (!name || !email || !message) {
                e.preventDefault();
                showAlert('لطفاً تمام فیلدهای ضروری را پر کنید.', 'error');
                return false;
            }
            
            if (!isValidEmail(email)) {
                e.preventDefault();
                showAlert('لطفاً ایمیل معتبر وارد کنید.', 'error');
                return false;
            }
            
            // Show loading state
            const submitBtn = this.querySelector('button[type="submit"]');
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>در حال ارسال...';
            submitBtn.disabled = true;
        });
        
        // Add real-time validation
        const inputs = contactForm.querySelectorAll('input, textarea');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
        });
    }
}

// Email validation
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Field validation
function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.getAttribute('name');
    
    // Remove existing validation classes
    field.classList.remove('is-valid', 'is-invalid');
    
    if (field.hasAttribute('required') && !value) {
        field.classList.add('is-invalid');
        return false;
    }
    
    if (fieldName === 'email' && value && !isValidEmail(value)) {
        field.classList.add('is-invalid');
        return false;
    }
    
    if (value) {
        field.classList.add('is-valid');
    }
    
    return true;
}

// Show alert messages
function showAlert(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type === 'error' ? 'danger' : 'success'} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Insert alert at the top of the main content
    const main = document.querySelector('main');
    const container = document.createElement('div');
    container.className = 'container mt-3';
    container.appendChild(alertDiv);
    
    main.insertBefore(container, main.firstChild);
    
    // Auto-hide after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentElement) {
            alertDiv.remove();
        }
    }, 5000);
}

// Portfolio tabs functionality
function initializePortfolioTabs() {
    const tabButtons = document.querySelectorAll('#portfolioTabs .nav-link');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            tabButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // Filter portfolio items (if needed)
            const targetTab = this.getAttribute('data-bs-target');
            filterPortfolioItems(targetTab);
        });
    });
}

// Filter portfolio items
function filterPortfolioItems(category) {
    const portfolioItems = document.querySelectorAll('.archive-item');
    
    portfolioItems.forEach(item => {
        if (category === '#all') {
            item.style.display = 'block';
            item.classList.add('slide-up');
        } else {
            // This would filter based on data attributes in a real implementation
            item.style.display = 'block';
            item.classList.add('slide-up');
        }
    });
}

// Navbar behavior
function initializeNavbar() {
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Add/remove scrolled class
        if (scrollTop > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Hide/show navbar on scroll (optional)
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // Scrolling down
            navbar.style.transform = 'translateY(-100%)';
        } else {
            // Scrolling up
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = scrollTop;
    });
    
    // Add smooth transition
    navbar.style.transition = 'transform 0.3s ease, background-color 0.3s ease';
}

// Lazy loading for placeholder images
function initializeLazyLoading() {
    const placeholderImages = document.querySelectorAll('.placeholder-image');
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add loaded class for animation
                entry.target.classList.add('loaded');
                
                // Unobserve the element
                imageObserver.unobserve(entry.target);
            }
        });
    });
    
    placeholderImages.forEach(img => {
        imageObserver.observe(img);
    });
}

// Utility functions
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

// Add CSS class for scrolled navbar
const style = document.createElement('style');
style.textContent = `
    .navbar.scrolled {
        background: rgba(0, 0, 0, 0.95) !important;
        backdrop-filter: blur(15px);
    }
    
    .placeholder-image.loaded {
        animation: imageLoad 0.5s ease-in;
    }
    
    @keyframes imageLoad {
        from {
            opacity: 0.5;
            transform: scale(0.95);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    .is-valid {
        border-color: #28a745 !important;
        box-shadow: 0 0 0 0.2rem rgba(40, 167, 69, 0.25) !important;
    }
    
    .is-invalid {
        border-color: #dc3545 !important;
        box-shadow: 0 0 0 0.2rem rgba(220, 53, 69, 0.25) !important;
    }
`;
document.head.appendChild(style);

// Initialize tooltips and popovers (if Bootstrap is being used)
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Initialize Bootstrap popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
});

// Add click tracking for analytics (placeholder)
function trackClick(element, action) {
    // This would integrate with analytics services
    console.log(`Tracked: ${action} on ${element}`);
}

// Add WhatsApp click tracking
document.addEventListener('click', function(e) {
    if (e.target.closest('.whatsapp-link, .whatsapp-btn')) {
        trackClick('WhatsApp', 'Contact');
    }
    
    if (e.target.closest('.btn-primary')) {
        trackClick('Button', 'Primary Action');
    }
});

// Performance optimization: Preload critical resources
function preloadCriticalResources() {
    const criticalResources = [
        'https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap'
    ];
    
    criticalResources.forEach(resource => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.href = resource;
        link.as = 'style';
        document.head.appendChild(link);
    });
}

// Call preload function
preloadCriticalResources();
