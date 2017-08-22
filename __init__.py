from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")
@app.route("/other")
def otherpage():
    return render_template("otherpage.html")
@app.route("/3box")
def box():
    return render_template("3box.html")
@app.route("/3line")
def line():
    return render_template("3line.html")
@app.route("/3loader")
def loader():
    return render_template("3loader.html")

if __name__ == "__main__":
    app.run()
