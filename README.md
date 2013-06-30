RESTedDonkey
============

Instant REST API backend/frontend.
Inside

 * klein/twisted as web framework
 * ZODB as backend object database

Current status: pre ALPHA

Install && run
--------------
 * virtualenv ./env
 * source ./env/bin/activate
 * pip install -r requirements.txt
 * twistd -n web donkey.server.resource

Open

 * http://localhost:8080/\_manager
 
Screenshots
-----------
### Dashboard
![rested donkey dashboard](https://dl.dropboxusercontent.com/u/185133/gh/RESTedDonkey/manager-dashboard.jpg)

### Single resource
![rested donkey resource](https://dl.dropboxusercontent.com/u/185133/gh/RESTedDonkey/manager-resource.jpg)


API
---

Create new resource with template:

    curl -X PUT -d '{"id": "", "name":"", "description":"", "published": false}' http://localhost:8080/products

Add entry to resource:

    curl -X POST -d '{"id": "some_text_id", "name":"some name", "description":"my description", "published": true}' http://localhost:8080/products

Get entries:

    curl -X GET http://localhost:8080/products

Get specific entry:

    curl -X GET http://localhost:8080/products/some_text_id
