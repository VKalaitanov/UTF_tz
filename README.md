<h3>Инструкция для запуска проекта:</h3>
 - git clone https://github.com/VKalaitanov/UTF_tz.git
 - cd UTF_tz
 - pip install -r requirementx.txt
 - В корневую папку проекта добавляете файл ".env"
 
<h3>В файле ".env": </h3>
SECRET_KEY='<секретный ключ>'
DEBUG=1
ALLOWED_HOSTS='<ваши хосты >'

<h3>Создаем миграции:</h3>
 - python manage.py makemigrations
 - python manage.py migrate

<h3>Запуск проекта</h3>
 - python3 manage.py runserver


