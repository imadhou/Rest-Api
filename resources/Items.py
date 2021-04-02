from flask_restful import Resource
import DB

class Items(Resource):
    def get(self):
        return {"items": DB.select("items")}

