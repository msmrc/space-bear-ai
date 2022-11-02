import pandas as pd
from typing import Dict

from utils.get_data import get_all_projects, get_project, get_all_users, get_user
from utils.text_utils import get_project_text_desc, embedd_representation
from utils.similarity_utils import cosine_similarity
from utils.text_utils import get_user_text_desc, get_user_roles_desc, get_user_skill_desc
from utils.metric_utils import intersection_metric


def search_similar_projects(input_id: str, input_df: pd.DataFrame) -> Dict[int, float]:
    input_desc = get_project_text_desc(input_id)
    input_embedd = embedd_representation(input_desc, input_df)

    all_projects = get_all_projects()
    all_id_embedds = {project['_id']:embedd_representation(get_project_text_desc(project['_id']), input_df) for project in all_projects}

    all_id_embedds.pop(str(input_id), None)

    result_dict = {id: cosine_similarity(input_embedd, all_id_embedds[id]) for id in all_id_embedds.keys()}

    return result_dict


def search_specialists_for_project(project_id: str, input_df: pd.DataFrame) -> Dict[int, Dict[str, float]]:
    looking_for_info = get_project(project_id)['lookingForTeam']

    all_users = get_all_users()
    all_ids = [user['_id'] for user in all_users]

    exist_ids = [user['_id'] for user in get_project(project_id)['existTeam']]

    result_dict = {}

    for id in all_ids:
        if id not in exist_ids:
            id_metrics = {}
            for info in looking_for_info:
                role_metric = 1 if intersection_metric(get_user_roles_desc(id), info['category']) > 0 else 0
                skills_metric = intersection_metric(get_user_skill_desc(id), info['skills'])
                result_metric = role_metric * skills_metric
                id_metrics[info['category']] = result_metric
            user_desc = get_user_text_desc(id)
            project_desc = get_project_text_desc(project_id)
            id_metrics['semantic'] = cosine_similarity(embedd_representation(user_desc, input_df), embedd_representation(project_desc, input_df))
            result_dict[id] = id_metrics

    return result_dict


def search_projects_for_specialist(user_id: str, input_df: pd.DataFrame) -> Dict[int, Dict[str, float]]:

    roles = get_user_roles_desc(user_id)
    skills = get_user_skill_desc(user_id)
    desc = get_user_text_desc(user_id)

    all_projects = get_all_projects()
    all_ids = [user['_id'] for user in all_projects]

    result_dict = {}

    for id in all_ids:
        id_metrics = {}
        looking_for_info = get_project(id)['lookingForTeam']
        for info in looking_for_info:
            role_metric = 1 if intersection_metric(roles, info['category']) > 0 else 0
            skills_metric = intersection_metric(skills, info['skills'])
            result_metric = role_metric * skills_metric
            id_metrics[info['category']] = result_metric
        project_desc = get_project_text_desc(id)
        id_metrics['semantic'] = cosine_similarity(embedd_representation(desc, input_df), embedd_representation(project_desc, input_df))
        result_dict[id] = id_metrics

    return result_dict


def search_users_for_user(user_id: str, input_df: pd.DataFrame) -> Dict[int, Dict[str, float]]:
    interests = get_user(user_id)['interestedTags']
    desc = get_user(user_id)['aboutDescription']

    all_users = get_all_users()

    result_dict = {}

    for user in all_users:
        if user['_id'] != user_id:
            interests_metric = intersection_metric(interests, user['interestedTags'])
            semantic_metric = cosine_similarity(embedd_representation(desc, input_df), embedd_representation(user['aboutDescription'], input_df))
            result_dict[user['_id']] = {"Interests": interests_metric, "Semantic": semantic_metric}

    return result_dict
