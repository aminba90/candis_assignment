# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource

# mongo-engine models
from models.contacts import Contact

class ContactsApi(Resource):
    def get(self) -> Response:
        output = Contact.objects()
        return jsonify({'result': output})

    def post(self) -> Response:
          data = request.get_json()
          post_user = Contact(**data).save()
          return jsonify({'result': post_user})

class ContactApi(Resource):
    
    def get(self, id: str) -> Response:
        output = Contact.objects.get(_id=id)
        return jsonify({'result': output})

    def put(self, id: str) -> Response:
       
        data = request.get_json()
        put_user = Contact.objects(_id=id).update(**data)
        return jsonify({'result': put_user})

    def delete(self, id: str) -> Response:
        output = Contact.objects(_id=id).delete()
        return jsonify({'result': output})

