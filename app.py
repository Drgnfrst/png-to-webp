# Access it by running it, then going to whatever port its running on (It'll say which port it's running on).
from flask import Flask,render_template,request
import convert_webp
import webbrowser

app=Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def submit():
    path=request.form["path"]
    convert_webp.covert_to_webp(r"{}".format(path))
    return render_template("done.html")

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
    open_browser()
    app.run(port=5000)

