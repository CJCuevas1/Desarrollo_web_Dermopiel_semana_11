from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ClienteForm(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[
        DataRequired(message="El nombre es obligatorio.")
    ])
    email = StringField('Correo Electrónico', validators=[
        DataRequired(message="El correo es obligatorio."),
        Email(message="Ingrese un correo electrónico válido.")
    ])
    telefono = StringField('Teléfono', validators=[
        DataRequired(message="El teléfono es obligatorio."),
        Length(min=7, max=15, message="El teléfono debe tener entre 7 y 15 dígitos.")
    ])
    submit = SubmitField('Guardar Cliente')