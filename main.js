document.addEventListener('DOMContentLoaded', () => {

    // ── 1. Sticky Header shadow on scroll ──────────────────────────
    const header = document.querySelector('.header');
    if (header) {
        window.addEventListener('scroll', () => {
            header.classList.toggle('scrolled', window.scrollY > 50);
        }, { passive: true });
    }

    // ── 2. Mobile Nav Toggle (id="menuBtn" / id="mobileMenu") ──────
    const menuBtn    = document.getElementById('menuBtn');
    const mobileMenu = document.getElementById('mobileMenu');

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => {
            const isOpen = mobileMenu.classList.toggle('active');
            const icon   = menuBtn.querySelector('i');
            if (icon) icon.className = isOpen ? 'fas fa-times' : 'fas fa-bars';
        });

        // Close when a link inside mobile menu is clicked
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.remove('active');
                const icon = menuBtn.querySelector('i');
                if (icon) icon.className = 'fas fa-bars';
            });
        });

        // Close when clicking outside the header / mobile menu
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.header') && !e.target.closest('#mobileMenu')) {
                mobileMenu.classList.remove('active');
                const icon = menuBtn.querySelector('i');
                if (icon) icon.className = 'fas fa-bars';
            }
        });
    }

    // ── 3. Active nav link highlight ───────────────────────────────
    const currentFile = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav a, .mobile-menu a').forEach(link => {
        const href = link.getAttribute('href');
        if (href && href === currentFile) link.classList.add('active');
    });

    // ── 4. FAQ Accordion ───────────────────────────────────────────
    document.querySelectorAll('.faq-item').forEach(item => {
        const q = item.querySelector('.faq-q');
        if (!q) return;
        q.addEventListener('click', () => {
            const isOpen = item.classList.contains('open');
            // Close all
            document.querySelectorAll('.faq-item.open').forEach(other => other.classList.remove('open'));
            // Open clicked (if it was closed)
            if (!isOpen) item.classList.add('open');
        });
    });

    // ── 5. Contact Form Validation ─────────────────────────────────
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            let isValid = true;
            contactForm.querySelectorAll('[required]').forEach(input => {
                const group = input.closest('.form-group');
                if (!input.value.trim()) {
                    isValid = false;
                    if (group) group.classList.add('error');
                } else {
                    if (group) group.classList.remove('error');
                }
            });

            if (isValid) {
                contactForm.innerHTML = `
                    <div style="text-align:center;padding:3rem 1rem;">
                        <i class="fas fa-check-circle" style="font-size:3rem;color:var(--c-gold);margin-bottom:1rem;display:block;"></i>
                        <h4 style="font-family:var(--font-head);color:var(--c-navy);margin-bottom:0.5rem;">Message Sent Successfully!</h4>
                        <p style="color:var(--c-text-light);">Thank you for reaching out. An admission expert will contact you within 24 hours.</p>
                    </div>`;
            }
        });

        contactForm.querySelectorAll('input, select, textarea').forEach(input => {
            input.addEventListener('input', () => {
                const group = input.closest('.form-group');
                if (group) group.classList.remove('error');
            });
        });
    }

    // ── 6. Newsletter Form ─────────────────────────────────────────
    document.querySelectorAll('.nl-form').forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const input = form.querySelector('input');
            if (input && input.value.trim()) {
                alert(`Thank you for subscribing! We've sent a confirmation to ${input.value.trim()}`);
                input.value = '';
            }
        });
    });

    // ── 7. Dynamic footer year ─────────────────────────────────────
    const yearEl = document.getElementById('footerYear');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

});
