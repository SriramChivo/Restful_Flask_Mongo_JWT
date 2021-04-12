from flask_restful import Resource, Api

from flask import jsonify,request

from models import User,Template

from flask_jwt_extended import JWTManager

from flask_jwt_extended import (create_access_token, 
                                jwt_required,
                                 get_jwt_identity)

from initial_setup import app

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

jwt = JWTManager(app)

class Userregister(Resource):
    def post(self):
        get_data=(request.data).decode('utf-8')
        import json
        data_dict=json.loads(get_data)
        username_data=data_dict["username"]
        password_data=data_dict["password"]
        email_data=data_dict["email"]
        user_registered=User(email=email_data,UserName=username_data,Password=password_data)
        user_registered.save()
        access_token = create_access_token(identity = username_data)
        return access_token

class Getusers(Resource):
    def get(self):
        get_data=User.objects.all()
        print(get_data)
        return jsonify(get_data)
    
class Userlogin(Resource):
    
    def post(self):
        get_data=(request.data).decode('utf-8')
        import json
        data_dict=json.loads(get_data)
        username_data=data_dict["username"]
        password_data=data_dict["password"]
        access_token = create_access_token(identity = username_data)
        return access_token

class Newtemplate(Resource):
    @jwt_required()
    def post(self):
        get_data=(request.data).decode('utf-8')
        import json
        data_dict=json.loads(get_data)
        template_name_data=data_dict["template_name"]
        subject_data=data_dict["subject"]
        body_data=data_dict["body"]
        template_registered=Template(template_name=template_name_data,subject=subject_data,body=body_data)
        template_registered.save()
        return "Template Insertion Successfully.."

class Getalltemplate(Resource):
    @jwt_required()
    def get(self):
        get_data=Template.objects.all()
        return jsonify(get_data)

class singletemplate(Resource):
    @jwt_required()
    def get(self,template_data: str):
        template_data=Template.objects(template_name=template_data).first()
        return jsonify(template_data)

class Deletetemplate(Resource):
    @jwt_required()
    def post(self,template_data: str):
        template_data=Template.objects(template_name=template_data).first()
        template_data.delete()
        return "Deleted SuccessFully...!"
        
