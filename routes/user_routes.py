from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import User
from forms import UserForm

# Page d'accueil avec pagination
@app.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(page=page, per_page=5)
    return render_template("index.html", users=users)

# Ajout d'un utilisateur avec Flask-WTF
@app.route("/add", methods=["GET", "POST"])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(
            nom=form.nom.data,
            prenom=form.prenom.data,
            age=form.age.data,
            nationalite=form.nationalite.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Utilisateur ajouté avec succès ✅", "success")
        return redirect(url_for("home"))
    return render_template("add.html", form=form)

# Mise à jour d'un utilisateur
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_user(id):
    user = User.query.get_or_404(id)
    if request.method == "POST":
        user.nom = request.form.get("nom")
        user.prenom = request.form.get("prenom")
        user.age = int(request.form.get("age"))
        user.nationalite = request.form.get("nationalite")
        db.session.commit()
        flash("Utilisateur modifié avec succès ✏️", "success")
        return redirect(url_for("home"))
    return render_template("update.html", user=user)

# Suppression d'un utilisateur
@app.route("/delete/<int:id>")
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash("Utilisateur supprimé ❌", "danger")
    return redirect(url_for("home"))
# 18.216.155.154
# 18.216.155.154