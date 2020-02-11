# -*- coding: utf-8 -*-

from flask_sqlalchemy import flask_sqlalchemy
from config import app_config, app_active
from model.Role import Role

config = app_config[app_active]
db = SQLAlchemy(config.APP)


class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime(
        6), onupdate=db.func.current_timestamp(), nullable=False)
    date_created = db.Column(db.DateTime(
        6), onupdate=db.func.current_timestamp(), nullable=True)
    recovery_code = db.Column(db.String(200), nullable=True)
    activate = db.Column(db.Boolean(), default=1, nullable=True)
    role = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)
