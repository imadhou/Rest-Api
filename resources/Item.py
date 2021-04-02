from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
import DB


class Item(Resource):
    # the parser parses the data within the body of the post method
    # we shall add each expected parameter to the parser
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="Cannot be blank")

    @jwt_required()
    def get(self, name):
        item = DB.select("items", {"name": name})
        return {"item": {"id": item[0], "name": item[1], "price": item[2]}} if item else 404, "Item not found"

    def post(self, name):

        # we use a request parser that will check in the payload if the parameters specified in the
        # parser exist then it will return them it will ignore the presence of data not specified
        # by the parser

        item = DB.select("items", {"name": name})
        if item:
            return {"item": "already exists"}, 400

        # we parse the arguments specified in the parser which are in the payload of post
        posted_data = Item.parser.parse_args()
        item = {"name": name, "price": posted_data["price"]}
        DB.insert("items", item)
        return item, 201

    def delete(self, name):
        DB.delete("items", {"name": name})
        return {"message": "item " + name + " is deleted"}

    def put(self, name):

        global parser
        parser.add_argument('id', type=int, required=True, help="Cannot be blank")
        # we are looking for the data specified in the parser within the the posted payload
        posted_data = Item.parser.parse_args()
        item = DB.select("items", {"id": posted_data['id']})
        print(item)
        if item is None:
            item = {"name": name, "price": posted_data["price"]}
            DB.insert("items", item)
        else:
            item = {"name": name, "price": posted_data["price"]}
            DB.update("items", posted_data['id'], item)
        return item
