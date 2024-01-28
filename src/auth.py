import secrets
import sqlite3

def create_db():

    con = sqlite3.connect("excelgpt.db")
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS api_keys (
            ID INTEGER PRIMARY KEY,
            API_KEY TEXT UNIQUE
        )          
''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS admin_keys (
            ID INTEGER PRIMARY KEY,
            ADMIN_KEY TEXT UNIQUE
        )          
''')
    con.commit()
    con.close()

def is_admin_key(adminkey: str):
    con = sqlite3.connect("excelgpt.db")
    cur = con.cursor()
    data = cur.execute('''SELECT ADMIN_KEY FROM admin_keys''').fetchall()
    if adminkey in data[0]: return 1 
    else: 
        con.close()
        return 0

def is_in_db(apikey: str):
    print(apikey)
    con = sqlite3.connect("excelgpt.db")
    cur = con.cursor()
    data = cur.execute('''SELECT API_KEY FROM api_keys''').fetchall()
    print(data)
    for entry in data:
        if apikey in entry: return 1 
    else: 
        con.close()
        return 0

def new_adminkey():
    con = sqlite3.connect("excelgpt.db")
    cur = con.cursor()
    key = create_apikey()
    cur.execute("INSERT INTO admin_keys (ADMIN_KEY) VALUES (?)", (key,))
    con.commit()
    con.close()
    return (key)

def import_apikey():
    con = sqlite3.connect("excelgpt.db")
    cur = con.cursor()
    key = create_apikey()
    print(key)
    cur.execute("INSERT INTO api_keys (API_KEY) VALUES (?)", (key,))
    con.commit()
    con.close()
    return (key)

def create_apikey() -> str:
    new_key = secrets.token_hex(32)
    while is_in_db(new_key): new_key = secrets.token_hex(32)

    return str(new_key)