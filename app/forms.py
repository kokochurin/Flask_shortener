from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class URLForm(FlaskForm):
    url = StringField("Введите ссылку", validators=[DataRequired(message="Поле для ввода ссылки не может быть пустым")])
    submit = SubmitField("Сократить")
