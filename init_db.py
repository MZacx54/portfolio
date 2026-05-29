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
        {'category': 'web_dev', 'name': 'Python & Django', 'proficiency': 92, 'icon_class': 'fab fa-python', 'order': 1},
        {'category': 'web_dev', 'name': 'HTML5 & CSS3', 'proficiency': 95, 'icon_class': 'fab fa-html5', 'order': 2},
        {'category': 'web_dev', 'name': 'JavaScript (ES6)', 'proficiency': 82, 'icon_class': 'fab fa-js', 'order': 3},
        {'category': 'web_dev', 'name': 'WordPress & Elementor', 'proficiency': 90, 'icon_class': 'fab fa-wordpress', 'order': 4},
        
        # Digital Marketing
        {'category': 'digital_mkt', 'name': 'SEO & SEM', 'proficiency': 85, 'icon_class': 'fas fa-search', 'order': 1},
        {'category': 'digital_mkt', 'name': 'Social Media Specialist', 'proficiency': 88, 'icon_class': 'fas fa-share-alt', 'order': 2},
        {'category': 'digital_mkt', 'name': 'Google Analytics', 'proficiency': 80, 'icon_class': 'fas fa-chart-bar', 'order': 3},
        {'category': 'digital_mkt', 'name': 'TikTok Marketing', 'proficiency': 82, 'icon_class': 'fab fa-tiktok', 'order': 4},
        
        # Creative Design & CMS
        {'category': 'design', 'name': 'Adobe Photoshop', 'proficiency': 85, 'icon_class': 'fas fa-palette', 'order': 1},
        {'category': 'design', 'name': 'Adobe Illustrator', 'proficiency': 78, 'icon_class': 'fas fa-vector-square', 'order': 2},
        {'category': 'design', 'name': 'GIMP', 'proficiency': 80, 'icon_class': 'fas fa-paint-brush', 'order': 3},
        {'category': 'design', 'name': 'Graphic Asset Creation', 'proficiency': 80, 'icon_class': 'fas fa-image', 'order': 4},
        
        # Soft Skills
        {'category': 'soft_skills', 'name': 'Analytical & Problem Solving', 'proficiency': 95, 'icon_class': 'fas fa-brain', 'order': 1},
        {'category': 'soft_skills', 'name': 'Project Management', 'proficiency': 90, 'icon_class': 'fas fa-tasks', 'order': 2},
        {'category': 'soft_skills', 'name': 'Customer Relations', 'proficiency': 92, 'icon_class': 'fas fa-comments', 'order': 3},
        {'category': 'soft_skills', 'name': 'Research & Biochemistry', 'proficiency': 88, 'icon_class': 'fas fa-flask', 'order': 4},
    ]
    
    for skill in skills_data:
        Skill.objects.create(**skill)
        
    # 3. Seed Projects
    print("Seeding projects...")
    projects_data = [
        {
            'name': 'JDPC Bauchi',
            'description': 'A full-featured responsive NGO web platform built for the Justice Development and Peace Commission (JDPC) in Bauchi, supporting advocacy reporting, community development tracking, and media resources.',
            'tech_stack': 'Python, Django, HTML5/CSS3, SQLite',
            'github_url': 'MZacx54/Judsci',
            'live_url': 'https://www.judsci.org.ng/',
            'icon_class': 'fas fa-hand-holding-heart',
            'order': 1
        },
        {
            'name': 'SmartBiz Coach',
            'description': 'An interactive, AI-driven business coaching platform that empowers small-to-medium business owners in Nigeria with data-informed recommendations, digital templates, and strategic analytics.',
            'tech_stack': 'Python, Django, JavaScript (ES6), OpenAI API',
            'github_url': 'MZacx54/Judsci',
            'live_url': 'https://smartbizcoach.com.ng/',
            'icon_class': 'fas fa-brain',
            'order': 2
        }
    ]
    
    for project in projects_data:
        Project.objects.create(**project)
        
    # 4. Seed Experiences
    print("Seeding experience timeline...")
    experiences_data = [
        {
            'role': 'IT Manager',
            'company': 'Emperor Business Center',
            'location': 'Bauchi State, Nigeria',
            'start_date': '2025',
            'end_date': 'Present',
            'description': 'Spearheading general IT system upgrades and database installations.\nOverlooking server maintenance, hardware solutions, and web application administration.',
            'order': 1
        },
        {
            'role': 'Web Developer & Digital Marketing Manager',
            'company': 'Zacx Maxicool Ventures',
            'location': 'Bauchi State, Nigeria',
            'start_date': '2019',
            'end_date': 'Present',
            'description': 'Building customized, responsive websites for local companies and non-profits using Python/Django and CMS (WordPress/Elementor).\nFormulating search engine optimization (SEO) techniques and digital advertisement frameworks on TikTok, Google, and Meta Ads.',
            'order': 2
        },
        {
            'role': 'Industrial Training (IT) Developer',
            'company': 'National Biotechnology Research and Development Agency (NBRDA)',
            'location': 'Abuja, Nigeria',
            'start_date': '2024',
            'end_date': '2024',
            'description': 'Supported bio-data analysis and laboratory data recording management systems.\nDeveloped internal software databases using Python to optimize storage and data tracking of experimental samples.',
            'order': 3
        },
        {
            'role': 'Customer Care Rep Sales and Distribution',
            'company': 'MTN Nigeria',
            'location': 'Bauchi, Nigeria',
            'start_date': '2023',
            'end_date': '2024',
            'description': 'Managed customer complaints, service configurations, and mobile network technical support.\nRecognized for outstanding client retention and attention to detail.',
            'order': 4
        },
        {
            'role': 'Enroller / Operator',
            'company': 'NINC VENDOR',
            'location': 'Bauchi State, Nigeria',
            'start_date': '2021',
            'end_date': 'Present',
            'description': 'Enrolled citizens and managed data entry systems.\nEnsured high accuracy, integrity, and privacy compliance in digital database operations.',
            'order': 5
        },
        {
            'role': 'Volunteer Officer & Data Entry Assistant',
            'company': 'PUSH AFRICA',
            'location': 'Bauchi State, Nigeria',
            'start_date': '2018',
            'end_date': '2020',
            'description': 'Supported community outreach, administrative reporting, and data entry workflows.\nAssisted in organizing field research data and volunteer programs.',
            'order': 6
        },
        {
            'role': 'Laboratory Technician',
            'company': 'New Global Paper Product Nigeria Limited',
            'location': 'Kano, Nigeria',
            'start_date': '2017',
            'end_date': '2017',
            'description': 'Conducted quality assurance trials and sample validation.\nMaintained precise chemical records and laboratory compliance logs.',
            'order': 7
        },
        {
            'role': 'Laboratory Technician (SIWES)',
            'company': 'Our Lady of Apostles (OLA) Clinic Maryam',
            'location': 'Jos, Nigeria',
            'start_date': '2015',
            'end_date': '2015',
            'description': 'Analyzed clinical blood, serum, and urine samples using standardized biochemical protocols.\nCooperated with medical experts for urgent laboratory assessments.',
            'order': 8
        }
    ]
    
    for exp in experiences_data:
        Experience.objects.create(**exp)
        
    # 5. Seed Educations
    print("Seeding education details...")
    educations_data = [
        {
            'degree': 'Medical Biochemistry (B. Tech)',
            'school': 'Abubakar Tafawa Balewa University Bauchi',
            'year': '2019 - 2025',
            'description': 'Acquired an in-depth science and biochemistry education, developing advanced skills in clinical lab methods, research methodologies, statistical modeling, and analytical reasoning.',
            'order': 1
        },
        {
            'degree': 'Science Laboratory Technology (ND)',
            'school': 'Federal Polytechnic Bauchi',
            'year': '2014 - 2016',
            'description': 'Comprehensive training in scientific laboratory disciplines, statistics, scientific protocols, and database recording.',
            'order': 2
        },
        {
            'degree': 'Diploma in Computer',
            'school': 'Njulla Computer Center',
            'year': '2013',
            'description': 'Intensive introduction to core database designs, computer systems, and local networking principles.',
            'order': 3
        },
        {
            'degree': 'Secondary School Certificate (SSCE)',
            'school': 'Ghil Model Secondary School',
            'year': '2007 - 2013',
            'description': 'Core secondary school science curriculum.',
            'order': 4
        },
        {
            'degree': 'First School Leaving Certificate (FSLC)',
            'school': 'Sabon Gurara Primary School',
            'year': '2000 - 2005',
            'description': 'Primary school education.',
            'order': 5
        }
    ]
    
    for edu in educations_data:
        Education.objects.create(**edu)
        
    # 6. Seed Certificates
    print("Seeding certificates obtained...")
    certificates_data = [
        {'title': 'Vibe Coding', 'issuer': 'Coursera', 'year': '2024', 'order': 1},
        {'title': 'Generative AI', 'issuer': 'Microsoft', 'year': '2024', 'order': 2},
        {'title': 'Prompt Engineering', 'issuer': 'Coursera', 'year': '2024', 'order': 3},
        {'title': 'Data Science (3MTT)', 'issuer': '3MTT Program', 'year': '2024', 'order': 4},
        {'title': 'Introduction to Python Program', 'issuer': 'Coursera', 'year': '2023', 'order': 5},
        {'title': 'Digital Marketing Revolution', 'issuer': 'Coursera', 'year': '2023', 'order': 6},
        {'title': 'Social Media Marketing', 'issuer': 'Coursera', 'year': '2023', 'order': 7},
        {'title': 'CSS & HTML with Java Script', 'issuer': 'Coursera', 'year': '2022', 'order': 8},
        {'title': 'WordPress (Elementor) Web Development', 'issuer': 'Elementor Academy', 'year': '2022', 'order': 9},
        {'title': 'TEFL Course', 'issuer': 'TEFL Academy', 'year': '2021', 'order': 10},
    ]
    
    for cert in certificates_data:
        Certificate.objects.create(**cert)
        
    print("Database seeding completed successfully! All portfolios populated!")

if __name__ == '__main__':
    seed_database()
