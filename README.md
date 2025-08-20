# 🎨 Desafio Loomi Admin
# Um projeto Django Admin para gerenciamento de usuários e tintas, totalmente containerizado com Docker, pronto para rodar localmente e testar via Swagger e Redoc.

# 🚀 Pré-requisitos
# Antes de começar, você precisará ter instalado:
# - Docker: https://docs.docker.com/get-docker/
# - Docker Compose: https://docs.docker.com/compose/install/
# - Iniciar o projeto: https://github.com/igorcenziai/desafio-loomi

# 📥 Clonando o repositório
git clone https://github.com/igorcenziai/desafio-loomi-admin-api.git
cd desafio-loomi-admin

# ⚙️ Rodando o projeto com Docker
# O projeto já vem com Dockerfile e docker-compose configurados. Para subir o ambiente:
docker-compose up -d --build

# Isso fará:
# 1. Criar os containers de `app` e `migrate`.
# 2. Rodar as migrations automaticamente.
# 3. Mapear a porta 8000 para acessar o Django no navegador.

# 🔧 Comandos úteis
# Verificar logs do Django
docker logs -f desafio-loomi-admin_app_1

# Derrubar o ambiente
docker-compose down

# Rodar migrations manualmente (se necessário)
docker-compose run --rm migrate

# Acessar o shell do Django
docker-compose run --rm app python manage.py shell

# 🌐 Acessando a aplicação
# Swagger UI: http://localhost:8000/api/schema/swagger
# Redoc: http://localhost:8000/api/schema/redoc
