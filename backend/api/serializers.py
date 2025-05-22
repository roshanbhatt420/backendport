# projects/serializers.py
from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description','long_description', 'image_url', 'github_url', 'live_url', 'technologies']



class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = ['id', 'title', 'organization', 'description', 'date', 'image_url', 'short_description']



class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ['id', 'title', 'abstract', 'journal', 'publication_date', 'image_url', 'url_field', 'short_description']

class CollaborationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = collaboration_images
        fields = ['id', 'collaboration_id','image']

        
class ResearchImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = research_images
        fields = ['id', 'research_id', 'image']

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = project_images
        fields = ['id', 'project_id', 'image']
