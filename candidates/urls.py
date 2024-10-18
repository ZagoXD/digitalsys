from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalInfoViewSet, ContactViewSet, WorkExperienceViewSet, EducationViewSet
from . import views

router = DefaultRouter()

router.register(r'personal-info', PersonalInfoViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'work-experiences', WorkExperienceViewSet)
router.register(r'education', EducationViewSet)


urlpatterns = [
    path('submit/', views.submit_resume, name='submit_resume'),
    path('', include(router.urls)), 
]
