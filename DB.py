import sqlite3


def create_table(table, fields={}):
    con = sqlite3.connect("MydataBase.db")
    if len(fields) == 0:
        raise ValueError("fields must be a valid dictionary")
        # {name : text, age : int}
        return -1
    curs = con.cursor()
    params = ""
    for a in fields.keys():
        params += a + " " + fields[a] + ","
    params = params.rstrip(",")
    req = F"CREATE TABLE IF NOT EXISTS {table} ({params})"
    curs.execute(req)
    con.commit()
    con.close()


def insert(table, values={}):
    con = sqlite3.connect("MydataBase.db")
    req = f'INSERT INTO "{table}" ('
    vals = ""
    Evals = []
    for i in values.keys():
        req += i + ", "
        vals += " ?, "
        Evals.append(values.get(i))
    req = req.rstrip(", ")
    vals = vals.rstrip(", ")
    req += f") VALUES({vals} )"
    print(req)
    cursor = con.cursor()
    cursor.execute(req, Evals)
    con.commit()
    con.close()


def select(table, condition={}):
    con = sqlite3.connect("MydataBase.db")
    if len(condition) == 0:
        req = f"SELECT * FROM {table}"
        print(req)
    else:
        req = f'SELECT * FROM "{table}" WHERE '
        values = []
        for key in condition.keys():
            req += key + " = ? AND "
            values.append(condition.get(key))
        req = req.rstrip("AND ")
        print(req)

    cursor = con.cursor()
    if len(condition) == 0:
        cursor.execute(req)
        items = cursor.fetchall()
    else:
        cursor.execute(req, values)
        items = cursor.fetchone()
    con.close()
    return items


def update(table, id, nValues={}):
    con = sqlite3.connect("MydataBase.db")
    req = f'UPDATE {table} SET '
    values = []
    for key in nValues.keys():
        req += key + " = ? , "
        values.append(nValues.get(key))
    req = req.rstrip(", ")
    req += f' WHERE id = {id}'
    print(req)

    print(req)
    cursor = con.cursor()
    cursor.execute(req, values)
    con.commit()
    con.close()


def delete(table, conditions={}):
    con = sqlite3.connect("MydataBase.db")
    req = f'DELETE FROM {table} WHERE '
    values = []
    for key in conditions.keys():
        req += key + " = ? AND"
        values.append(conditions.get(key))
    req = req.rstrip("AND")
    print(req)
    cursor = con.cursor()
    cursor.execute(req, values)
    con.commit()
    con.close()

# create_table("users", {"id": "INTEGER PRIMARY KEY", "username": "text", "password": "text"})
# users = [
#     {"username": "imadhou", "password": "abcd1234"},
#     {"username": "raouf", "password": "hjhj4514"},
#     {"username": "hicham","password": "adsz6542"},
#     {"username": "anas","password": "ahdi9875"}
# ]

# insert("users", {"id": 1, "username": "bouhwassou", "password": "azse522"})
# for user in users:
#     insert("users", user)
# for a in select("users", {"id": 1}):
#     print(a)
#
# create_table("items",{"id ": "INTEGER PRIMARY KEY", "name": "text", "price": "int"})

# insert("items", {"id": 1, "name": "tv", "price": 20})
# items = [
#     {"name": "tv","price": 12},
#     {"name": "phone","price":  20},
#     {"name": "pc","price":  40}
# ]
#
# for item in items:
#     insert("items", item)
