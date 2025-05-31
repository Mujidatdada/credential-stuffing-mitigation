from flask import Flask, request, jsonify

app = Flask(__name__)
 
 # Mock user database
users = {
     "user1@example.com": "password123",
     "user2@example.com": "welcome2023",
     "admin@bank.com": "securepass"
}
 
@app.route('/login', methods=['POST'])
def login():
     data = request.get_json()
     email = data.get('email')
     password = data.get('password')
 
     if users.get(email) == password:
         return jsonify({"message": "Login successful"}), 200
     else:
         return jsonify({"message": "Invalid credentials"}), 401
 
if __name__ == '__main__':
     app.run(debug=True, host="0.0.0.0", port 80)
