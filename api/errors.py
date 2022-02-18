# flask packages
from flask import Response, jsonify


def invalid_route() -> Response:
    output = {"error":
              {"msg": "404 error: This route is currently not supported. See API documentation."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp

def NotFound() -> Response:
    output = {"error":
              {"msg": "The information which you provided does not exist in our DB"}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp