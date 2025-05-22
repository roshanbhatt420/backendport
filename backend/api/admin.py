# projects/admin.py
from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Collaboration)
admin.site.register(Research)
admin.site.register(collaboration_images)
admin.site.register(research_images)
admin.site.register(project_images)
# Register your models here.
