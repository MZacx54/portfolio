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
        # Full-Stack Web Development & Software Engineering
        {'category': 'web_dev', 'name': 'Python & Django (REST APIs & Architecture)', 'proficiency': 95, 'icon_class': 'fab fa-python', 'order': 1},
        {'category': 'web_dev', 'name': 'React & Next.js (Modern Frontend)', 'proficiency': 90, 'icon_class': 'fab fa-react', 'order': 2},
        {'category': 'web_dev', 'name': 'Tailwind CSS & Bootstrap', 'proficiency': 92, 'icon_class': 'fab fa-css3-alt', 'order': 3},
        {'category': 'web_dev', 'name': 'PostgreSQL & Database Management', 'proficiency': 88, 'icon_class': 'fas fa-database', 'order': 4},
        {'category': 'web_dev', 'name': 'Prompt Engineering & AI Integrations', 'proficiency': 92, 'icon_class': 'fas fa-terminal', 'order': 5},
        
        # Modern Digital Marketing & Growth Strategy
        {'category': 'digital_mkt', 'name': 'GEO & AI Search Optimization (Perplexity/SearchGPT)', 'proficiency': 92, 'icon_class': 'fas fa-robot', 'order': 1},
        {'category': 'digital_mkt', 'name': 'Google Ads & Meta Business Suite (PPC & ROAS)', 'proficiency': 90, 'icon_class': 'fas fa-ad', 'order': 2},
        {'category': 'digital_mkt', 'name': 'Customer Engagement & Retention Strategy', 'proficiency': 88, 'icon_class': 'fas fa-users-cog', 'order': 3},
        {'category': 'digital_mkt', 'name': 'SEO, Local SEO & Google Business Profile (5.0★)', 'proficiency': 92, 'icon_class': 'fas fa-map-marker-alt', 'order': 4},
        {'category': 'digital_mkt', 'name': 'TikTok & Video Marketing Growth Strategy', 'proficiency': 85, 'icon_class': 'fab fa-tiktok', 'order': 5},
        {'category': 'digital_mkt', 'name': 'Marketing Analytics (GA4, Meta Pixel, CRO)', 'proficiency': 86, 'icon_class': 'fas fa-chart-line', 'order': 6},
        {'category': 'digital_mkt', 'name': 'Email Marketing & CRM Automation (Mailchimp)', 'proficiency': 86, 'icon_class': 'fas fa-envelope-open-text', 'order': 7},
        
        # Creative Design & CMS
        {'category': 'design', 'name': 'WordPress & Elementor (Custom CMS)', 'proficiency': 90, 'icon_class': 'fab fa-wordpress', 'order': 1},
        {'category': 'design', 'name': 'Adobe Photoshop', 'proficiency': 85, 'icon_class': 'fas fa-palette', 'order': 2},
        {'category': 'design', 'name': 'Corel Draw', 'proficiency': 82, 'icon_class': 'fas fa-bezier-curve', 'order': 3},
        {'category': 'design', 'name': 'Canva Pro & Brand Collateral', 'proficiency': 88, 'icon_class': 'fas fa-object-group', 'order': 4},
        {'category': 'design', 'name': 'Social Media Visual Content Creation', 'proficiency': 85, 'icon_class': 'fas fa-pen-nib', 'order': 5},
        
        # Soft & Transferable Skills
        {'category': 'soft_skills', 'name': 'Analytical & Problem Solving', 'proficiency': 95, 'icon_class': 'fas fa-brain', 'order': 1},
        {'category': 'soft_skills', 'name': 'Agile Methodologies & Scrum', 'proficiency': 90, 'icon_class': 'fas fa-sync', 'order': 2},
        {'category': 'soft_skills', 'name': 'Project & Client Management', 'proficiency': 92, 'icon_class': 'fas fa-tasks', 'order': 3},
        
        # DevOps & Cloud Deployment
        {'category': 'devops', 'name': 'Vercel & Railway (Frontend/Backend)', 'proficiency': 90, 'icon_class': 'fas fa-rocket', 'order': 1},
        {'category': 'devops', 'name': 'Firebase (Hosting, Auth & Firestore)', 'proficiency': 85, 'icon_class': 'fas fa-fire', 'order': 2},
        {'category': 'devops', 'name': 'Render & Supabase (Backend & DB)', 'proficiency': 85, 'icon_class': 'fas fa-cloud', 'order': 3},
        {'category': 'devops', 'name': 'cPanel & Shared Hosting (Production)', 'proficiency': 92, 'icon_class': 'fas fa-server', 'order': 4},
        {'category': 'devops', 'name': 'Git & CI/CD Workflows', 'proficiency': 88, 'icon_class': 'fab fa-git-alt', 'order': 5},
    ]
    
    for skill in skills_data:
        Skill.objects.create(**skill)
        
    # 3. Seed Projects
    print("Seeding projects...")
    projects_data = [
        {
            'name': 'SmartBiz Digital Agency',
            'description': 'Full-service digital agency platform and local business presence providing bespoke web development, Generative Engine Optimization (GEO), Meta/Google Ads management, and brand strategy with a verified 5.0★ Google rating.',
            'tech_stack': 'Next.js, Tailwind CSS, Google Business Profile, Meta Business Suite, GA4',
            'github_url': 'MZacx54/portfolio',
            'live_url': 'https://share.google/teV7OZwWQTruKLTGA',
            'icon_class': 'fas fa-bullhorn',
            'order': 1
        },
        {
            'name': 'SmartBiz Coach',
            'description': 'An interactive, AI-driven business coaching platform empowering users with GEO (Generative Engine Optimization) insights, personalized Prompt Engineering recommendations, and digital marketing analytics.',
            'tech_stack': 'React, Next.js, Django, Tailwind CSS, OpenAI API',
            'github_url': 'MZacx54/smartbiz-coach',
            'live_url': 'https://smartbizcoach.com.ng/',
            'icon_class': 'fas fa-robot',
            'order': 2
        },
        {
            'name': 'JDPC Bauchi',
            'description': 'A responsive, high-performance web platform built for the Justice Development and Peace Commission (JDPC), featuring custom CMS, data visualization, and SEO-optimized architecture.',
            'tech_stack': 'Python, Django, Bootstrap, SQLite',
            'github_url': 'MZacx54/Judsci',
            'live_url': 'https://www.judsci.org.ng/',
            'icon_class': 'fas fa-hand-holding-heart',
            'order': 3
        },
        {
            'name': 'Personal Portfolio Platform',
            'description': 'A dynamic, dark-themed personal portfolio website. Features a custom Django backend with SQLite, optimized SEO architecture, modern UI animations, and automated deployment pipelines.',
            'tech_stack': 'Django, Python, HTML5, Vanilla CSS',
            'github_url': 'MZacx54/portfolio',
            'live_url': 'https://portfolio.smartbizcoach.com.ng/',
            'icon_class': 'fas fa-id-card',
            'order': 4
        }
    ]
    
    for project in projects_data:
        Project.objects.create(**project)
        
    # 4. Seed Experiences
    print("Seeding experience timeline...")
    experiences_data = [
        {
            'role': 'Founder & Lead Digital Strategist / Full-Stack Engineer',
            'company': 'SmartBiz Digital Agency (formerly Zacx Digital Agency)',
            'location': 'Bauchi, Nigeria & Remote',
            'start_date': '2019',
            'end_date': 'Present',
            'description': 'Founded and scaled a full-service digital agency, maintaining a verified 5.0★ Google Business Profile.\nArchitecting bespoke web applications using Python/Django, React, Next.js, and WordPress.\nOrchestrating multi-channel paid acquisition campaigns across Google Ads, Meta Business Suite (Facebook/Instagram), and TikTok.\nExecuting Generative Engine Optimization (GEO), Local SEO, and customer retention strategies that drive verifiable lead generation and conversion.',
            'order': 1
        },
        {
            'role': 'IT Manager & Lead Developer',
            'company': 'Emperor Business Center',
            'location': 'Bauchi State, Nigeria',
            'start_date': '2025',
            'end_date': 'Present',
            'description': 'Architecting robust IT solutions and web infrastructure.\nImplementing AI-driven strategies to automate business processes and improve operational efficiency.',
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
            'description': 'Intensive hands-on experience and self-directed learning in building modern web architectures (React, Next.js, Django, Tailwind) and executing AI-driven marketing strategies (Prompt Engineering, GEO, Google Ads, Meta Ads).',
            'order': 1
        },
        {
            'degree': 'Bachelor of Technology (B. Tech)',
            'school': 'Abubakar Tafawa Balewa University Bauchi',
            'year': '2019 - 2025',
            'description': 'Developed strong analytical, problem-solving, and research skills through rigorous technical curriculum, seamlessly transferring these capabilities to complex software engineering, systems design, and data-driven marketing.',
            'order': 2
        }
    ]
    
    for edu in educations_data:
        Education.objects.create(**edu)
        
    # 6. Seed Certificates
    print("Seeding certificates obtained...")
    certificates_data = [
        {'title': 'Digital Marketing: Customer Engagement Strategy', 'issuer': 'Univ. of Illinois Urbana-Champaign (Coursera)', 'year': '2024', 'order': 1},
        {'title': 'The Digital Marketing Revolution', 'issuer': 'Univ. of Illinois Urbana-Champaign (Coursera)', 'year': '2024', 'order': 2},
        {'title': 'Getting Started with TikTok', 'issuer': 'Aptly (Coursera)', 'year': '2024', 'order': 3},
        {'title': 'Prompt Engineering Specialization', 'issuer': 'Coursera (Google)', 'year': '2024', 'order': 4},
        {'title': 'Generative AI for Leaders & Developers', 'issuer': 'Microsoft', 'year': '2024', 'order': 5},
        {'title': 'Social Media Marketing & Meta Ads', 'issuer': 'Meta / Coursera', 'year': '2023', 'order': 6},
        {'title': 'Data Science Fellowship', 'issuer': '3MTT Program', 'year': '2024', 'order': 7},
        {'title': 'React & Next.js Specialization', 'issuer': 'Industry Practice & Self-Directed', 'year': '2023', 'order': 8},
    ]
    
    for cert in certificates_data:
        Certificate.objects.create(**cert)
        
    return "Database seeding completed successfully! All portfolios populated!"

if __name__ == '__main__':
    seed_database()
