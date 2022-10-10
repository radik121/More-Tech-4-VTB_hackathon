## Установка и запуск
Склонируйте репозиторий в рабочую директорию
 
 `git clone https://github.com/paragonov/nap-api.git`
 
Создайте образы Docker

`sudo docker-compose up -d --build`

### Запуск Telegram-bot

Установите зависимости

`pip install -r requirements.txt`

Перейдите в рабочую директорию бота и запустите файл

`python tg-bot.py`

Зайдите в приложение Telegram и найдите бота @test_news_hack_bot
- команда /start запускает бота
