from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.user_routes import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ma_cle_secrete_super_securisee'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importer les routes
from routes.user_routes import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

