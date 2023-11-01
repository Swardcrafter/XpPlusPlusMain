from flask import Flask, render_template
import os

app = Flask(__name__)

login_url = os.environ['LOGIN_URL']

@app.route("/")
def home():
    return render_template("index.html", discord_url=login_url)


@app.route("/login")
def login():
	return "Done"


if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port=81)