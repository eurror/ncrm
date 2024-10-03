# Trello/Jira clone

## TODO
1. Makerfile
2. .env
3. SMTP

## Описание
Система управления задачами, похожая на Trello или Jira, с поддержкой уведомлений и отчетов с помощью Celery.

## Установка и запуска
1. Клонируйте репозиторий
```bash
git clone https://github.com/eurror/ncrm.git
```
2. Создайте виртуальное окружение
```bash
python3 -m venv <venv>
#Активируйте виртуальное окружение ->
source venv/bin/activate
```
3. Установите зависимости
```bash
pip install -r requirements.txt
```
4. Настройте базу данных
```bash
./manage.py migrate
```
5. Запустите сервер
```bash
./manage.py runserver
```bash
celery -A main worker --loglevel=info
celery -A main beat --loglevel=info
```
## Документация и API
Документация доступна по адресу /swagger/ или /redoc/
