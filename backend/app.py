from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/minecraft/builds', methods=['GET'])
def get_builds():
    return jsonify([{
        'name': 'Build 1',
        'description': 'This is the first build'
    }, {
        'name': 'Build 2',
        'description': 'This is the second build'
    }])
    
@app.route('/minecraft/builds', methods=['POST'])
def add_build():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    # Insert build into the database (assuming `build_planner.db` is set up correctly)
    conn = sqlite3.connect('build_planner.db')
    c = conn.cursor()
    c.execute("INSERT INTO builds (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()
    return jsonify({"message": "Build added successfully!"}), 201

    
if __name__ == '__main__':
    app.run(debug=True)