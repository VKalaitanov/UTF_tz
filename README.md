<h3>Инструкция для запуска проекта:</h3>
 <p>- git clone https://github.com/VKalaitanov/UTF_tz.git</p>
 <p>- cd UTF_tz</p>
 <p>- pip install -r requirementx.txt</p>
 <p>- В корневую папку проекта добавляете файл ".env"</p>
 
<h3>В файле ".env": </h3>
<p>SECRET_KEY='<секретный ключ>'</p>
<p>DEBUG=1</p>
<p>ALLOWED_HOSTS='<ваши хосты >'</p>

<h3>Создаем миграции:</h3>
 <p>- python manage.py makemigrations</p>
 <p>- python manage.py migrate</p>

<h3>Запуск проекта</h3>
 <p>- python3 manage.py runserver</p>


