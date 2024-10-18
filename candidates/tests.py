from django.test import TestCase
from .models import PersonalInfo
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import PersonalInfo


class PersonalInfoModelTest(TestCase):

     def setUp(self):
         self.personal_info = PersonalInfo.objects.create(
             name="Gustavo Zago",
             birth_date="2001-05-27",
             email="gugu_zago@hotmail.com",
             phone="(16) 99233-0309",
             cep="14300202",
             country="Brasil",
             state="SP",
             city="Batatais",
             street="Rua Jose Augusto Fernandes",
             number="72",
             neighborhood="Castelo"
         )
    
     def test_get_personal_info(self):
         url = reverse('personalinfo-list')  
         response = self.client.get(url)
         self.assertEqual(response.status_code, status.HTTP_200_OK)
         self.assertEqual(len(response.data), 1)
         self.assertEqual(response.data[0]['email'], self.personal_info.email)

     def test_personal_info_creation(self):
         self.assertEqual(self.personal_info.name, "Gustavo Zago")
         self.assertEqual(self.personal_info.email, "gugu_zago@hotmail.com")
         self.assertEqual(self.personal_info.phone, "(16) 99233-0309")
         self.assertEqual(self.personal_info.city, "Batatais")

     def test_email_max_length(self):
         max_length = self.personal_info._meta.get_field('email').max_length
         self.assertEqual(max_length, 100)

class PersonalInfoAPITest(APITestCase):

    def setUp(self):
        self.personal_info = PersonalInfo.objects.create(
            name="Gustavo Zago",
             birth_date="2001-05-27",
             email="gugu_zago@hotmail.com",
             phone="(16) 99233-0309",
        )

    def test_get_personal_info(self):
        url = reverse('personalinfo-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['email'], self.personal_info.email)