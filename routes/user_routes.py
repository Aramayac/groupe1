from flask import Blueprint, request, render_template, redirect, url_for, flash
from models import User, db

# Déclaration du Blueprint
user_bp = Blueprint("user_bp", __name__)

# Page d'accueil avec pagination
@user_bp.route("/")
def home():
    page = request.args.get("page", 1, type=int)
    users = User.query.paginate(page=page, per_page=5)
    return render_template("index.html", users=users)

# Ajouter un utilisateur
@user_bp.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        nom = request.form["nom"]
        prenom = request.form["prenom"]
        age = request.form["age"]
        nationalite = request.form["nationalite"]

        new_user = User(nom=nom, prenom=prenom, age=age, nationalite=nationalite)
        db.session.add(new_user)
        db.session.commit()
        flash("✅ Utilisateur ajouté avec succès", "success")
        return redirect(url_for("user_bp.home"))

    return render_template("add.html")

# Mettre à jour un utilisateur
@user_bp.route("/update/<int:id>", methods=["GET", "POST"])
def update_user(id):
    user = User.query.get_or_404(id)
    if request.method == "POST":
        user.nom = request.form["nom"]
        user.prenom = request.form["prenom"]
        user.age = request.form["age"]
        user.nationalite = request.form["nationalite"]

        db.session.commit()
        flash("✏️ Utilisateur modifié avec succès", "info")
        return redirect(url_for("user_bp.home"))

    return render_template("update.html", user=user)

# Supprimer un utilisateur
@user_bp.route("/delete/<int:id>", methods=["GET"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash("🗑️ Utilisateur supprimé avec succès", "danger")
    return redirect(url_for("user_bp.home"))
