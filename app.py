from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/solharsh")
def about():
    return render_template("about.html")

@app.route("/site")
def site():
    return render_template("site.html")
    
if __name__ == "__main__":
    app.run(debug=True)
