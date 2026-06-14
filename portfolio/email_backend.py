import ssl
from django.core.mail.backends.smtp import EmailBackend as SMTPBackend
from django.utils.functional import cached_property

class InsecureEmailBackend(SMTPBackend):
    """
    A custom SMTP backend that bypasses SSL/TLS certificate verification.
    Useful for shared hosting environments (like cPanel) where outbound 
    SMTP connections on ports 587/465 are intercepted/proxied by the host, 
    causing SSL/TLS hostname mismatch errors.
    """
    @cached_property
    def ssl_context(self):
        context = ssl._create_unverified_context()
        return context
