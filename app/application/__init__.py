from flask import current_app, Flask, redirect, url_for


app = Flask(__name__)

debug, testing = False, False

app.debug = debug
app.testing = testing


# Register the App blueprints
from .routes.main.main import main as Main
from .routes.main.handlers import error_pages as ErrorPages

app.register_blueprint(Main)
app.register_blueprint(ErrorPages)


# Add a default root route.
@app.route("/")
def index():
    return redirect(url_for('main.home'))
