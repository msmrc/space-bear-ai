import pickle
import logging
import pandas as pd

from flask import Flask
from flask import jsonify

from utils.get_data import get_user, get_project, get_all_projects, get_all_users


logger = logging.getLogger(__name__)


main = Flask(__name__)


# with open('../assets/embedds.pickle', 'rb') as f:
#     embeddings_dict = pickle.load(f)
#     logger.info("Embeddings loaded")


# just for test
dfs = []
for i in range(40):
    selected_df = pd.read_parquet(f"./assets/embedds_chunks/chunk_{i}.parquet")
    dfs.append(selected_df)
embeddings_df = pd.concat(dfs)


@main.route('/')
def ML_service_space_bear():
    return 'ML_service_space_bear'


@main.route('/embedding/<word>')
def embedding_word(word):
    # return jsonify(embeddings_dict[word].tolist())
    return jsonify(embeddings_df.loc[word].values.tolist())


@main.route('/test_ping')
def test_ping():
    test_output = {}
    test_output["all_projects"] = get_all_projects()
    test_output["all_users"] = get_all_users()
    return jsonify(test_output)


if __name__ == '__main__':
    main.run(debug=True)
