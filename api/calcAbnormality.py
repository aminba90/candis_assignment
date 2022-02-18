# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource
from models.contacts import Contact
from models.invoices import Invoices
from api.errors import NotFound
import Levenshtein
import numpy as np


class calcAbnormalApi(Resource):
    def post(self) -> Response:
        data = request.get_json()
        output = Contact.objects(organization=data["organization"])
        if len(output)>0:
            requested_name=data['contactName']
            requested_amount=data['amount']        
            conf=[[] for i in range(0,len(output))]
            myContact=0
            for i in range(0,len(output)):
                calc_distance=Levenshtein.distance(requested_name,output[i].name)
                calcConf=(len(requested_name)-calc_distance)/len(requested_name)
                conf[i].append(output[i].name)
                conf[i].append(calcConf)
            max_conf=max(conf, key=lambda x: x[1])
            for j in range(0,len(output)):
                if output[j].name==max_conf[0]:
                    myContact= output[j]._id
            
            invoices=Invoices.objects(contact_id=myContact)
            amount=[]
            for i in range(len(invoices)):
                amount.append(invoices[i].amount.value)
            # Set upper and lower limit to 3 standard deviation
            random_data_std = np.std(amount)
            random_data_mean = np.mean(amount)
            anomaly_cut_off = random_data_std * 3
            
            lower_limit  = random_data_mean - anomaly_cut_off 
            upper_limit = random_data_mean + anomaly_cut_off
            if requested_amount > upper_limit or requested_amount < lower_limit:
                return jsonify({"abnormal": "true"})
            else:
                return jsonify({"abnormal": "false"})
        else:
            return NotFound()