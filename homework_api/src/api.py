import os
import requests
from base64 import b64encode
from dotenv import load_dotenv

load_dotenv()

def load_environment_variables():
    return {
        "token": os.getenv("TOKENgithub"),
        "tokenvk": os.getenv("TOKENvk"),
        "tokenzulip": os.getenv("api"),
        "username": os.getenv("user_git"),
        "usernamevk": os.getenv("user_vk"),
        "idzulip": os.getenv("id_zulip"),
        "email": os.getenv("email_zulip")
    }

# Получение данных пользователя в Github
def get_github_user_data(username, token):
    headers = {
        "Authorization": f"token {token}",
        "User-Agent": "MyApp/1.0"
    }
    response = requests.get(f"https://api.github.com/users/{username}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: {response.status_code}")
        print(response.json())
        return None

# Получение данных о репозиториях пользователя в Github
def get_github_repos_data(username, token):
    headers = {
        "Authorization": f"token {token}",
        "User-Agent": "MyApp/1.0"
    }
    response = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка при получении репозиториев: {response.status_code}")
        print(response.json())
        return None

# Получение данных пользователя в VK
def get_vk_user_data(usernamevk, tokenvk):
    params_vk = {
        "access_token": tokenvk,
        "v": "5.199",
        "user_ids": usernamevk,
        "fields": "schools,universities"
    }
    response = requests.get("https://api.vk.com/method/users.get", params=params_vk)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: {response.status_code}")
        print(response.json())
        return None

# Получение данных пользователя в Zulip и определение его роли
def get_zulip_user_data(email, tokenzulip, idzulip):
    credentials = f"{email}:{tokenzulip}"
    encoded_credentials = b64encode(credentials.encode("utf-8")).decode("utf-8")
    headers_zulip = {
        "Authorization": f"Basic {encoded_credentials}"
    }
    response = requests.get(f"https://chat.miem.hse.ru/api/v1/users/{idzulip}", headers=headers_zulip)
    if response.status_code == 200:
        user_data_zulip = response.json()
        role = user_data_zulip['user'].get('role')
        role_description = {
            100: "Владелец организации",
            200: "Администратор организации",
            300: "Организационный модератор",
            400: "Участник",
            600: "Гость"
        }.get(role, "Неизвестная роль")
        return user_data_zulip, role_description
    else:
        print(f"Ошибка: {response.status_code}")
        print(response.json())
        return None, None
