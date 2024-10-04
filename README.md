# Trello/Jira clone

## TODO
1. Makerfile

## Описание
Система управления задачами, похожая на Trello или Jira, с поддержкой уведомлений и отчетов с помощью Celery.

## Установка и запуска
1. Клонируйте репозиторий
```bash
git clone https://github.com/eurror/ncrm.git
```
2. Создайте виртуальное окружение
```bash
cd ncrm
python3 -m venv <venv>
#Активируйте виртуальное окружение ->
source venv/bin/activate
```
3. Установите зависимости
```bash
pip install -r requirements.txt
```
4. Настройте базу данных
Для удобства, были настроены автоматические начальные данные при миграции
```bash
./manage.py makemigrations
./manage.py migrate
```
5. Создайте файл .env, скопируйте данные с файла template.env в .env и заполните его своими данными
```bash
touch .env
cp template.env .env
### Далее вам необходимо заполнить свои данные в файле .env
```
6. Запустите сервер
```bash
./manage.py runserver
```bash
celery -A main worker --loglevel=info
celery -A main beat --loglevel=info
```
## Документация и API
Документация доступна по адресу /swagger/ или /redoc/
