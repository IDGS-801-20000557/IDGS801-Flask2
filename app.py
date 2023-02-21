from flask import Flask, render_template, redirect
from flask import request
import forms
from operaciones import Calculadora
 
app=Flask(__name__)
cantidad=[]

@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    mat=''
    nom=''
    if request.method == 'POST':
        mat=reg_alum.matricula.data
        nom=reg_alum.nombre.data
    return render_template("Alumnos.html", form=reg_alum, mat=mat,nom=nom)

@app.route("/CajasDinamicas", methods=['GET','POST'])
def cajasdINAMICAS():
    Active = False
    Ns = 0
    
    if request.method == 'POST':
        Ns = int(request.form.get('numero'))
        Active = Ns != 0
    
    return render_template('cajasDinamicas.html', active = Active, ns = Ns, name="Cajas Dinámicas")
    
    #flash(message)
    return render_template("cajasDinamicas.html", form=formulario, variable=variable)

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
    app.run(debug=True, port=3000)