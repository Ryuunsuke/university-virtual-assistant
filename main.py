from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from back_end.authentication import *
import database

app = Flask(__name__)
CORS(app)

@app.route('/home')
def index():
    return render_template('auth.html')

@app.route('/login', methods=['POST'])
def login():
    if request.content_type != 'application/json':
        return jsonify({"success": False, "message": "Content-Type must be application/json"}), 415
    else:
        try:
            data = request.get_json()  # Extract JSON data correctly
            print(f"Received data: {data}")  # Log the incoming data for debugging
            
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return jsonify({"success": False, "message": "Username and password are required"}), 400
            
            if database.check_user(username):  # Ensure this function checks if the user exists
                if database.check_pass(username) == password:  # Ensure this compares the password correctly
                    # return redirect(url_for('main'))
                    return jsonify({"success": True, "message": "Login Successful"}), 200
                else:
                    return jsonify({"success": False, "message": "Incorrect username or password"}), 401
            else:
                return jsonify({"success": False, "message": "User does not exist"}), 404
            
        except Exception as e:
            # Log the error for debugging
            print(f"Error occurred: {str(e)}")
            return jsonify({"success": False, "message": f"Error: {str(e)}"}), 500

    
@app.route('/register', methods=['POST'])
def register():
    if request.content_type != 'application/json':
        return jsonify({"success": False, "message": "Content-Type must be application/json"}), 415
    else:
        try:
            data = request.get_json()  # This extracts JSON data correctly
            
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')

            if database.check_user(username) == username:
                return jsonify({"success": False, "message": "User already exist"}), 400
            else: 
                database.register(username, password, email, 0)
                return jsonify({"success": True, "message": "User registered successfully!"})
        except Exception as e:
            return jsonify({"success": False, "message": str(e)}), 500

# @app.route('/main')
# def main():
    
#     return render_template('main.html') 

if __name__ == '__main__':
    app.run(debug=True)
