from passlib import hash


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

def confirm(password, encrypted):
    return hash.atlassian_pbkdf2_sha1.verify(password, encrypted)
