import os
import django
import sys

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Initialize Django
django.setup()

from django.contrib.auth.models import User
from portfolio.models import Skill, Project, Experience, Education, Certificate

def seed_database():
    print("Starting database seeding...")
    
    # 1. Create a superuser if none exists
    if not User.objects.filter(username='admin').exists():
        print("Creating superuser 'admin'...")
        User.objects.create_superuser('admin', 'meshachzax@gmail.com', 'admin1234')
        print("Superuser created successfully! (Username: admin, Password: admin1234)")
    else:
        print("Superuser 'admin' already exists.")
        
    # Clear existing data to avoid duplicates
    print("Clearing old records...")
    Skill.objects.all().delete()
    Project.objects.all().delete()
    Experience.objects.all().delete()
    Education.objects.all().delete()
    Certificate.objects.all().delete()
    
    # 2. Seed Skills
    print("Seeding skills...")
    skills_data = [
        # Web Dev
        {'category': 'web_dev', 'name': 'Python & Django', 'proficiency': 95, 'icon_class': 'fab fa-python', 'order': 1},
        {'category': 'web_dev', 'name': 'React & Next.js', 'proficiency': 90, 'icon_class': 'fab fa-react', 'order': 2},
        {'category': 'web_dev', 'name': 'Tailwind CSS & Bootstrap', 'proficiency': 92, 'icon_class': 'fab fa-css3-alt', 'order': 3},
        {'category': 'web_dev', 'name': 'RESTful APIs & PostgreSQL', 'proficiency': 88, 'icon_class': 'fas fa-database', 'order': 4},
        
        # Digital Marketing
        {'category': 'digital_mkt', 'name': 'GEO & AI Marketing Strategist', 'proficiency': 90, 'icon_class': 'fas fa-robot', 'order': 1},
        {'category': 'digital_mkt', 'name': 'Google Ads & Meta Business Suite', 'proficiency': 88, 'icon_class': 'fas fa-ad', 'order': 2},
        {'category': 'digital_mkt', 'name': 'Mailchimp & Email Marketing', 'proficiency': 85, 'icon_class': 'fas fa-envelope-open-text', 'order': 3},
        {'category': 'digital_mkt', 'name': 'Prompt Engineering', 'proficiency': 92, 'icon_class': 'fas fa-terminal', 'order': 4},
        
        # Creative Design & CMS
        {'category': 'design', 'name': 'WordPress & Elementor', 'proficiency': 90, 'icon_class': 'fab fa-wordpress', 'order': 1},
        {'category': 'design', 'name': 'Adobe Photoshop', 'proficiency': 85, 'icon_class': 'fas fa-palette', 'order': 2},
        {'category': 'design', 'name': 'Content Creation', 'proficiency': 80, 'icon_class': 'fas fa-pen-nib', 'order': 3},
        
        # Soft Skills
        {'category': 'soft_skills', 'name': 'Analytical & Problem Solving', 'proficiency': 95, 'icon_class': 'fas fa-brain', 'order': 1},
        {'category': 'soft_skills', 'name': 'Agile Methodologies', 'proficiency': 90, 'icon_class': 'fas fa-sync', 'order': 2},
        {'category': 'soft_skills', 'name': 'Project Management', 'proficiency': 92, 'icon_class': 'fas fa-tasks', 'order': 3},
    ]
    
    for skill in skills_data:
        Skill.objects.create(**skill)
        
    # 3. Seed Projects
    print("Seeding projects...")
    projects_data = [
        {
            'name': 'SmartBiz Coach',
            'description': 'An interactive, AI-driven business coaching platform empowering users with GEO (Generative Engine Optimization) insights, personalized Prompt Engineering recommendations, and digital marketing analytics.',
            'tech_stack': 'React, Next.js, Django, Tailwind CSS, OpenAI API',
            'github_url': 'MZacx54/Smartbiz',
            'live_url': 'https://smartbizcoach.com.ng/',
            'icon_class': 'fas fa-robot',
            'order': 1
        },
        {
            'name': 'JDPC Bauchi',
            'description': 'A responsive, high-performance web platform built for the Justice Development and Peace Commission (JDPC), featuring custom CMS, data visualization, and SEO-optimized architecture.',
            'tech_stack': 'Python, Django, Bootstrap, SQLite',
            'github_url': 'MZacx54/Judsci',
            'live_url': 'https://www.judsci.org.ng/',
            'icon_class': 'fas fa-hand-holding-heart',
            'order': 2
        }
    ]
    
    for project in projects_data:
        Project.objects.create(**project)
        
    # 4. Seed Experiences
    print("Seeding experience timeline...")
    experiences_data = [
        {
            'role': 'IT Manager & Lead Developer',
            'company': 'Emperor Business Center',
            'location': 'Bauchi State, Nigeria',
            'start_date': '2025',
            'end_date': 'Present',
            'description': 'Architecting robust IT solutions and web infrastructure.\nImplementing AI-driven strategies to automate business processes and improve operational efficiency.',
            'order': 1
        },
        {
            'role': 'Full-Stack Web Developer & Marketing Strategist',
            'company': 'Zacx Maxicool Ventures',
            'location': 'Bauchi State, Nigeria',
            'start_date': '2019',
            'end_date': 'Present',
            'description': 'Developing scalable web applications using modern frameworks like React, Next.js, and Django.\nOrchestrating high-converting marketing campaigns via Google Ads, Meta Business Suite, and Mailchimp.\nApplying Generative Engine Optimization (GEO) techniques to boost organic traffic and conversions.',
            'order': 2
        },
        {
            'role': 'IT Developer',
            'company': 'National Biotechnology Research and Development Agency (NBRDA)',
            'location': 'Abuja, Nigeria',
            'start_date': '2024',
            'end_date': '2024',
            'description': 'Built internal software tools and dashboards using Python to optimize data tracking and analytics.\nCollaborated with cross-functional teams using Agile methodologies.',
            'order': 3
        }
    ]
    
    for exp in experiences_data:
        Experience.objects.create(**exp)
        
    # 5. Seed Educations
    print("Seeding education details...")
    educations_data = [
        {
            'degree': 'Full-Stack Web Development & AI Marketing',
            'school': 'Continuous Professional Development',
            'year': '2019 - Present',
            'description': 'Intensive hands-on experience and self-directed learning in building modern web architectures (React, Next.js, Django, Tailwind) and executing AI-driven marketing strategies (Prompt Engineering, GEO, Google Ads).',
            'order': 1
        },
        {
            'degree': 'Bachelor of Technology (B. Tech)',
            'school': 'Abubakar Tafawa Balewa University Bauchi',
            'year': '2019 - 2025',
            'description': 'Developed strong analytical, problem-solving, and research skills through rigorous technical curriculum, seamlessly transferring these capabilities to complex software engineering and data modeling.',
            'order': 2
        }
    ]
    
    for edu in educations_data:
        Education.objects.create(**edu)
        
    # 6. Seed Certificates
    print("Seeding certificates obtained...")
    certificates_data = [
        {'title': 'Prompt Engineering', 'issuer': 'Coursera (Google)', 'year': '2024', 'order': 1},
        {'title': 'Vibe Coding', 'issuer': 'Coursera', 'year': '2024', 'order': 2},
        {'title': 'Generative AI', 'issuer': 'Microsoft', 'year': '2024', 'order': 3},
        {'title': 'Data Science (3MTT)', 'issuer': '3MTT Program', 'year': '2024', 'order': 4},
        {'title': 'React & Next.js Specialization', 'issuer': 'Self-Taught / Industry Practice', 'year': '2023', 'order': 5},
        {'title': 'Social Media Marketing & Meta Ads', 'issuer': 'Coursera', 'year': '2023', 'order': 6},
    ]
    
    for cert in certificates_data:
        Certificate.objects.create(**cert)
        
    return "Database seeding completed successfully! All portfolios populated!"

if __name__ == '__main__':
    seed_database()
