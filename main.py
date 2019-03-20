from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
import dns

app = Flask(__name__)
<<<<<<< HEAD

# ------- MongoDB configuration --------
app.config['MONGO_DBNAME'] = 'enubfs_data'
app.config['MONGO_URI'] = 'mongodb+srv://mhashX:EeAuDKtDeUZV8x00@enubfs-ak8by.mongodb.net/enubfs_data'

=======
app.config['MONGO_DBNAME'] = ''
app.config['MONGO_URI'] = ''
>>>>>>> c5627e79056c982f6788ac071f310ec7a1295571
mongo = PyMongo(app)

# ------- FLask_Mail Config -------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'napierblockchain@gmail.com'
app.config['MAIL_PASSWORD'] = 'bitcoin4life!'

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
        # email_txt = request.form['email']
        # welcome_email = Message("Welcome to the Napier Fintech & Blockchain Society!", sender='napierblockchain@gmail.com', recipients=[email_txt])  #Send email to the Subscribed User
        # welcome_email.body = 'This is a test email'                                                        #Customize based on user input
        # wlecome_email.html = render_template('index.html')
        # mail.send(welcome_email)
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
    app.run(debug=True)
