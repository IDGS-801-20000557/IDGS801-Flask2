from flask import Flask, render_template, redirect
from flask import request
import forms
from operaciones import Calculadora
from agregarTxt import txt
from flask import make_response
from flask import flash
from flask_wtf import CSRFProtect


app=Flask(__name__)
app.config['SECRET_KEY']="esta es tu clave encriptada"
csrf=CSRFProtect()
#app.secret_key="claudio"
cantidad=[]

@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/traductor", methods=['GET', 'POST'])
def traductor():
    print("ssss")
    active=""
    if request.method=='POST' and request.form.get("bandera")=="1":
        txt.addPalabras(request.form.get("ingles"), request.form.get("espanol"))
    if request.method=='POST' and request.form.get("bandera2")=="2":
       active=txt.buscar(request.form.get("buscar"), request.form.get("numero"))
    return render_template("traductor.html", active=active)

@app.route("/cookie", methods=['GET', 'POST'])
def cookie():
    reg_user=forms.LoginForm(request.form)
   
    if request.method=='POST' and reg_user.validate():
        user=reg_user.username.data
        pasw=reg_user.password.data
        datos=user+"@"+pasw
        sucess_message='Bienvenido {}'.format(user)
        response.set_cookie('datos_user',datos)
        flash(sucess_message)
    response=make_response(render_template("cookie.html", form=reg_user))
       
        
    return response
 

@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    mat=''
    nom=''
    if request.method == 'POST' and reg_alum.validate():
        mat=reg_alum.matricula.data
        nom=reg_alum.nombre.data
    return render_template("Alumnos.html", form=reg_alum, mat=mat,nom=nom)

@app.route("/CajasDinamicas", methods=['GET','POST'])
def cajasDinamicas():
    Active = False
    Ns = 0
    
    if request.method == 'POST':
        Ns = int(request.form.get('numero'))
        Active = Ns != 0
    
    return render_template('cajasDinamicas.html', active = Active, ns = Ns, name="Cajas Dinámicas")
    
    

@app.route("/resultados", methods=['GET','POST'])
def res():
    Numeros = Calculadora.get_Array(request.form)
    
    return render_template("operaciones.html",
                           numeros = Numeros,
                           repetidos = Calculadora.contarRepeticiones(Numeros),
                           comas = Calculadora.concatenarNumeros(Numeros),
                           promedio = Calculadora.promedio(Numeros),
                           nMenor = Calculadora.numMenor(Numeros),
                           nMayor = Calculadora.numMayor(Numeros),
                           name = "Resultado de " + str(len(Numeros)) + " números")





    

if __name__=="__main__":
   ## csrf.init_app(app)
    app.run(debug=True, port=3000)