from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectList, ProjectList, CollaborationListAPIView, CollaborationDetailAPIView, ResearchListAPIView, ResearchDetailAPIView, ProjectDetailAPIView, ContactAPIView

# Define URL patterns for the project app
urlpatterns = [
    # Project URLs
    path('projects/', ProjectList.as_view(), name='project-list'),  # List all projects or create a new project  # Get, update, or delete a specific project

    # Collaboration URLs
    path('collaborations/', CollaborationListAPIView.as_view(), name='collaboration-list'),  # List all collaborations or create a new one
    path('collaboration/<int:pk>/', CollaborationDetailAPIView.as_view(), name='collaboration-detail'),  # Get, update, or delete a specific collaboration

    # Research URLs
    path('research/', ResearchListAPIView.as_view(), name='research-list'),  # List all research publications or create a new one
    path('research/<int:pk>/', ResearchDetailAPIView.as_view(), name='research-detail'),  # Get, update, or delete a specific research publication
    path('project/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),  # Get, update, or delete a specific project

    # Contact URL
    path('contact/', ContactAPIView.as_view(), name='contact'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
