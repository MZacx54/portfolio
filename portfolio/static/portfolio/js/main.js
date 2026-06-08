/**
 * ZACHARIAH MESHACH - PORTFOLIO INTERACTIVE CORE
 * Vanilla ES6 Script
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. DYNAMIC NAVIGATION SHADING & LINK HIGHLIGHTING
    const navbar = document.getElementById('navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section');

    const handleNavbarScroll = () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    };

    const handleActiveLinkHighlight = () => {
        let currentSectionId = '';
        const scrollPosition = window.scrollY + 160;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', () => {
        handleNavbarScroll();
        handleActiveLinkHighlight();
    });
    
    // Initial triggers on load
    handleNavbarScroll();
    handleActiveLinkHighlight();

    // 2. MOBILE TOGGLE MENU
    const mobileToggle = document.getElementById('mobile-toggle');
    const navLinksContainer = document.getElementById('nav-links');

    if (mobileToggle && navLinksContainer) {
        mobileToggle.addEventListener('click', () => {
            const isOpened = navLinksContainer.style.display === 'flex';
            if (isOpened) {
                navLinksContainer.style.display = 'none';
                mobileToggle.querySelector('i').className = 'fas fa-bars';
            } else {
                navLinksContainer.style.display = 'flex';
                navLinksContainer.style.flexDirection = 'column';
                navLinksContainer.style.position = 'absolute';
                navLinksContainer.style.top = '100%';
                navLinksContainer.style.left = '0';
                navLinksContainer.style.width = '100%';
                navLinksContainer.style.backgroundColor = 'rgba(252, 252, 253, 0.98)';
                navLinksContainer.style.padding = '20px 24px';
                navLinksContainer.style.boxShadow = '0 10px 15px rgba(0,0,0,0.05)';
                navLinksContainer.style.borderBottom = '1px solid rgba(16, 24, 40, 0.08)';
                mobileToggle.querySelector('i').className = 'fas fa-times';
            }
        });

        // Close mobile menu on clicking any navigation link
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 900) {
                    navLinksContainer.style.display = 'none';
                    mobileToggle.querySelector('i').className = 'fas fa-bars';
                }
            });
        });
    }

    // 3. INTERACTIVE AJAX CONTACT FORM SUBMISSION
    const contactForm = document.getElementById('contactForm');
    const successAlert = document.getElementById('successAlert');
    const errorAlert = document.getElementById('errorAlert');
    const successMsgText = document.getElementById('successMsgText');
    const errorMsgText = document.getElementById('errorMsgText');
    const submitBtn = document.getElementById('submitBtn');

    if (contactForm) {
        contactForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            // Clear previous errors
            document.querySelectorAll('.error-msg').forEach(el => {
                el.style.display = 'none';
                el.innerText = '';
            });

            // Disable button and change state
            const origButtonText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = `<span>Sending...</span> <i class="fas fa-spinner fa-spin"></i>`;

            const formData = new FormData(contactForm);

            try {
                const response = await fetch(contactForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                });

                const data = await response.json();

                if (response.ok && data.success) {
                    // Success View
                    successMsgText.innerText = data.message;
                    successAlert.style.display = 'flex';
                    contactForm.reset();
                } else {
                    // Handling Form Errors
                    if (data.errors) {
                        for (const [field, error] of Object.entries(data.errors)) {
                            const errorContainer = document.getElementById(`error_${field}`);
                            if (errorContainer) {
                                errorContainer.innerText = error;
                                errorContainer.style.display = 'block';
                            }
                        }
                    }
                    throw new Error(data.message || 'Verification failed. Please review your form content.');
                }

            } catch (err) {
                errorMsgText.innerText = err.message || 'An unexpected error occurred while delivering your message. Please try again.';
                errorAlert.style.display = 'flex';
            } finally {
                // Restore button
                submitBtn.disabled = false;
                submitBtn.innerHTML = origButtonText;
            }
        });
    }

    // Reset Alert Screens
    const resetAlertBtn = document.getElementById('resetAlertBtn');
    const retryAlertBtn = document.getElementById('retryAlertBtn');

    if (resetAlertBtn) {
        resetAlertBtn.addEventListener('click', () => {
            successAlert.style.display = 'none';
        });
    }

    if (retryAlertBtn) {
        retryAlertBtn.addEventListener('click', () => {
            errorAlert.style.display = 'none';
        });
    }
});
