from flask import Flask, render_template
from testScript import sayHello # it works!

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    sayHello()
    return render_template("home.html")

# main app route (for the entry into the app)
@app.route("/app")
def application():
    return render_template("app.html")

@app.route("/about")
def about():
    return render_template("about.html")

# run the actual server
if __name__ == "__main__":
    app.run(debug=True)