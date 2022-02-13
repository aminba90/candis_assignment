# mongo-engine packages
from pydoc import Doc
from mongoengine import Document, StringField, EmbeddedDocument


class Contact(Document):

    _id = StringField(required=True,primary_key=True)
    iban= StringField()
    name= StringField()
    organization= StringField()