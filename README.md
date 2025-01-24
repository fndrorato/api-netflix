
# Django API - Clone do Netflix

Este projeto é uma API desenvolvida em Django com o objetivo de simular uma plataforma similar à Netflix. A API permite gerenciar dados como atores, gêneros, filmes e reviews, além de oferecer funcionalidade de autenticação de usuários utilizando o pacote **Simple JWT**.

---

## Funcionalidades

### **1. CRUDs Disponíveis**
- **Atores (Actors):** Gerenciamento de atores com informações detalhadas.
- **Gêneros (Genres):** Gerenciamento de gêneros de filmes/séries.
- **Filmes (Movies):** Gerenciamento de filmes com informações sobre atores e gêneros associados.
- **Reviews:** Criação, leitura, atualização e exclusão de reviews associados aos filmes.

### **2. Autenticação**
- Sistema de login baseado em **JWT (JSON Web Token)** usando o pacote **Simple JWT**.
- Suporte para obtenção de tokens de acesso e renovação de tokens.

---

## Tecnologias Utilizadas
- **Linguagem:** Python 3.8+
- **Framework:** Django 4.0+
- **Banco de Dados:** PostgreSQL
- **Autenticação:** Simple JWT
- **Serialização:** Django REST Framework (DRF)

---

## Requisitos de Instalação

Antes de começar, certifique-se de que você tenha instalado:
- Python 3.8 ou superior
- DB.SQLITE3
- Git
- Virtualenv (opcional, mas recomendado)

---

## Configuração do Projeto

### **1. Clonar o Repositório**
```bash
git clone https://github.com/fndrorato/api-netflix.git
cd api-netflix
```
### **2. Criar e Ativar um Ambiente Virtual**
```bash
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

### **3. Instalar Dependências**
```bash
pip install -r requirements.txt
```

### **4. Configurar o banco de dados**
```bash
Edite o arquivo settings.py com as credenciais do seu banco de dados PostgreSQL:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netflix_clone',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### **5. Aplicar as Migrações**
```bash
python manage.py migrate

```

### **6. Criar um Superusuário**
```bash
python manage.py createsuperuser
```

### **7. Executar o servidor**
```bash
python manage.py runserver
```
A API estará disponível em: http://127.0.0.1:8000

## Endpoints da API

### 1. Autenticação
- POST /api/v1/authentication/token/: Obter tokens de acesso e atualização.
- POST /api/v1/authentication/token/refresh/: Renovar o token de acesso.
- POST /api/v1/authentication/token/verify/: Verificar o token de acesso.
### 2. Atores
- GET /api/v1/actors/: Listar todos os atores.
- POST /api/v1/actors/: Criar um novo ator.
- GET /api/v1/actors/{id}/: Detalhes de um ator.
- PUT /api/v1/actors/{id}/: Atualizar um ator.
- DELETE /api/v1/actors/{id}/: Deletar um ator.
### 3. Gêneros
- GET /api/v1/genres/: Listar todos os gêneros.
- POST /api/v1/genres/: Criar um novo gênero.
- GET /api/v1/genres/{id}/: Detalhes de um gênero.
- PUT /api/v1/genres/{id}/: Atualizar um gênero.
- DELETE /api/v1/genres/{id}/: Deletar um gênero.
### 4. Filmes
- GET /api/v1/movies/: Listar todos os filmes.
- POST /api/v1/movies/: Criar um novo filme.
- GET /api/v1/movies/{id}/: Detalhes de um filme.
- PUT /api/v1/movies/{id}/: Atualizar um filme.
- DELETE /api/v1/movies/{id}/: Deletar um filme.
### 5. Reviews
- GET /api/v1/reviews/: Listar todas as reviews.
- POST /api/v1/reviews/: Criar uma nova review.
- GET /api/v1/reviews/{id}/: Detalhes de uma review.
- PUT /api/v1/reviews/{id}/: Atualizar uma review.
- DELETE /api/v1/reviews/{id}/: Deletar uma review.



