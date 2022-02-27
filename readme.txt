***Follow this instruction to install and run Restful service for my take-home assignment***

Prerequisites:
1- installing docker: 
To gain complete functionality of this application, docker needs to be installed and operated to be able to run provided docker-compose file.
2- Install postman for invoking Restful endpoints. You can follow below steps:
    • sudo apt install snapd
    • sudo snap install postman

Installation:
1- after pulling entire project files, you can start all services including Mongod and our Restful service using “docker-compose up -d” which leads to installing and deploying all dependencies and required services.

APIs:
1- selecting invoice documents:
in this step, a Restful API has been implemented for selecting all invoices from invoice collection. This is a get method which can be invoked from http://localhost:5000/invoice/
2-loading invoice documents:
in this step, a Restful API has been implemented for inserting single or multiple invoice documents in invoice collection. This is a post method that can be invoked from http://localhost:5000/invoice.
As per our default assumption, contact details are included within the invoice JSON document and this information got updated almost frequently (1:30) in comparison to invoice details. So I decided to segregate invoice and contact collection to handle this issue (using reference structure instead of embedding). So I added the id of contact into invoice collection and store it as a “contact_id” and when this get method is invoked, contact information is also inserted into contact collection simultaneously. 
3-updating contract documents:
an endpoint has been developed for handling updates for contact information based on the id key in contact. There is a put method for this task and can be invoked from http://localhost:5000/contact/<_id>
4- calculating contact name confidence:
as requested in the assignment, an endpoint for Suggesting the invoice contact based on previous invoices and its confidence has to be developed. It can be invoked with the post method from http://localhost:5000/conf/.
5- calculating invoice amount abnormality:
as requested in the assignment, an endpoint for Indicating an abnormal amount for one invoice has to be developed that can be invoked with post method from http://localhost:5000/abnormal/

TEST CASE:
To do the unit test on our Restful methods, a class called “API_TEST”  in /test/api_test.py has been created. There are multiple functions that each of them will do a unit test on our developed endpoints.