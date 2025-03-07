from datetime import datetime
from jinja2 import Template
from .api import load_environment_variables, get_github_user_data, get_github_repos_data, get_vk_user_data, get_zulip_user_data

TEMPLATE_FILE_NAME = "./templates/index.html"
INDEX_FILE_NAME = "./public/index.html"

def generate_resume():
    with open(TEMPLATE_FILE_NAME, "r", encoding="utf-8") as template_file:
        env_vars = load_environment_variables()
        user_data = get_github_user_data(env_vars["username"], env_vars["token"])
        repos_data = get_github_repos_data(env_vars["username"], env_vars["token"])
        user_data_vk = get_vk_user_data(env_vars["usernamevk"], env_vars["tokenvk"])
        user_data_zulip, role_description = get_zulip_user_data(env_vars["email"], env_vars["tokenzulip"], env_vars["idzulip"])

        template_text = template_file.read()
        jinja_template = Template(template_text)

        context = {
            "name": user_data.get("name", "Не указано"),
            "email": user_data.get("email", "Не указано"),
            "repos": [
                {
                    "name": repo["name"],
                    "description": repo.get("description", "Нет описания"),
                    "language": repo.get("language", "Не указан"),
                    "link": repo["html_url"]
                }
                for repo in repos_data
            ],
            "school": [
                {
                    "school": school.get('name', 'Нет названия')
                }
                for school in user_data_vk['response'][0]["schools"]
            ],
            "university": [
                {
                    "university": university.get('name', 'Нет названия')
                }
                for university in user_data_vk['response'][0]["universities"]
            ],
            "registration_date": user_data_zulip["user"].get("date_joined", "Не указано"),
            "role": role_description,
            "datetime": datetime.now()
        }

        rendered_resume = jinja_template.render(**context)

        with open(INDEX_FILE_NAME, "w", encoding="utf-8") as resume_file:
            resume_file.write(rendered_resume)

def get_resume():
    with open(INDEX_FILE_NAME, "r", encoding="utf-8") as f:
        return f.read()