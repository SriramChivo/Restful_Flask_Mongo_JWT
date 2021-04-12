from flask import Flask

from flask_mongoengine import MongoEngine

from flask_restful import Resource, Api

from initial_setup import app

import Api_requests

api = Api(app)

api.add_resource(Api_requests.Userregister, '/all/')

api.add_resource(Api_requests.Getusers, '/getusers/')

api.add_resource(Api_requests.Userlogin, '/userlogin/')

api.add_resource(Api_requests.Newtemplate, '/newtemp/')

api.add_resource(Api_requests.Getalltemplate, '/getalltemp/')

api.add_resource(Api_requests.singletemplate, '/getsingletemp/<template_data>/')

api.add_resource(Api_requests.Deletetemplate, '/deletetemp/<template_data>/')

@app.route("/")
def home():
    return "Hi All..."

if __name__=="__main__":
    app.run(debug=True)