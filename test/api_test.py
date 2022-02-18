import unittest
import requests


class ApiTest(unittest.TestCase):
    API_URL="http://localhost:5000"
    INVOICE_URL="{}/invoice".format(API_URL)
    CONTACT_URL="{}/contact".format(API_URL)
    CONF_URL="{}/conf/".format(API_URL)
    ABNORMAL_URL="{}/abnormal/".format(API_URL)
    INVOICE_INSERTED_OBJ={
                    "_id": "98988989898", 
                    "organization": "candis", 
                    "createdAt": "2021-10-11T09:53:31.339Z", 
                    "updatedAt": "2021-11-29T13:15:19.500Z", 
                    "amount": {
                    "currencyCode": "EUR", 
                    "value": 80 
                    },
                    "contact": {
                    "_id": "43666578", 
                    "iban": "DE88100500001310032358", 
                    "name": "Amin", 
                    "organization": "Candis"
                    },
                    "invoiceDate": "2021-10-11T00:00:00.000Z",
                    "invoiceId": "VR33210230898"
                    }
                          
    INVOICE_OBJ= {
    "result": {
        "_id": "98988989898",
        "amount": {
            "currencyCode": "EUR",
            "value": 80.0
        },
        "contact_id": "43666578",
        "createdAt": {
            "$date": 1633910400000
        },
        "invoiceDate": {
            "$date": 1633910400000
        },
        "invoiceId": "VR33210230898",
        "organization": "candis",
        "updatedAt": {
            "$date": 1638144000000
        }
    }
}
    NEW_CONTACT_OBJ={
                    "_id": "43666578",
                    "iban": "DE88100500001310032358",
                    "name": "Aminb",
                    "organization": "Candis_new"
                    }
    RESULT_CONTACT_OBJ={
                    "result": {
                    "_id": "43666578",
                    "iban": "DE88100500001310032358",
                    "name": "Aminb",
                    "organization": "Candis_new"
                        }
                                    }
    CALC_CONF_OBJ={
                    "organization": "brtech", 
                    "contactName": "amir" 
                                }
    CALC_CONF_EXPECTED_VAL={
                             "confidence": 1.0,
                             "suggestedContact": "amir"
                            }

    CALC_ABNORMAL_OBJ={
            "contactName": "Sarah",
            "organization": "Candis",
            "amount" : 800
        }

    CALC_ABNORMAL_EXPECTED_VAL={
                     "abnormal": "true"
                                }


    #POST request to /API/invoice to create a new invoice
    def test1_create_new_invoice(self):
        r=requests.post(ApiTest.INVOICE_URL+"/",json=ApiTest.INVOICE_INSERTED_OBJ)
        self.assertEqual(r.status_code,200)

    #GET request for selecting newly created invoice
    def test2_get_new_invoice(self):
        id=98988989898
        r=requests.get("{}/{}".format(ApiTest.INVOICE_URL,id))
        self.assertEqual(r.status_code,200)
        self.assertDictEqual(r.json(),ApiTest.INVOICE_OBJ)

    #PUT request to updated existing contact
    def test3_update_contact(self):
        id=43666578
        r=requests.put("{}/{}".format(ApiTest.CONTACT_URL,id),json=ApiTest.NEW_CONTACT_OBJ)
        self.assertEqual(r.status_code,200)
    
    #GET request for checking updated contact
    def test4_get_new_contact_After_update(self):
        id=43666578
        r=requests.get("{}/{}".format(ApiTest.CONTACT_URL,id))
        self.assertEqual(r.status_code,200)
        self.assertDictEqual(r.json(),ApiTest.RESULT_CONTACT_OBJ)

    #POST request for checking confidence calculator service functionality

    def test5_calc_Conf(self):
        r=requests.post(ApiTest.CONF_URL,json=ApiTest.CALC_CONF_OBJ)
        self.assertEqual(r.status_code,200)
        self.assertDictEqual(r.json(),ApiTest.CALC_CONF_EXPECTED_VAL)

    def test6_calc_Abnormality(self):
        r=requests.post(ApiTest.ABNORMAL_URL,json=ApiTest.CALC_ABNORMAL_OBJ)
        self.assertEqual(r.status_code,200)
        self.assertDictEqual(r.json(),ApiTest.CALC_ABNORMAL_EXPECTED_VAL)

    
