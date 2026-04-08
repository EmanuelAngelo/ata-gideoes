# ATA Gideões

Sistema para gestão de atas, reuniões, membros, presenças, igrejas parceiras e agendamentos às igrejas. O projeto possui backend em Django/DRF e frontend em Vue 3.

## Stack

**Backend**
- Django
- Django REST Framework (DRF)
- SimpleJWT (JWT)
- django-filter
- django-cors-headers
- python-decouple (config via `.env`)

**Frontend**
- Vue 3
- Vite
- TypeScript
- Pinia
- Vue Router
- Tailwind CSS v4
- Vuetify (instalado no projeto, mas a interface principal atual usa Tailwind como base visual)

## Estrutura do repositório

- `core/`: projeto Django (settings/urls/asgi/wsgi)
- `ata/`: app Django com os models e ViewSets (DRF)
- `frontend/`: projeto do frontend SPA

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

## Frontend

O frontend fica em `frontend/` e já possui autenticação, dashboard com dados reais do backend e módulos CRUD iniciais para todos os recursos principais da API.

### 1) Stack e abordagem

- `Vue 3` com `script setup`
- `TypeScript`
- `Pinia` para estado global de autenticação
- `Vue Router` para navegação protegida
- `Tailwind CSS v4` como base principal da interface
- `Vuetify` permanece instalado e configurado no projeto, mas a UI implementada até aqui foi padronizada em Tailwind para evitar inconsistências visuais

### 2) Como rodar o frontend

Entre na pasta `frontend/` e execute:

```bash
cd frontend
npm install
npm run dev
```

O Vite sobe a aplicação em ambiente local. Pela configuração atual do projeto, o frontend normalmente roda em:

- `http://127.0.0.1:3000`
- ou `http://localhost:3000`

Para build de produção:

```bash
cd frontend
npm run build
```

Para validação de tipos:

```bash
cd frontend
npm run type-check
```

### 3) Configuração de API no frontend

O frontend usa uma camada própria para chamadas HTTP em:

- `frontend/src/api/api.ts`

Por padrão, a API base é:

- `http://127.0.0.1:8000`

Ela pode ser sobrescrita com a variável:

- `VITE_API_BASE_URL`

Exemplo:

```dotenv
VITE_API_BASE_URL=http://127.0.0.1:8000
```

### 4) Autenticação no frontend

O login do frontend já está integrado ao backend Django usando JWT.

Arquivos principais:

- `frontend/src/api/auth.ts`
- `frontend/src/stores/auth.ts`
- `frontend/src/pages/LoginPage.vue`
- `frontend/src/components/LoginForm.vue`

Fluxo atual:

1. Usuário informa login e senha na tela de login
2. Frontend chama `POST /api/auth/token/`
3. Backend retorna `access` e `refresh`
4. Tokens são persistidos em `localStorage`
5. Rotas protegidas só abrem quando `isAuthenticated === true`

### 5) Estrutura principal do frontend

Arquivos e pastas mais importantes:

- `frontend/src/api/`
  - camada de acesso à API
  - autenticação, recursos e tratamento de erro
- `frontend/src/stores/`
  - store de autenticação com Pinia
- `frontend/src/router/index.ts`
  - rotas públicas e protegidas
- `frontend/src/config/navigation.ts`
  - definição central do menu lateral
- `frontend/src/config/resources.ts`
  - configuração dos módulos CRUD por recurso
- `frontend/src/components/layout/DashboardShell.vue`
  - layout autenticado com menu lateral
- `frontend/src/components/resources/ResourceCrudPage.vue`
  - componente genérico de CRUD
- `frontend/src/pages/`
  - telas do dashboard, login e módulos

### 6) Rotas do frontend

Rotas já implementadas:

- `/login` → tela de login
- `/dashboard` → painel principal com dados reais do backend
- `/membros` → módulo de membros
- `/reunioes` → módulo de reuniões
- `/atas` → módulo de atas
- `/publico` → módulo de presenças
- `/igrejas-parceiras` → módulo de igrejas parceiras
- `/horarios-igreja` → módulo de agendamento às igrejas

Observação: o caminho `/horarios-igreja` foi mantido como rota, mas o rótulo visual do menu já está regularizado como **Agendamento às Igrejas**.

### 7) Layout e navegação

Após autenticação, a aplicação usa um shell lateral em:

- `frontend/src/components/layout/DashboardShell.vue`

Esse layout oferece:

- menu lateral responsivo
- navegação por módulos reais do backend
- conteúdo principal empurrado lateralmente no desktop
- comportamento mobile com menu recolhível

Itens atuais do menu:

- `Dashboard`
- `Presenças`
- `Agendamento às Igrejas`
- `Reuniões`
- `Membros`
- `Atas`
- `Igrejas Parceiras`

### 8) Dashboard

O dashboard já consome dados reais do backend.

Hoje ele mostra:

- total de membros
- total de reuniões
- total de atas
- total de presenças
- total de igrejas parceiras
- total de agendamentos às igrejas
- prévia de reuniões recentes
- prévia de atas recentes
- prévia de agendamentos às igrejas

Os dados vêm dos endpoints reais da API e respeitam a paginação do DRF.

### 9) Módulos CRUD já implementados

Todos os módulos abaixo já têm uma base funcional de CRUD:

- `Membros`
- `Reuniões`
- `Atas`
- `Presenças`
- `Igrejas Parceiras`
- `Agendamento às Igrejas`

O componente base de CRUD fica em:

- `frontend/src/components/resources/ResourceCrudPage.vue`

Recursos atuais do CRUD:

- listagem dos registros
- busca textual
- formulário modal para criação e edição
- exclusão de registros
- exibição expansível dos dados cadastrados
- mensagens de erro e sucesso

### 10) Regras de UX já aplicadas

Alguns módulos já receberam inteligência de formulário para evitar campos técnicos expostos ao usuário:

**Presenças**
- não exige digitar `id` do membro ou da reunião manualmente
- seleciona `Membro` e `Reunião` já cadastrados
- preenche automaticamente nome, classificação e função do membro

**Agendamento às Igrejas**
- permite escolher uma igreja parceira já cadastrada
- também permite digitar uma igreja manualmente se ela ainda não existir no cadastro
- ao escolher uma igreja existente, preenche automaticamente dados como pastor, telefone, endereço, bairro e cidade

### 11) Padrões de frontend adotados

O frontend foi organizado para seguir uma estrutura mais sustentável e limpa:

- separação entre camada de API, estado, páginas e componentes
- rotas protegidas por autenticação
- configurações centralizadas de navegação e recursos
- CRUD genérico reutilizável por módulo
- formulários com foco em reduzir entrada manual de IDs técnicos

### 12) Observações importantes

- o backend usa paginação do DRF, e o frontend já trata respostas com `count`, `next`, `previous` e `results`
- o projeto ainda pode evoluir com paginação visual, filtros avançados, máscaras e formulários mais específicos por domínio
- o Vuetify segue instalado no projeto, mas a interface principal atual foi padronizada em Tailwind

## Licença

Este projeto utiliza a licença MIT. Consulte o arquivo `LICENSE`.
