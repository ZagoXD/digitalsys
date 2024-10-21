from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import PersonalInfo, Contact, WorkExperience, Education
from .serializers import PersonalInfoSerializer, ContactSerializer, WorkExperienceSerializer, EducationSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, 'candidates/home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


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
        # print(request.POST)
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

        # Captura as experiências profissionais
        experienceCount = 1
        while f'position_{experienceCount}' in request.POST:
            position = request.POST[f'position_{experienceCount}']
            company = request.POST[f'company_{experienceCount}']
            start_date = request.POST[f'start_date_{experienceCount}']
            end_date = request.POST.get(f'end_date_{experienceCount}', None)
            description = request.POST[f'description_{experienceCount}']

            WorkExperience.objects.create(
                personal_info=personal_info,
                position=position,
                company=company,
                start_date=start_date,
                end_date=end_date,
                description=description
            )
            experienceCount += 1

        # Captura e salva as formações acadêmicas
        education_count = 1
        while f'institution_{education_count}' in request.POST:
            institution = request.POST[f'institution_{education_count}']
            course = request.POST[f'course_{education_count}']
            start_date_education = request.POST[f'start_date_education_{education_count}']
            graduation_date = request.POST.get(f'graduation_date_{education_count}', None)

            Education.objects.create(
                personal_info=personal_info,
                institution=institution,
                course=course,
                start_date=start_date_education,
                graduation_date=graduation_date
            )
            education_count += 1

        return HttpResponse('Currículo enviado com sucesso!')
    
    return render(request, 'candidates/form.html')