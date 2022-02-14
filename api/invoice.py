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
          contact_obj=data['contact']
          contact_id=contact_obj['_id']
          del data["contact"]
          data['contact_id']=contact_id
          post_user = Invoices(**data).save()
          post_contact= Contact(**contact_obj).save()
          return jsonify(post_user,post_contact)
          
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