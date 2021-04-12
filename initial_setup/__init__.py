from flask import Flask

from flask_mongoengine import MongoEngine

from flask_restful import Resource, Api

db = MongoEngine()

app=Flask(__name__)

db.init_app(app)