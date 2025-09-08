from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial in-memory data (acts like a database)
tasks = [
    {'id': 1, 'title': 'Noodles', 'description': 'Noodles with veggies'},
    {'id': 2, 'title': 'Pasta', 'description': 'Pasta with tomato sauce'},
    {'id': 3, 'title': 'Rice', 'description': 'Rice with curry'},
    {'id': 4, 'title': 'Salad', 'description': 'Fresh garden salad'}
]

# Home route
@app.route("/")
def home():
    return "<h1 style='color:blue;text-align:center'>Welcome to the Best Flask Application</h1>"

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'tasks': tasks})

# GET a specific item by ID
@app.route('/items/<int:task_id>', methods=['GET'])
def get_item(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify({'task': task})
    return jsonify({'error': 'Task not found'}), 404

# POST: Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    if not request.is_json:
        return jsonify({'error': 'Bad Request - JSON required'}), 400

    data = request.get_json()
    if 'title' not in data:
        return jsonify({'error': 'Bad Request - title required'}), 400

    new_task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': data['title'],
        'description': data.get('description', "")
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# PUT: Update an existing item
@app.route('/items/<int:task_id>', methods=['PUT'])
def update_item(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    if not request.is_json:
        return jsonify({'error': 'Bad Request - JSON required'}), 400

    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])

    return jsonify({'task': task})

# DELETE: Remove an item
@app.route('/items/<int:task_id>', methods=['DELETE'])
def delete_item(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    tasks.remove(task)
    return jsonify({'result': True})

if __name__ == "__main__":
    app.run(debug=True)
