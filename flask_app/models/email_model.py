from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM emails;'
        allEmails = connectToMySQL('email_db').query_db(query)
        emails=[]
        for user in allEmails:
            emails.append(cls(user))
        return emails

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW() );'
        return connectToMySQL('email_db').query_db(query, data)

    @classmethod
    def get_last(cls):
        query = 'SELECT * FROM emails ORDER BY id DESC LIMIT 1;'
        result =  connectToMySQL('email_db').query_db(query)
        return cls(result[0])

    @classmethod
    def deleteThis(cls,data):
        query = 'DELETE FROM emails WHERE id = %(id)s;'
        return connectToMySQL('email_db').query_db(query,data)

    @staticmethod
    def validate_user ( user ):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!')
            is_valid =False
        return is_valid