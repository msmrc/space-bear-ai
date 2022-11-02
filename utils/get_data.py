import requests
from typing import Any, Dict, List

request_all_users = requests.get("https://space-bear-api.herokuapp.com/api/users/get-all-users")
all_users_dict = request_all_users.json()
all_users = {user['_id']: user for user in all_users_dict}

request_all_projects = requests.get("https://space-bear-api.herokuapp.com/api/projects/ml-get-all")
all_projects_dict = request_all_projects.json()
all_projects = {project['_id']: project for project in all_projects_dict}

def get_user(id: str) -> Dict[str, Any]:
    # request = requests.get(f"https://space-bear-api.herokuapp.com/api/users/ml-get-by-id/{id}")
    # json_dict = request.json()
    # return json_dict
    return all_users[id]


def get_all_users() -> List[Dict[str, Any]]:
    # request = requests.get("https://space-bear-api.herokuapp.com/api/users/ml-get-all")
    # json_dict = request.json()
    # return json_dict
    return list(all_users.values())


def get_project(id: str) -> Dict[str, Any]:
    # request = requests.get(f"https://space-bear-api.herokuapp.com/api/projects/ml-get-by-id/{id}")
    # json_dict = request.json()
    # return json_dict
    return all_projects[id]


def get_all_projects() -> List[Dict[str, Any]]:
    # request = requests.get("https://space-bear-api.herokuapp.com/api/projects/ml-get-all")
    # json_dict = request.json()
    # return json_dict
    return list(all_projects.values())
