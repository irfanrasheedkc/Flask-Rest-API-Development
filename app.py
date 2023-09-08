from config import db
from flask import Flask

users = db['users']
app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    # Get all users details from the database
    users_list = list(users.find({}, {'_id': 0}))
    return users_list

if __name__=='__main__':
    app.run(debug=True)