from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

# run the actual server
if __name__ == "__main__":
    app.run()