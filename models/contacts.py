# mongo-engine packages
from mongoengine import Document, StringField


class Contact(Document):

    _id = StringField(required=True,primary_key=True)
    iban= StringField()
    name= StringField()
    organization= StringField()