from passlib import hash
import sqlite3

DB = sqlite3.connect('static/database/sql.db', check_same_thread=False)
cursor = DB.cursor()


def select(table, condition='', what='*'):
    sql = f"""SELECT {what} FROM {table} {condition}"""
    try:
        result = cursor.execute(sql).fetchall()
    except Exception as err:
        print(sql)
        result = str(err)
    finally:
        return result


def insert():
    pass


def update():
    pass


def delete():
    pass


def replacer(statement, old, new):
    return statement.replace(old, new)


def checkEmpty(array):
    empty = False
    for item in array:
        if not item:
            empty = True
    return empty


def password(word):
    return hash.atlassian_pbkdf2_sha1.encrypt(word.strip())


def verify(password, encrypted):
    return hash.atlassian_pbkdf2_sha1.verify(password, encrypted)
