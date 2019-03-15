from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
import dns

app = Flask(__name__)
app.config['MONGO_DBNAME'] = ''
app.config['MONGO_URI'] = ''
mongo = PyMongo(app)

# ------- Main Page -------

@app.route('/')
def index():
    return render_template('index.html')

# ------- Sending Subscription User Data to MongoDB Atlas -------

@app.route('/subscribed', methods=['GET','POST'])
def subscribed():
    email_txt = request.form['email']
    target_db = mongo.db.email_subscriptions
    email_check = target_db.find_one({'email': email_txt})          # Email Validation
    if email_check:
        return jsonify({'error':'Oops! Email already in use'})     # Email Duplicate Error Message
    else:
        target_db.insert({'email': email_txt})
        return jsonify({'success':'Success! You are Subscribed'})   # Email Correct

if __name__ == '__main__':
    app.run(debug=True)
