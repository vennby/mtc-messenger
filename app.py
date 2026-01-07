from flask import Flask, render_template, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'microsofttechclub@dubai.bits-pilani.ac.in'
app.config['MAIL_PASSWORD'] = 'rbnj oaoo uekf mtvu'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send')
def send_email(): 
    msg = Message(
        subject='Hello!',
        sender='microsofttechclub@dubai.bits-pilani.ac.in',
        recipients=['f20220233@dubai.bits-pilani.ac.in'],
        body='This email was sent automatically through Flask!'
    )
    mail.send(msg)
    return render_template('sent.html')