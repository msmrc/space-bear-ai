import requests
from typing import Any, Dict, Optional, List


def get_user(id: int) -> Dict[str, Any]:
    request = requests.get(f"https://space-bear-api.herokuapp.com/api/users/ml-get-by-id/{id}")
    json_dict = request.json()
    return json_dict


def get_all_users() -> List[Dict[str, Any]]:
    request = requests.get("https://space-bear-api.herokuapp.com/api/users/ml-get-all")
    json_dict = request.json()
    return json_dict


def get_project(id: int) -> Dict[str, Any]:
    request = requests.get(f"https://space-bear-api.herokuapp.com/api/projects/ml-get-by-id/{id}")
    json_dict = request.json()
    return json_dict


def get_all_projects() -> Dict[str, Any]:
    request = requests.get("https://space-bear-api.herokuapp.com/api/projects/ml-get-all")
    json_dict = request.json()
    return json_dict
