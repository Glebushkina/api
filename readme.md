# README

## Описание программы

Программа предоставляет api к сгенерированному в формате HTML резюме. Программа запускает локальный HTTP-сервер, который отображает резюме студента в браузере. Резюме включает информацию о пользователе из трех различных сервисов: GitHub, VK и Zulip. Она извлекает информацию о профиле пользователя, его репозиториях (для GitHub), образовательных учреждениях (для VK) и роли в организации (для Zulip). 

## Настройка программы

### 1. Установка зависимостей

1. ```python -m venv venv```
2. windows: ```.\venv\Scripts\activate```
unix: ```sourse ./venv./bin/activate```
3. ```pip install -r requirements.txt```

### 2. Создание конфигурационного файла

Необходимо создать файл .env и заполните его следующими переменными:
(GitHub)
TOKENgithub=ваш_токен_github
user_git=ваше_username_github

(VK)
TOKENvk=ваш_токен_vk
user_vk=ваше_username_vk

(Zulip)
api=ваш_api_ключ_zulip
id_zulip=ваш_id_zulip
email_zulip=ваш_email_zulip

Как получить токены:
1. GitHub
    - Перейдите в [настройки разработчика](https://github.com/settings/tokens) на GitHub
    - Создайте новый токен (Personal access tokens (classic)) с необходимыми разрешениями (read:user, user:email)
2. VK
    - Перейдите на сайт по получению [токенов доступа](https://vkhost.github.io/)
    - Выполните инструкции
3. Zulip
    - Перейдите в настройки профиля в Zulip 
    - Выберите  "Учетная запись и конфиденциальность"
    - Получите API-ключ

## Запуск программы

После настройки конфигурационного файла, программа готова к запуску. В терминале нужно ввести 

```bash
python main.py
```
где main.py - название файла программы.
Сервер запустится на http://localhost:3000. Откройте этот адрес в браузере, чтобы увидеть резюме.

## Обновление зависимостей

При добавлении новых зависимостей в проект, обновите файл requirements.txt с помощью команды:

```pip freeze > requirements.txt```

Этот файл должен использоваться для установки всех пакетов с указанными версиями.

## Структура проекта

```bash
project/
├── src/
│   ├── .env
│   ├── api.py
│   └── resume_manipulator.py
├── templates/
│   └── index.html
├── public/
│   └── index.html
├── requirements.txt
└── main.py
```

## Результат работы программы

После успешного выполнения программы, сервер запустится на http://localhost:3000. Открыв этот адрес в браузере, можно увидеть резюме.
