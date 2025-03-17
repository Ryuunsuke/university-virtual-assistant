from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

users = {}  # Temporary storage for registered users

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username in users and users[username] == password:
        return "Login Successful"
    else:
        return "Invalid username or password"

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    
    if username in users:
        return jsonify({"message": "Username already exists."}), 400
    else:
        users[username] = password  # Store the username and password (in memory for now)
        return jsonify({"message": "Registration successful!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
