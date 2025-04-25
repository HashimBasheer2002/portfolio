from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    date_created = models.DateField()

    def __str__(self):
        return self.title

class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)  # e.g., Internship, Full Stack Developer
    description = models.TextField()
    logo = models.ImageField(upload_to='experience_logos/', blank=True, null=True)

    def __str__(self):
        return self.company_name