from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
