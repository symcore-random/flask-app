from mongoengine import Document, StringField, DateTimeField, BooleanField
from datetime import datetime


class Tag(Document):
    tag = StringField(required=True, max_length=30)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    deleted = BooleanField(default=False)
    deleted_at = DateTimeField(default=None)
