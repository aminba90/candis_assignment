# flask packages
import json
from operator import contains
from flask import jsonify, Response, request
from flask_restful import Resource
from models.contacts import Contact
import Levenshtein
from api.errors import NotFound


class calcConfApi(Resource):
    def post(self) -> Response:
        data = request.get_json()
        output = Contact.objects(organization=data["organization"])
        if len(output)>0:
            requested_name=data['contactName']        
            conf=[[] for i in range(0,len(output))]
            for i in range(0,len(output)):
                calc_distance=Levenshtein.distance(requested_name,output[i].name)
                calcConf=(len(requested_name)-calc_distance)/len(requested_name)
                conf[i].append(output[i].name)
                conf[i].append(calcConf)
            max_conf=max(conf, key=lambda x: x[1])
            return jsonify({'suggestedContact': max_conf[0] ,
                            "confidence": max_conf[1]})
        else:
            return NotFound()