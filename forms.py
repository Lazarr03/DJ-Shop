from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import ValidationError, DataRequired

class RegistrationForm(Form):
    name = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired()])
    submit = SubmitField("Send")

class LoginForm(Form):
    username = StringField(label="Username", validators=[DataRequired()])
    sifra = StringField(label='Password', validators=[DataRequired()])
    logSubmit = SubmitField("Send")