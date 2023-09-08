from config import db
from flask import Flask,jsonify,request

users = db['users']
app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        # Retrieve all users from the 'users' collection
        user_list = list(users.find({}, {'_id': 0}))
        
        # Return the list of users as JSON
        return jsonify({"users": user_list})
    except Exception as e:
        # Handle any errors that may occur (e.g., database connection issues)
        return jsonify({"message": str(e)}), 500

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        # Get user data by id
        user = users.find_one({"id": user_id}, {'_id': 0})
        
        if user:
            # If the user is found, return the user data as JSON
            return jsonify({"user": user})
        else:
            # If the user is not found, return a 404 error
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        # Return error
        return jsonify({"message": str(e)}), 500

# Define a function to validate user data
def validate_user_data(user_data):
    required_fields = ["id", "name", "email", "password"]
    
    # Check if all required fields are present in the data
    for field in required_fields:
        if field not in user_data:
            return False, f"Missing field: {field}"
    
    return True, None

@app.route('/users', methods=['POST'])
def create_user():
    try:
        # Get user data from the request JSON
        user_data = request.get_json()

        # Validate the user data
        is_valid, validation_message = validate_user_data(user_data)
        
        if not is_valid:
            return jsonify({"message": f"Invalid user data. {validation_message}"}), 400

        # Check if the user with the specified ID already exists
        existing_user = users.find_one({"id": user_data["id"]})
        if existing_user:
            return jsonify({"message": "User with the same ID already exists"}), 409

        # Insert the new user into the 'users' collection
        result = users.insert_one(user_data)
        
        # Return the ID of the newly created user
        return jsonify({"message": "User created"}), 201
    except Exception as e:
        # Handle any errors that may occur (e.g., database connection issues)
        return jsonify({"message": str(e)}), 500

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        # Get updated user data from the request JSON
        updated_data = request.get_json()
        
        # Update the user with the specified ID with the new data
        result = users.update_one({"id": user_id}, {"$set": updated_data})
        
        if result.modified_count == 1:
            return jsonify({"message": "User updated"})
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        # Handle any errors that may occur (e.g., database connection issues)
        return jsonify({"message": str(e)}), 500

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        # Delete the user with the specified ID
        result = users.delete_one({"id": user_id})
        
        if result.deleted_count == 1:
            return jsonify({"message": "User deleted"})
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        # Handle any errors that may occur (e.g., database connection issues)
        return jsonify({"message": str(e)}), 500

if __name__=='__main__':
    app.run(debug=True)