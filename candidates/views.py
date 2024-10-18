from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import PersonalInfo, Contact, WorkExperience, Education
from .serializers import PersonalInfoSerializer, ContactSerializer, WorkExperienceSerializer, EducationSerializer

def home(request):
    return render(request, 'candidates/home.html')


class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer

class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer

# verificar
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

def submit_resume(request):
    if request.method == 'POST':
        print(request.POST)
        # Captura os dados pessoais
        name = request.POST['name']
        birth_date = request.POST['birth_date']
        email = request.POST['email']
        phone = request.POST['phone']
        
        # Captura os dados do endereço
        cep = request.POST['cep']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        street = request.POST['street']
        number = request.POST['number']
        neighborhood = request.POST['neighborhood']
        
        # Captura os dados da experiência profissional
        position = request.POST['position']
        company = request.POST['company']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        description = request.POST['description']
        
        # Captura os dados da formação acadêmica
        institution = request.POST['institution']
        course = request.POST['course']
        start_date_education = request.POST['start_date_education']
        graduation_date = request.POST['graduation_date']

        # Salva os dados no banco de dados
        personal_info = PersonalInfo.objects.create(
            name=name,
            birth_date=birth_date,
            email=email,
            phone=phone,
            cep=cep,
            country=country,
            state=state,
            city=city,
            street=street,
            number=number,
            neighborhood=neighborhood
        )

        WorkExperience.objects.create(
            personal_info=personal_info,
            position=position,
            company=company,
            start_date=start_date,
            end_date=end_date,
            description=description
        )

        Education.objects.create(
            personal_info=personal_info,
            institution=institution,
            course=course,
            start_date=start_date_education,
            graduation_date=graduation_date
        )

        return HttpResponse('Currículo enviado com sucesso!')
    
    return render(request, 'candidates/form.html')