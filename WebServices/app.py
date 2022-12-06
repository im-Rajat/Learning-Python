# https://www.youtube.com/watch?v=-gUyWoe_SKI&ab_channel=edureka%21

from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {
        'id': '101',
        'name': 'Saravanan S',
        'title': 'Technical Leader'
    },
    {
        'id': '201',
        'name': 'Rajkumar P',
        'title': 'Sr Software Engineer'
    }
]


@app.route('/')
def index():
    return "Welcome To The Course API"


@app.route("/employees", methods=['GET'])
def get():
    return jsonify({'Employees': employees})


@app.route("/employees/<int:id>", methods=['GET'])
def get_course(id):
    return jsonify({'id': employees[id]})


@app.route("/employees", methods=['POST'])
def create():
    employee = {
                    'id': '301',
                    'name': 'Roshan S',
                    'title': 'Leader'
                }
    employees.append(employee);
    return jsonify({'Created' : employee})


@app.route("/employees/<int:id>", methods=['PUT'])
def employee_update(id):
    employees[id]['title'] = "New Title"
    return jsonify({'employees': employees[id]})


@app.route("/employee/<int:id>", methods=['DELETE'])
def delete(id):
    employees.remove(employees[id])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True)
