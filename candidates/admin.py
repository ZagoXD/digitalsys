from django.contrib import admin
from .models import PersonalInfo, Contact, WorkExperience, Education

admin.site.register(PersonalInfo)
admin.site.register(Contact)
admin.site.register(WorkExperience)
admin.site.register(Education)
