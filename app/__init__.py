from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fhadabonerules'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525' # (or try 2525)
app.config['MAIL_USERNAME'] = '325adc92daa880'
app.config['MAIL_PASSWORD'] = '15becad413a1c3'
mail = Mail(app)
from app import views
