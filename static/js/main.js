// ROBETS TRAVEL AGENTS - Main JavaScript

// Dark mode toggle
document.querySelector('.dark-mode-toggle')?.addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    const icon = this.querySelector('i');
    if (document.body.classList.contains('dark-mode')) {
        icon.className = 'fas fa-sun';
        localStorage.setItem('darkMode', 'enabled');
    } else {
        icon.className = 'fas fa-moon';
        localStorage.setItem('darkMode', 'disabled');
    }
});

// Check saved dark mode preference
if (localStorage.getItem('darkMode') === 'enabled') {
    document.body.classList.add('dark-mode');
    const toggle = document.querySelector('.dark-mode-toggle i');
    if (toggle) toggle.className = 'fas fa-sun';
}

// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const menuBtn = document.getElementById('mobile-menu-btn');
    if (menuBtn) {
        menuBtn.addEventListener('click', function() {
            const menu = document.getElementById('mobile-menu');
            if (menu) menu.classList.toggle('hidden');
        });
    }
});

// Newsletter subscription
document.querySelector('.newsletter-form')?.addEventListener('submit', async function(e) {
    e.preventDefault();
    const email = this.querySelector('input[type="email"]').value;
    const button = this.querySelector('button');
    
    if (!email) {
        alert('Please enter your email address');
        return;
    }
    
    button.disabled = true;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Subscribing...';
    
    try {
        const response = await fetch('/api/subscribe', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email })
        });
        
        const data = await response.json();
        alert(data.message || 'Subscribed successfully!');
        this.reset();
    } catch (error) {
        alert('Something went wrong. Please try again.');
    } finally {
        button.disabled = false;
        button.innerHTML = 'Subscribe';
    }
});

// Gallery lightbox with smooth animation
document.querySelectorAll('.gallery-img').forEach(img => {
    img.addEventListener('click', function() {
        const lightbox = document.createElement('div');
        lightbox.className = 'fixed inset-0 bg-black/90 z-50 flex items-center justify-center p-4 animate__animated animate__fadeIn';
        lightbox.innerHTML = `
            <img src="${this.src}" class="max-h-[90vh] max-w-[90vw] object-contain rounded-lg shadow-2xl animate__animated animate__zoomIn">
            <button class="absolute top-4 right-4 text-white text-4xl hover:text-gray-300 transition transform hover:scale-125">&times;</button>
        `;
        document.body.appendChild(lightbox);
        lightbox.querySelector('button').addEventListener('click', () => {
            lightbox.classList.add('animate__fadeOut');
            setTimeout(() => lightbox.remove(), 500);
        });
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                lightbox.classList.add('animate__fadeOut');
                setTimeout(() => lightbox.remove(), 500);
            }
        });
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Form validation with animations
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        const required = this.querySelectorAll('[required]');
        let valid = true;
        
        required.forEach(field => {
            if (!field.value.trim()) {
                valid = false;
                field.classList.add('border-red-500');
                field.style.animation = 'shake 0.5s';
                setTimeout(() => {
                    field.classList.remove('border-red-500');
                    field.style.animation = '';
                }, 3000);
            }
        });
        
        if (!valid) {
            e.preventDefault();
            alert('Please fill in all required fields.');
        }
    });
});

// Counter animation for stats
function animateCounters() {
    const counters = document.querySelectorAll('.counter-value');
    counters.forEach(counter => {
        const target = parseInt(counter.dataset.target);
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;
        
        const updateCounter = () => {
            current += step;
            if (current < target) {
                counter.textContent = Math.round(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };
        updateCounter();
    });
}

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate__animated', 'animate__fadeInUp');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.animate-on-scroll').forEach(el => {
    observer.observe(el);
});

console.log('🚐 ROBETS TRAVEL AGENTS - Your trusted travel partner in Kampala, Uganda');
console.log('📞 Available 24/7: +256 700 123 456');

// Instead of toggle('hidden'), use style.display
menuBtn.addEventListener('click', function() {
    if (mobileMenu.style.display === 'block') {
        mobileMenu.style.display = 'none';
        this.innerHTML = '<i class="fas fa-bars"></i>';
    } else {
        mobileMenu.style.display = 'block';
        this.innerHTML = '<i class="fas fa-times"></i>';
    }
});