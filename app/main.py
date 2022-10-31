import logging
import pandas as pd

from flask import Flask
from flask import jsonify

from utils.get_data import get_all_projects, get_all_users
from utils.search_utils import (
    search_similar_projects,
    search_specialists_for_project,
    search_projects_for_specialist,
    search_users_for_user
)


logger = logging.getLogger(__name__)


main = Flask(__name__)


url="https://storage.yandexcloud.net/spacebear/embedds.parquet"
EMBEDDINGS_DF=pd.read_parquet(url)


@main.route('/')
def ML_service_space_bear():
    return 'ML_service_space_bear'


@main.route('/embedding/<word>')
def embedding_word(word):
    # return jsonify(embeddings_dict[word].tolist())
    return jsonify(EMBEDDINGS_DF.loc[word].values.tolist())


@main.route('/test_ping')
def test_ping():
    test_output = {}
    test_output["all_projects"] = get_all_projects()
    test_output["all_users"] = get_all_users()
    return jsonify(test_output)


@main.route('/search_similar_projects/<id>')
def search_similar_prs(id):
    result_dict = search_similar_projects(int(id), EMBEDDINGS_DF)
    return jsonify(result_dict)


@main.route('/search_specialists_for_project/<id>')
def search_users_for_pr(id):
    result_dict = search_specialists_for_project(int(id), EMBEDDINGS_DF)
    return jsonify(result_dict)


@main.route('/search_projects_for_specialist/<id>')
def search_prs_for_user(id):
    result_dict = search_projects_for_specialist(int(id), EMBEDDINGS_DF)
    return jsonify(result_dict)


@main.route('/search_users_for_user/<id>')
def search_users_for_usr(id):
    result_dict = search_users_for_user(int(id), EMBEDDINGS_DF)
    return jsonify(result_dict)


if __name__ == '__main__':
    main.run(debug=True)
