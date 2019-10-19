# ---- Dependacies Import ----
from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
import dns
# ----
from instance.config import mongo_dbname, mongo_uri, email, password
# ----

app = Flask(__name__)

# ------- MongoDB configuration --------
app.config['MONGO_DBNAME'] = mongo_dbname
app.config['MONGO_URI'] = mongo_uri

app.config['MONGO_DBNAME'] = ''
app.config['MONGO_URI'] = ''

mongo = PyMongo(app)

# ------- FLask_Mail Config -------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False

app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = password

app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''

mail = Mail(app)

# ------- Main Page -------
@app.route('/')
def index():
    return render_template('index.html')

# ------- Sending Subscription User Data to MongoDB Atlas -------
@app.route('/subscribed', methods=['GET','POST'])
def subscribed():
    email_txt = request.form['email']
    target_db = mongo.db.email_subscriptions
    email_check = target_db.find_one({'email': email_txt})                                                 #Email Validation
    if email_check:
        return jsonify({'error':'<b> Email in Use <b>'})                                             #Email Duplicate Error Message
    else:
        target_db.insert({'email': email_txt})
        return jsonify({'success':'<b> You are Subscribed <b>'})                                          #Email Correct

@app.route('/email', methods=['POST'])
def email():
    email_txt = request.form['email']
    welcome_email = Message("🤗💌 Welcome to the Napier Fintech & Blockchain Society!", sender='napierblockchain@gmail.com', recipients=[email_txt])  #Send email to the Subscribed User
    welcome_email.html = '<h1> Thank you for subscribing to us! </h1> <hr> <p> We hope you will continue with us in our exciting journey into the future of Fintech & Blockchain! We have much exciting stuff planned for the future, and we would like you to be a part of it! 🤗 </p> <p> ☺️ Help us grow by mentioning us to your friends or via social media. </p> <p> Stay tuned on our social media platforms to keep up-to-date with us and our progress! </p> <hr> <br> <p> For any questions, please email us to contactus@napierfintech.com 24/7 </p> <p> If you consider sponsoring us ❤️, please email us to napierblockchain@gmail.com 24/7 </p> <br> <p> Fintech & Blockchain Society | Edinburgh Napier Univeristy | <b> Striving for Future Knowledge </b> </p>'                                                        #Customize based on user input
    mail.send(welcome_email)                                                                           #Send Email
    return "Success"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
