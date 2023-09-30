from flask import Flask, request, jsonify, abort
import argparse

app = Flask(__name__)

users = {} # A simple in-memory "database" for demonstration purposes

# Definitions of validations
def validate_user_exists(user_id):
    """Check if user exists."""
    if user_id not in users:
        abort(404, description="User not found")

def validate_user_not_exists(user_id):
    """Check if user doesn't exist."""
    if user_id in users:
        abort(400, description="User already exists")

def validate_data(data, require_all=True):
    """Validate user data."""
    if not data:
        abort(400, description="Invalid data")

    if require_all and ("name" not in data or "email" not in data):
        abort(400, description="Missing required fields")

# REST Routes
@app.route("/")
def home():
    return "Hey there!"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    validate_user_exists(user_id)
    return jsonify(users[user_id]), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = data["user_id"]

    # Basic validation
    validate_data(data)
    validate_user_not_exists(user_id)

    users[user_id] = {
        "user_id": user_id,
        "name": data["name"],
        "email": data["email"]
    }
    return jsonify(users[user_id]), 201

@app.route("/update-user/<user_id>", methods=["PUT"])
def update_user(user_id):
    validate_user_exists(user_id)
    data = request.get_json()
    validate_data(data)
    
    # Update user data
    users[user_id].update(data)
    users[user_id]['user_id'] = user_id  # Ensure user_id remains consistent
    
    return jsonify(users[user_id]), 200

@app.route("/patch-user/<user_id>", methods=["PATCH"])
def patch_user(user_id):
    validate_user_exists(user_id)
    data = request.get_json()
    validate_data(data, require_all=False)
    
    # Partially update user data
    for key, value in data.items():
        if key in users[user_id]:
            users[user_id][key] = value
    
    return jsonify(users[user_id]), 200

@app.route("/delete-user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    validate_user_exists(user_id)
    del users[user_id]
    return "", 204

@app.errorhandler(400)
def bad_request(error):
    message = str(error).split(": ", 1)[-1]  # This will split at the first ": " and take the second part
    return jsonify({"error": True, "message": message}), 400

@app.errorhandler(404)
def not_found(error):
    message = str(error).split(": ", 1)[-1]  # This will split at the first ": " and take the second part
    return jsonify({"error": True, "message": message}), 404

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Flask web server.")
    parser.add_argument("--port", default=6000, help="Port to run the server on.")
    args = parser.parse_args()

    app.run(debug=True, host="0.0.0.0", port=args.port)