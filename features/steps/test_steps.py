from behave import given, when, then
from django.test import Client
from django.urls import reverse

@given('que eu sou um usuário não autenticado')
def step_impl(context):
    context.client = Client()

@when('eu preencho o formulário de currículo corretamente')
def step_impl(context):
    context.response = context.client.post(reverse('submit_resume'), {
        'name': 'Gustavo Zago',
        'birth_date': '2001-01-01',
        'email': 'gu@ex.com',
        'phone': '(16) 99999-9999',
        'cep': '12345678',
        'country': 'Brasil',
        'state': 'SP',
        'city': 'São Paulo',
        'street': 'Rua Teste',
        'number': '123',
        'neighborhood': 'Bairro Teste',
        'position_1': 'Dev',
        'company_1': 'Empresa X',
        'start_date_1': '2020-01-01',
        'end_date_1': '2021-01-01',
        'description_1': 'Dev de software',
        'institution_1': 'Universidade Teste',
        'course_1': 'Engenharia da Computação',
        'start_date_education_1': '2015-01-01',
        'graduation_date_1': '2019-01-01'
    })

@when('eu clico no botão "Submeter Currículo"')
def step_impl(context):
    pass  

@then('o sistema deve mostrar uma mensagem de sucesso "Currículo enviado com sucesso!"')
def step_impl(context):
    assert 'Currículo enviado com sucesso!' in context.response.content.decode()
