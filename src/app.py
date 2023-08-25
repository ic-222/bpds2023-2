from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "khfkh,fkh,flkj"

if __name__== "__main__":
    app.run()

