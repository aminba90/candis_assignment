# flask packages
from flask_restful import Api


# project resources

from api.invoice import InvoicesApi, InvoiceApi
from api.contact import ContactsApi, ContactApi
from api.calcConf import calcConfApi



def create_routes(api: Api):
    """Adds resources to the api.

    :param api: Flask-RESTful Api Object

    :Example:

        api.add_resource(HelloWorld, '/', '/hello')
        api.add_resource(Foo, '/foo', endpoint="foo")
        api.add_resource(FooSpecial, '/special/foo', endpoint="foo")

    """

    api.add_resource(InvoicesApi, '/invoice/')
    api.add_resource(InvoiceApi, '/invoice/<id>')
    api.add_resource(ContactsApi, '/contact/')
    api.add_resource(ContactApi, '/contact/<id>')
    api.add_resource(calcConfApi, '/conf/')
  #  api.add_resource(MealApi, '/meal/<meal_id>')
