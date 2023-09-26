RESTedDonkey
============

Instant REST API backend/frontend.
Inside

 * klein/twisted as web framework
 * ZODB as backend object database

Current status: pre ALPHA

Install && run
--------------
 * hatch env create default
 * python server.py

Open

 * http://localhost:8080/\_manager
 
Screenshots
-----------
### Dashboard
![rested donkey dashboard](https://github.com/onjin/RESTedDonkey/assets/44516/a5cbc6fd-1f38-4d42-aad5-30a1a84e1bff)

### Single resource
![rested donkey resource](https://github.com/onjin/RESTedDonkey/assets/44516/6cb6b4b0-ed45-4648-9451-7262d1e40548)


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
