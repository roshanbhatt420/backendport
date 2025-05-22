from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Collaboration, Research, collaboration_images,research_images,project_images
from .serializers import ProjectSerializer, CollaborationSerializer, ResearchSerializer
from django.core.mail import send_mail
from django.conf import settings


# Collaboration List View
class CollaborationListAPIView(APIView):
    """
    API View for listing and creating Collaborations.
    """
    def get(self, request, *args, **kwargs):
        collaborations = Collaboration.objects.all()
        serializer = CollaborationSerializer(collaborations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CollaborationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Project List View
class ProjectList(APIView):
    """
    API View for listing and creating Projects.
    """
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Research List View
class ResearchListAPIView(APIView):
    """
    API View for listing and creating Research Publications.
    """
    def get(self, request, *args, **kwargs):
        research_papers = Research.objects.all().order_by('-publication_date')  # Sort by latest first
        serializer = ResearchSerializer(research_papers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ResearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# collaboration images for fetching images accordng to collab id and which is used in fk in collaboration_image model
class CollaborationDetailAPIView(APIView):
    """
    API View for retrieving all images related to a specific Collaboration.
    """
    def get(self, request, pk, *args, **kwargs):
        images = collaboration_images.objects.filter(collaboration_id=pk)
        if images.exists():
            from .serializers import CollaborationImageSerializer  # Adjust import as needed
            serializer = CollaborationImageSerializer(images, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No images found for this collaboration."}, status=status.HTTP_404_NOT_FOUND)



#research images for fetching images accordng to research id and which is used in fk in research_image model
class ResearchDetailAPIView(APIView):
    """
    API View for retrieving all images related to a specific Research Publication.
    """
    def get(self, request, pk, *args, **kwargs):
        images = research_images.objects.filter(research_id=pk)
        if images.exists():
            # If you have a serializer for research_images, use it here.
            # Otherwise, you can serialize manually.
            from .serializers import ResearchImageSerializer  # Adjust import as needed
            serializer = ResearchImageSerializer(images, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No images found for this research."}, status=status.HTTP_404_NOT_FOUND)


class ProjectDetailAPIView(APIView):    
    """
    API View for retrieving all images related to a specific Project.
    """
    def get(self, request, pk, *args, **kwargs):
        images = project_images.objects.filter(project_id=pk)
        if images.exists():
            # If you have a serializer for project_images, use it here.
            # Otherwise, you can serialize manually.
            from .serializers import ProjectImageSerializer  # Adjust import as needed
            serializer = ProjectImageSerializer(images, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No images found for this project."}, status=status.HTTP_404_NOT_FOUND)


class ContactAPIView(APIView):
    """
    API View for handling contact form submissions and sending email.
    """
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')
        if not (name and email and subject and message):
            return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            send_mail(
                subject=f"Portfolio Contact: {subject}",
                message=f"From: {name} <{email}>\n\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["roshanbhatta605@gmail.com"],
                fail_silently=False,
            )
            return Response({'success': 'Message sent successfully!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)