from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.user_routes import *  # ✅ Import unique

import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ma_cle_secrete_super_securisee'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ✅ Configurer les logs
logging.basicConfig(
    filename="app.log",        # fichier log
    level=logging.INFO,        # niveau de log
    format="%(asctime)s [%(levelname)s] %(message)s"
)

if __name__ == "__main__":
    app.logger.info("🚀 Démarrage de l'application Flask sur 0.0.0.0:5001")
    app.run(host="0.0.0.0", port=5007, debug=True)
