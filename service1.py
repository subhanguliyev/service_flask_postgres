
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['Get'])
def welcome():
    return "Welcome to Python service 1"


if __name__ == "__main__":
    app.run()