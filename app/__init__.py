from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__, instance_relative_config=True)

from . import views

app.config.from_object('config')

db = MongoEngine(app)
