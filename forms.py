from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class UserForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired(), Length(min=2, max=80)])
    prenom = StringField("Prénom", validators=[DataRequired(), Length(min=2, max=80)])
    age = IntegerField("Âge", validators=[DataRequired(), NumberRange(min=1, max=120)])
    nationalite = StringField("Nationalité", validators=[DataRequired(), Length(min=2, max=80)])
    submit = SubmitField("Ajouter")
    
