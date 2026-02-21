from flask import Blueprint, request, render_template
from models import User

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/")
def home():
    page = request.args.get("page", 1, type=int)
    users = User.query.paginate(page=page, per_page=5)
    return render_template("index.html", users=users)