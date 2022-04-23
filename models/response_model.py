from mongoengine import BooleanField, ReferenceField, Document, ListField, StringField, DateTimeField
from datetime import datetime

from models.tag_model import Tag


class Response(Document):
    title = StringField(required=True, max_length=30)
    content = StringField(required=True, max_length=300)
    tag_ids = ListField(ReferenceField(Tag, dbref=False))
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    deleted = BooleanField(default=False)
    deleted_at = DateTimeField(default=None)
