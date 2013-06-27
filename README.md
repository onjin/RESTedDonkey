RESTedDonkey
============

Instant REST API backend/frontend.
Inside

 * klein/twisted as web framework
 * ZODB as backend object database

Current status: pre ALPHA

Install && run
--------------
 * virtualenv .
 * source ./bin/activate
 * pip install -r requirements.txt
 * python server.py

Open

 * http://localhost:8080/\_manager

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
