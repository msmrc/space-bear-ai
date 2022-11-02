import pandas as pd

from utils.get_data import get_project
from utils.text_utils import get_project_text_desc, embedd_representation
from utils.similarity_utils import cosine_similarity


def innovation_score_project(project_id: str, input_df: pd.DataFrame) -> bool:
    desc = get_project(project_id)['projectDescription']

    innovative_desc = "инновации ии искусственный интеллект дополненная виртуальная реальность энергосбережение автоматизация роботы робототехника" \
                      "имплантация космос генерализация блокчейн криптовалюта нфт аи децентрализованный децентрализация метавселенная неинвазивный"

    metric = cosine_similarity(embedd_representation(desc, input_df), embedd_representation(innovative_desc, input_df))

    return metric > 0.75