from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, TextAreaField,RadioField,PasswordField
from wtforms import validators

def mi_validacion(form, field):
    if len(field.data)==0:
        raise validators.ValidationError("El campo no tiene datos")

class UserForm(Form):
    matricula=StringField('Matricula',[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4,max=10, message='longitud del campo 4 min y 10 max')
        ])
    nombre=StringField('Nombre',[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4,max=10, message='longitud del campo 4 min y 10 max')
    ])
    amaterno=StringField('Amaterno',[mi_validacion])
    apaterno=StringField('Apaterno')
    email=StringField('Correo')

class UserForm2(Form):
    txtNum=StringField('TxtNum')
    resultado=StringField('Resultado')

class LoginForm(Form):
    username=StringField('usuario',[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4,max=10, message='longitud del campo 4 min y 10 max')
        ]) 
    password=StringField('password',[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4,max=10, message='longitud del campo 4 min y 10 max')
        ])
    
