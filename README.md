
# Sistema de Recrutamento da Pegho

## Autor
Gustavo

## Descrição
Este é um sistema de recrutamento desenvolvido para a empresa **Pegho**. Ele permite que candidatos submetam seus currículos, incluindo dados pessoais, experiência profissional e formação acadêmica. O sistema também possui um painel administrativo onde é possível gerenciar as informações submetidas pelos candidatos.

O projeto utiliza **Django** como framework backend e inclui uma interface web para o frontend. Além disso, há funcionalidades extras como validações de telefone, email e CEP, além de uso dinâmico de JavaScript para adicionar/remover múltiplas experiências e formações acadêmicas.

## Requisitos

- **Python 3.x**
- **Django 3.x ou 4.x**
- **Django Rest Framework**
- **Bootstrap 4 ou superior**
- **ViaCEP API** (para busca automática de endereços via CEP)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/usuario/repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd pegho_recruitment
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate      # Para Windows
   ```

4. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

5. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

6. Crie um superusuário para acessar o painel administrativo:
   ```bash
   python manage.py createsuperuser
   ```

7. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## Como Rodar

1. Abra um navegador e acesse o endereço:
   ```
   http://127.0.0.1:8000
   ```

2. **Submeter currículo**: O candidato pode submeter suas informações pessoais, experiência profissional e formação acadêmica no formulário acessível em `/candidates/submit/`.

3. **Acessar o painel de administração**: O administrador pode acessar o painel em `/admin`, onde é possível visualizar e gerenciar os currículos submetidos.

## Funcionalidades

- **Validação de Dados**: O sistema valida informações como telefone, email e CEP.
- **ViaCEP API**: Busca automática de endereço ao digitar o CEP.
- **Adicionar/Remover Experiências**: O candidato pode adicionar ou remover múltiplas experiências profissionais de forma dinâmica no formulário.
- **Adicionar/Remover Formações**: O candidato pode adicionar ou remover múltiplas formações acadêmicas no formulário.

## Tecnologias Utilizadas

- **Django**: Framework backend para construir o sistema de recrutamento.
- **Django Rest Framework**: Para APIs e interações CRUD.
- **Bootstrap**: Framework CSS para estilização básica.
- **JavaScript**: Utilizado para funcionalidades dinâmicas no frontend.
- **ViaCEP API**: Para buscar endereços automaticamente via CEP.

## Estrutura de Pastas

```
pegho_recruitment/
│
├── candidates/               # App principal
│   ├── migrations/           # Arquivos de migração do banco de dados
│   ├── static/               # Arquivos estáticos (CSS, JS)
│   ├── templates/            # Templates HTML
│   ├── models.py             # Modelos do banco de dados
│   ├── views.py              # Lógica das views
│   ├── urls.py               # Rotas do app
│   └── forms.py              # (Opcional) Arquivo de formulários
│
├── pegho_recruitment/        # Configurações do projeto Django
│   ├── settings.py           # Configurações gerais do projeto
│   ├── urls.py               # Rotas principais do projeto
│   └── wsgi.py               # Configurações WSGI para deploy
│
├── static/                   # Arquivos estáticos (global)
│   └── script/               # Arquivos JavaScript
│       └── script.js
├── manage.py                 # Comando de gerenciamento do Django
├── README.md                 # Documentação do projeto
└── requirements.txt          # Dependências do projeto
```

## Licença
Este projeto está sob a licença MIT. Para mais detalhes, consulte o arquivo LICENSE.
