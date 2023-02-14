from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html")


if __name__=="__main__":
    app.run(debug=True, port=3000)