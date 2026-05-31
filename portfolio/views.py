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
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
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
