from flask import Flask, render_template, request, session
from oauth import Oauth
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ['SECRET_KEY']


@app.route("/")
def home():
    return render_template("home_page/index.html", discord_url=os.environ['LOGIN_URL'])


@app.route("/login")
def login():
	code = request.args.get("code")

	at = Oauth.get_access_token(code)
	session["token"] = at

	user = Oauth.get_user_json(at)
	user_name, user_id = user.get("username"), user.get("discriminator")
	
	return render_template("logged_page/index.html", user_name=user_name, user_id=user_id)

@app.route("/api/main")
def api():
	args = request.args

	print(args)

	return render_template("api/index.html")


if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port=81)