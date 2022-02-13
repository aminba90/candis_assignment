# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource
from models.contacts import Contact
from models.invoices import Invoices


class InvoicesApi(Resource):
    def get(self) -> Response:
        output = Invoices.objects()
        return jsonify({'result': output})

    def post(self) -> Response:
          data = request.get_json()
          contact_id=data['contact_id']
          dbobj = Contact.objects(_id=str(contact_id)).first()
          del data["contact_id"]
          data['contact'] = list(dbobj)
          post_user = Invoices(**data).save()
          return jsonify(data)

class InvoiceApi(Resource):
    
    def get(self, id: str) -> Response:
        output = Invoices.objects.get(_id=id)
        return jsonify({'result': output})

    def put(self, id: str) -> Response:
       
        data = request.get_json()
        put_user = Invoices.objects(_id=id).update(**data)
        return jsonify({'result': put_user})

    def delete(self, id: str) -> Response:
        output = Invoices.objects(_id=id).delete()
        return jsonify({'result': output})