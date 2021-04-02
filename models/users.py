import DB
class Users:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        request = {"username": username}
        row = DB.select("users", request)
        if row:
            user = cls(*row)
        else:
            user = None
        return user

    @classmethod
    def find_by_id(cls, _id):
        request = {"id": _id}
        row = DB.select("users", request)
        if row:
            user = cls(*row)
        else:
            user = None
        return user
