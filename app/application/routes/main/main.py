from flask import Blueprint, render_template, make_response


main = Blueprint('main', __name__)

#################################### ROUTES ####################################
################################################################################
@main.route("/")
def home():
    resp = make_response(render_template(
        "main/home.html"))
    return resp
