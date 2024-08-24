from flask import Flask, render_template, url_for
from prettytable import PrettyTable

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/KET")
def ket():
    return render_template("KET.html")



@app.route("/Mindfulness")
def mindfulness():
    
    return render_template("mindfulness.html")


@app.route("/Psichoterapija")
def psichoterapija():
    return render_template("psichoterapija.html")


if __name__=="__main__":
    app.run(debug=True)

