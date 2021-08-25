from passlib import hash
import sqlite3, string, random

from datetime import datetime

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


def db_insert(table, column, data):
    sql = f"""INSERT INTO {table} ({column}) VALUES ({data})"""
    try:
        cursor.execute(sql)
        DB.commit()
        DB.close()
        msg = 'ok'
    except Exception as err:
        print("SQL CODE: ", sql)
        print("Insertion Error: ", err)
        msg = 'Error While Saving. Contact Admin'
    finally:
        return msg


def db_update(table, update, condition):
    sql = f"UPDATE {table} SET {update} {condition}"
    try:
        cursor.execute(sql)
        DB.commit()
        DB.close()
        msg = 'ok'
    except Exception as err:
        print("SQL CODE: ", sql)
        print("Updating Error: ", err)
        msg = 'Error While Updating. Contact Admin'
    finally:
        return msg


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


def gen_string(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
