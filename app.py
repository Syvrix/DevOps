## Import flask
from flask import Flask, request, render_template  # type: ignore

app = Flask(__name__)


## Basic Routes
@app.route('/')
def Home():
    return render_template("Home.html", title="Min hemsida")

@app.route('/submit', methods=["POST"])
def submit():
    email=request.form["email"]
    print(email)
    return "Email has been submitted, you will be contacted"

## display debugg data to the console.
if __name__ == "__main__":
    app.run(debug=True)
