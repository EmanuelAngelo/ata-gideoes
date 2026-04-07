# ATA Gideões

Sistema para gestão de atas, reuniões, membros e presenças (API em Django/DRF). O frontend (Vue + Vuetify) está em construção.

## Stack

**Backend**
- Django
- Django REST Framework (DRF)
- SimpleJWT (JWT)
- django-filter
- django-cors-headers
- python-decouple (config via `.env`)

**Frontend (WIP)**
- Vue 3 + Vite
- Vuetify

## Estrutura do repositório

- `core/`: projeto Django (settings/urls/asgi/wsgi)
- `ata/`: app Django com os models e ViewSets (DRF)
- `frontend/`: projeto do frontend (ainda em evolução)

## Backend (API)

### 1) Pré-requisitos

- Python 3.x

### 2) Configuração do ambiente

Crie um arquivo `.env` na raiz (use o `.env.example` como base):

```dotenv
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=true
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3) Instalação e execução

```bash
# na raiz do repo
python -m venv .venv
source .venv/Scripts/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Admin: `http://127.0.0.1:8000/admin/`

## Rotas da API (mapeadas por etapas)

Base da API: tudo fica sob `/api/`.

### Etapa 1 — Autenticação (JWT)

Essas rotas são fornecidas pelo SimpleJWT:

- `POST /api/auth/token/` — obtém `access` e `refresh`
- `POST /api/auth/token/refresh/` — renova o `access` usando o `refresh`
- `POST /api/auth/token/verify/` — verifica se um token é válido

Exemplo (obter tokens):

```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"SEU_USUARIO","password":"SUA_SENHA"}'
```

### Etapa 2 — Recursos (CRUD via DRF ViewSets)

Rotas registradas no `DefaultRouter` do DRF (`ata/urls.py`). Em geral, cada recurso expõe:
- `GET /api/<recurso>/` (listar)
- `POST /api/<recurso>/` (criar)
- `GET /api/<recurso>/{id}/` (detalhar)
- `PUT/PATCH /api/<recurso>/{id}/` (atualizar)
- `DELETE /api/<recurso>/{id}/` (remover)

Recursos disponíveis:
- ` /api/members/` — membros
- ` /api/meetings/` — reuniões
- ` /api/minutes/` — atas
- ` /api/attendances/` — presenças
- ` /api/partner-churches/` — igrejas parceiras
- ` /api/church-schedules/` — agenda (programação)

### Etapa 3 — Admin (Django)

- `GET /admin/` — painel administrativo do Django

## Frontend (em construção)

O frontend fica em `frontend/` e ainda está sendo criado/evoluído.

Quando chegar a hora de documentar, a ideia é:
- consumir a API em `/api/*` (com JWT)
- implementar telas para os recursos acima (listas e formulários)
- usar Vue + Vuetify para UI

## Licença

Defina a licença do projeto (se aplicável).
