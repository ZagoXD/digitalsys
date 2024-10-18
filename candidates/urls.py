from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalInfoViewSet
from . import views


router = DefaultRouter()
router.register(r'personal-info', PersonalInfoViewSet)

urlpatterns = [
    path('submit/', views.submit_resume, name='submit_resume'),
    path('', include(router.urls)), 
]
