# projects/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    long_description = models.TextField(blank=True, null=True)
    image_url = models.ImageField(upload_to='projects/')
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    technologies = models.JSONField()  # Stores a list of technologies as JSON

    def __str__(self):
        return self.title



class Collaboration(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    short_description = models.TextField(blank=True, null=True)
    image_url = models.ImageField(upload_to='collaboration/', blank=True, null=True)


    def __str__(self):
        return self.title
    


class Research(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    journal = models.CharField(max_length=255, blank=True, null=True)
    publication_date = models.DateField()
    short_description = models.TextField(blank=True, null=True)
    image_url = models.ImageField(upload_to='research/', blank=True, null=True)
    url_field= models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class  collaboration_images(models.Model):
    collaboration = models.ForeignKey(Collaboration, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='collaboration_images/')

    def __str__(self):
        return f"Image for {self.collaboration.title}"
class research_images(models.Model):
    research = models.ForeignKey(Research, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='research_images/')

    def __str__(self):
        return f"Image for {self.research.title}" 

class project_images(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.title}"