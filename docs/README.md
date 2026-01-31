markdown
# 📌 Projet Flask CRUD — Documentation

## 🚀 Présentation
Ce projet est une application Flask permettant de gérer un CRUD (Create, Read, Update, Delete) sur des utilisateurs.  
Il utilise **Flask**, **SQLAlchemy** et **Flask-Migrate** pour la gestion de la base de données et des migrations.

---

## 📂 Structure du projet

environment/
│
├── flask_project/
│   ├── app.py                            # Point d'entrée Flask
│   ├── models.py                      # Définition des modèles SQLAlchemy
│   ├── routes/             # Routes organisées par module
│   ├── templates/          # Templates HTML (Jinja2)
│   ├── static/             # Fichiers statiques (CSS, JS, images)
│   ├── migrations/         # Géré par Flask-Migrate
│   └── config.py                      # Configuration (DB, debug, etc.)
│
├── docs/
│   ├── README.md                      # Documentation générale
│   ├── INSTALL.md                    # Instructions d’installation
│   └── WORKFLOW.md                  # Bonnes pratiques Git et migrations
│
├── tests/                  # Tests unitaires
├── requirements.txt                # Dépendances Python
└── venv/                   # Environnement virtuel

Code

---

## ⚙️ Installation

### 1. Créer l’environnement virtuel
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
.\venv\Scripts\activate    # Windows PowerShell
2. Installer les dépendances
bash
pip install flask flask_sqlalchemy flask_migrate
pip freeze > requirements.txt
🛠️ Configuration
Dans app.py :

python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
🗄️ Migrations (à exécuter depuis flask_project/)
Initialiser les migrations
bash
flask db init
Créer une migration
bash
flask db migrate -m "Création du modèle User"
Appliquer la migration
bash
flask db upgrade
👉 Ces commandes doivent être exécutées dans le dossier flask_project/.

🔄 Workflow Git
Initialisation
bash
git init
git branch -M main
Ignorer les fichiers inutiles
Dans .gitignore :

Code
venv/
__pycache__/
site.db
migrations/
Workflow recommandé
main → branche stable

dev → branche de développement

Commits clairs et atomiques :

bash
git add .
git commit -m "Ajout du modèle User et configuration migrations"
git push origin dev