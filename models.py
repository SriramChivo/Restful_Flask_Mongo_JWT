# from app import 

from initial_setup import db


class User(db.Document):
    email = db.StringField(required=True)
    UserName = db.StringField(max_length=50,unique=True,required=True)
    Password = db.StringField(max_length=50,required=True)

class Template(db.Document):
    template_name = db.StringField(max_length=120, required=True,unique=True)
    subject=db.StringField(max_length=120,required=True)
    body=db.StringField(max_length=120,required=True)