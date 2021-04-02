from flask_restful import Resource, reqparse
from models.users import Users as u
import DB


class UserRegiser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    def post(self):
        posted_data = UserRegiser.parser.parse_args()
        print(posted_data)
        user = u.find_by_username(posted_data["username"])
        if user is None:
            DB.insert("users", {"username": posted_data["username"], "password": posted_data["password"]})
            return {"message": "user created with success"}
        return {"message": "username already exists please choose another one"}

