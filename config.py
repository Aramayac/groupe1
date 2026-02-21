import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "ma_cle_secrete_super_securisee")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
