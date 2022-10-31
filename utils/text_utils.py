from typing import List
import string

import pandas as pd
import numpy as np

from utils.get_data import get_project, get_user


def embedd_representation(input_str: str, embeddings_df: pd.DataFrame) -> np.ndarray:
    input_str = input_str.translate(str.maketrans('', '', string.punctuation))
    splitted_str = input_str.split()
    embeddings_list = np.asarray([(embeddings_df.loc[word] if word in embeddings_df.index.tolist() else np.zeros(50)) for word in splitted_str])
    mean_embedds = np.mean(embeddings_list, axis=0)
    return mean_embedds


def get_project_text_desc(id: int) -> str:
    project_dict = get_project(id)
    return project_dict['projectDescription']


def get_user_text_desc(id: int) -> str:
    user_dict = get_user(id)
    return user_dict['aboutDescription']


def get_user_skill_desc(id: int) -> List[str]:
    user_dict = get_user(id)
    return user_dict['skillInformation']['skills']


def get_user_roles_desc(id: int) -> List[str]:
    user_dict = get_user(id)
    return user_dict['skillInformation']['categories']