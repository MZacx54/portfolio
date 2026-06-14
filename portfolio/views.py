from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
import os
from django.conf import settings
from .models import Skill, Project, Experience, Education, Certificate
from .forms import ContactForm

def index(request):
    # Fetch all data from the database
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    certificates = Certificate.objects.all()
    
    # Categorize skills for easy rendering in templates
    skills_web_dev = skills.filter(category='web_dev')
    skills_digital_mkt = skills.filter(category='digital_mkt')
    skills_design = skills.filter(category='design')
    skills_soft_skills = skills.filter(category='soft_skills')
    
    # Initialize the contact form
    contact_form = ContactForm()
    
    context = {
        'skills_web_dev': skills_web_dev,
        'skills_digital_mkt': skills_digital_mkt,
        'skills_design': skills_design,
        'skills_soft_skills': skills_soft_skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
        'certificates': certificates,
        'contact_form': contact_form,
        'personal_info': {
            'name': 'Zachariah Meshach',
            'degree': 'B.Tech.',
            'title': 'Innovative Full-Stack Web Developer',
            'email': 'meshachzax@gmail.com',
            'mobile1': '09064556107',
            'mobile2': '08021460391',
            'address': 'NO. 35 Adjacent Deeper Life, Sabon Kaura, ATBU Yelwa Bauchi, Bauchi State, Nigeria',
            'github': 'https://github.com/MZacx54',
            'bio': 'Innovative B.Tech Medical Biochemistry graduate turned Full-Stack Web Developer. Highly skilled in building robust back-ends using Python and Django, and styling beautiful, responsive front-ends with HTML, CSS, JavaScript, and CMS (WordPress/Elementor). Adept at project management, customer relations, and analytical problem-solving, with a results-oriented mindset that drives digital innovation.'
        }
    }
    return render(request, 'portfolio/index.html', context)


@require_POST
def contact_submit(request):
    # Spam honeypot check
    if request.POST.get('website_url'):
        # Silently return success to trick the bot
        return JsonResponse({
            'success': True,
            'message': 'Your message has been sent successfully! Zachariah will contact you shortly.'
        })

    form = ContactForm(request.POST)
    if form.is_valid():
        message_instance = form.save()
        
        # Email Zachariah about the new lead
        from django.core.mail import send_mail
        import logging
        logger = logging.getLogger(__name__)
        try:
            send_mail(
                subject=f"New Portfolio Lead: {message_instance.subject}",
                message=f"You have received a new contact message from your portfolio website.\n\n"
                        f"Name: {message_instance.name}\n"
                        f"Email: {message_instance.email}\n\n"
                        f"Message:\n{message_instance.message}",
                from_email=None,  # Will use DEFAULT_FROM_EMAIL from settings
                recipient_list=[settings.CONTACT_ALERT_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            logger.error(f"Failed to send email alert: {e}", exc_info=True)
            # Try fallback to localhost:25 (cPanel's built-in Exim mailer)
            try:
                from django.core.mail.backends.smtp import EmailBackend
                import django.core.mail
                local_backend = EmailBackend(host='localhost', port=25, username='', password='', use_tls=False, use_ssl=False, timeout=10)
                msg = django.core.mail.EmailMessage(
                    subject=f"New Portfolio Lead: {message_instance.subject}",
                    body=f"You have received a new contact message from your portfolio website.\n\n"
                         f"Name: {message_instance.name}\n"
                         f"Email: {message_instance.email}\n\n"
                         f"Message:\n{message_instance.message}",
                    from_email='noreply@smartbizcoach.com.ng',
                    to=[settings.CONTACT_ALERT_EMAIL],
                )
                local_backend.send_messages([msg])
                logger.info("Email sent successfully using local SMTP fallback.")
            except Exception as fallback_e:
                logger.error(f"Failed to send email alert via local fallback: {fallback_e}", exc_info=True)


        return JsonResponse({
            'success': True,
            'message': 'Your message has been sent successfully! Zachariah will contact you shortly.'
        })
    else:
        errors = {field: error_list[0] for field, error_list in form.errors.items()}
        return JsonResponse({
            'success': False,
            'message': 'Failed to send message. Please correct the errors in the form.',
            'errors': errors
        }, status=400)


def download_resume(request):
    # Search for an uploaded resume PDF in media directory first
    resume_filename = 'Zachariah_Meshach_Resume.pdf'
    media_path = os.path.join(settings.MEDIA_ROOT, resume_filename)
    
    if os.path.exists(media_path):
        with open(media_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{resume_filename}"'
            return response
            
    # If not found in media, let's look in static
    static_path = os.path.join(settings.BASE_DIR, 'static', 'portfolio', 'resume.pdf')
    if os.path.exists(static_path):
        with open(static_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{resume_filename}"'
            return response

    # Dynamic plain text/HTML fallback if PDF doesn't exist yet
    fallback_text = (
        "ZACHARIAH MESHACH, B.Tech. - RESUME\n"
        "====================================\n"
        "Address: NO. 35 Adjacent Deeper Life, Sabon Kaura, ATBU Yelwa Bauchi, Bauchi State, Nigeria\n"
        "Email: meshachzax@gmail.com\n"
        "Mobile: 08021460391, 09064556107\n\n"
        "Please visit the online portfolio to view complete dynamic experiences, skills, and certifications.\n"
        "To upload a real PDF, simply place a file named 'Zachariah_Meshach_Resume.pdf' under the 'media' or 'static/portfolio/resume.pdf' directory."
    )
    response = HttpResponse(fallback_text, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="Zachariah_Meshach_Resume.txt"'
    return response


def test_email(request):
    from django.core.mail import send_mail
    import django.core.mail
    import traceback
    
    # Try using configured settings first
    try:
        send_mail(
            subject="SMTP Live Test from Portfolio",
            message="If you see this, SMTP is working perfectly!",
            from_email=None,
            recipient_list=[settings.CONTACT_ALERT_EMAIL],
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully to " + settings.CONTACT_ALERT_EMAIL)
    except Exception as e:
        configured_error = traceback.format_exc()
        
    # Try local SMTP fallback
    try:
        from django.core.mail.backends.smtp import EmailBackend
        local_backend = EmailBackend(
            host='localhost',
            port=25,
            username='',
            password='',
            use_tls=False,
            use_ssl=False,
            timeout=10
        )
        msg = django.core.mail.EmailMessage(
            subject="Local SMTP Fallback Test",
            body="If you see this, local SMTP (localhost:25) is working perfectly on cPanel!",
            from_email='noreply@smartbizcoach.com.ng',
            to=[settings.CONTACT_ALERT_EMAIL]
        )
        local_backend.send_messages([msg])
        local_succeeded = True
    except Exception as e:
        local_error = traceback.format_exc()
        local_succeeded = False
        
    if local_succeeded:
        return HttpResponse("Brevo SMTP failed, but Local SMTP (localhost:25) succeeded! You can switch to Local SMTP.")
        
    debug_info = (
        f"Debug Info:\n"
        f"- Host: {settings.EMAIL_HOST}\n"
        f"- Port: {settings.EMAIL_PORT}\n"
        f"- User: {settings.EMAIL_HOST_USER} (len: {len(settings.EMAIL_HOST_USER)})\n"
        f"- Pass prefix: {settings.EMAIL_HOST_PASSWORD[:8]}... (len: {len(settings.EMAIL_HOST_PASSWORD)})\n"
        f"- Recipient: {settings.CONTACT_ALERT_EMAIL}\n\n"
    )
    return HttpResponse(
        debug_info + 
        "=== Configured SMTP Error ===\n" + configured_error + "\n\n" +
        "=== Local SMTP Error ===\n" + local_error,
        content_type="text/plain"
    )



