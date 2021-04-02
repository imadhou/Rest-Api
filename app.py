from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

from resources.Item import Item
from resources.Items import Items
from resources.Users import UserRegiser
# we create an instance of class FLASK and specify the name of the startup module
app = Flask(__name__)

# for security issues and for getting more stronger encryption methods
app.secret_key = "imadhou"

# initialize the main entry of the api with a flask initialization
api = Api(app)

# jwt will create an endpoint /auth that will take a username and a password then using the authenticate
# function it will authenticate the user and get its identity
# this process is applied by the @jwt_required() decorator when the get method is called
# with decorating a function with @jwt_required we must athenticate to be able to performe the action we want
jwt = JWT(app, authenticate, identity)




# with adding a ressource to the api, it will be treated with rest norms (using the functions that we defined
# as implementation of each http-verb
# each resource will be represented by its defined class
api.add_resource(Item, "/item/<string:name>")
api.add_resource(Items, "/items")
api.add_resource(UserRegiser, "/users")
app.run(debug=True)
