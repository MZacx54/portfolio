from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('web_dev', 'Web Design & Full-Stack Development'),
        ('digital_mkt', 'Digital Marketing & SEO'),
        ('design', 'Graphic Design & CMS'),
        ('soft_skills', 'Soft & Transferable Skills'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web_dev')
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=85, help_text="Skill percentage (e.g. 90 for 90%)")
    icon_class = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class e.g. 'fab fa-python'")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated tech, e.g. 'Python, Django, SQLite'")
    github_url = models.CharField(max_length=250, help_text="GitHub repository link or username/repo")
    live_url = models.URLField(blank=True, null=True, help_text="Live website URL")
    icon_class = models.CharField(max_length=50, default='fas fa-code', help_text="FontAwesome icon for card header")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    @property
    def tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]


class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=150, blank=True)
    start_date = models.CharField(max_length=50, help_text="e.g. '2025' or '2019'")
    end_date = models.CharField(max_length=50, default='Present', help_text="e.g. 'Present' or '2024'")
    description = models.TextField(help_text="Provide details, use newlines for bullet points.")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"

    @property
    def bullet_points(self):
        return [point.strip() for point in self.description.split('\n') if point.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=150)
    school = models.CharField(max_length=150)
    year = models.CharField(max_length=50, help_text="e.g. '2019 - 2025'")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-year']

    def __str__(self):
        return f"{self.degree} - {self.school}"


class Certificate(models.Model):
    title = models.CharField(max_length=150)
    issuer = models.CharField(max_length=150)
    year = models.CharField(max_length=50, blank=True, help_text="e.g. '2024'")
    url = models.URLField(blank=True, null=True, help_text="Verification link if any")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return f"{self.title} - {self.issuer}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
