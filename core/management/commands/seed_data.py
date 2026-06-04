from django.core.management.base import BaseCommand
from core.models import Skill, Project

class Command(BaseCommand):
    help = 'Seeds the database with static resume data (Skills and Projects)'

    def handle(self, *args, **kwargs):
        self.stdout.write('Checking and seeding database...')

        # --- SEED SKILLS ---
        skills_data = [
            {'skill_name': 'Python, Django & DRF', 'skill_level': 95},
            {'skill_name': 'JavaScript, React & jQuery', 'skill_level': 85},
            {'skill_name': 'PostgreSQL & MySQL', 'skill_level': 90},
            {'skill_name': 'AWS EC2, Linux & DevOps', 'skill_level': 85},
            {'skill_name': 'Nginx, Gunicorn & Celery', 'skill_level': 80},
            {'skill_name': 'HTML5, CSS3 & Bootstrap', 'skill_level': 90},
            {'skill_name': 'Git, WebSockets & REST APIs', 'skill_level': 90},
        ]

        for s in skills_data:
            Skill.objects.get_or_create(
                skill_name=s['skill_name'],
                defaults={'skill_level': s['skill_level']}
            )

        # --- SEED PROJECTS ---
        projects_data = [
            {
                'title': 'Coffercard - Digital Gift Card Platform',
                'description': 'Built React-Django backend features and deployed on AWS EC2 with Nginx and Gunicorn for live production usage. Implemented vendor modules, coupon logic, transaction handling, and admin tools.',
                'technology_used': 'React, Django, AWS EC2, Nginx, Gunicorn, PostgreSQL',
                'live_link': '#',
                'github_link': '',
            },
            {
                'title': 'Card Betting Game with MLM Structure',
                'description': 'Led full project lifecycle from requirement analysis to deployment. Integrated a custom MLM backend increasing user engagement by 30%. Deployed on AWS EC2.',
                'technology_used': 'Django, AWS EC2, Custom Backend',
                'live_link': '',
                'github_link': '',
            },
            {
                'title': 'CFO Accounting Software',
                'description': 'Developed backend modules with Fatoora integration, improving financial reporting accuracy by 20%. Streamlined reporting for Saudi market compliance.',
                'technology_used': 'Python, Django, Frontend Stack',
                'live_link': '',
                'github_link': '',
            },
            {
                'title': 'Mubasher One Workshop Management System',
                'description': 'Built accounting, billing, and inventory modules, reducing manual processing time by 30%. Managed backend, frontend, and deployment operations gaining full-stack and DevOps exposure.',
                'technology_used': 'Django, HTML, CSS, JS',
                'live_link': '',
                'github_link': '',
            },
            {
                'title': 'Rafa Medicals Hospital Management Website',
                'description': 'Developed a bilingual hospital website with an online booking system and admin dashboard. Hosted on DigitalOcean using Nginx.',
                'technology_used': 'Django, DigitalOcean, Nginx',
                'live_link': 'http://rafamedicals.com/en',
                'github_link': '',
            },
            {
                'title': 'Alfa-Al-Khaleej ERP System',
                'description': 'Developed ERP modules for daily business operations, increasing operational efficiency by 25%. Automated workflows using Django, HTML, CSS, and JS.',
                'technology_used': 'Django, HTML, CSS, JS',
                'live_link': '',
                'github_link': '',
            }
        ]

        for p in projects_data:
            Project.objects.get_or_create(
                title=p['title'],
                defaults={
                    'description': p['description'],
                    'technology_used': p['technology_used'],
                    'live_link': p['live_link'],
                    'github_link': p['github_link']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))