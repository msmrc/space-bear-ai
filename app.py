from flask import Flask
from flask import jsonify
from flask import json
from utils.get_data import get_user, get_project, get_all_projects, get_all_users
app = Flask(__name__)


@app.route('/')
def ML_service_space_bear():
    return 'ML_service_space_bear'


@app.route('/test_ping')
def test_ping():
    test_output = {}
    test_output["all_projects"] = get_all_projects()
    test_output["all_users"] = get_all_users()
    return jsonify(test_output)


if __name__ == '__main__':
    app.run(debug=True)