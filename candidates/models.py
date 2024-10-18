from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(max_length=100, unique=True, validators=[EmailValidator()])
    phone = models.CharField(max_length=20)
    cep = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)   
    state = models.CharField(max_length=100, null=True, blank=True)    
    city = models.CharField(max_length=100, null=True, blank=True)    
    street = models.CharField(max_length=100, null=True, blank=True)    
    number = models.CharField(max_length=100, null=True, blank=True)    
    neighborhood = models.CharField(max_length=100, null=True, blank=True) 

class Contact(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

class WorkExperience(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, related_name='experiences', on_delete=models.CASCADE)
    position = models.CharField(max_length=100)  
    company = models.CharField(max_length=100)   
    start_date = models.DateField()              
    end_date = models.DateField(null=True, blank=True)  
    description = models.TextField() 

class Education(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, related_name='education', on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)   
    course = models.CharField(max_length=100)        
    start_date = models.DateField()                  
    graduation_date = models.DateField(null=True, blank=True)
