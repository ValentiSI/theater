python manage.py runserver - запустить сервер

python manage.py startapp name - создать подприложение name
Нужно будет добавить приложение в INSTALLED_APPS

python manage.py makemigrations app_name - если вы изменили модели, этой командой создается миграция - обновление базы данных
python manage.py migrate - обновление/создание базы данных

pip freeze > requirements.txt - создаст файл с библиотеками которые используются в проекте, если находишься в среде (venv)
pip install -r.\requirements.txt - загрузит нужные библиотеки

python manage.py createsuperuser --username admin --email admin@domain.com - добавить админ пользователя

python manage.py shell - копируем код из generate_test_data.py, вставляем, далее exit(), далее база заполняется

git config user.name "Your Name" # указать имя, которым будут подписаны коммиты
git config user.email "e@w.com"  # указать электропочту, которая будет в описании коммитера
