from flask import Flask
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.get("/")
def home():
    return "hello world"

app.run(debug=True)