import os

from klein import route, resource
from twisted.web.static import File
from twisted.web.resource import NoResource
from .storage import Database

from BTrees.OOBTree import OOBTree
import transaction
import json

resource
database = Database('zodb.conf')

STATIC_DIR = os.path.join(os.path.dirname(__file__), '..', 'static')


@route('/', branch=False)
def api_home(request):
    return NoResource()


@route('/_static', branch=True)
def static(request):
    return File(STATIC_DIR)


@route('/_static/<string:subdir>', branch=True)
def static_js(request, subdir):
    return File(os.path.join(STATIC_DIR, subdir))


@route('/_manager/')
def manager_home(request):
    """Manager / admin / dashboard"""
    return open(os.path.join(STATIC_DIR, 'index.html'), 'r').read()


@route('/_manager/resources', branch=True)
@route('/_manager/resources/<string:name>', branch=True)
def manager_resources(request, name=None):
    """Manager / admin / dashboard"""
    if name:
        result = {'name': name, 'template': database.dbroot[name]['_template']}
    else:
        result = [{'name': key, 'template': database.dbroot[key]['_template']}
                  for key in database.dbroot.keys()]
    return json.dumps(result)


@route('/<string:name>', branch=True, methods=['GET'])
@route('/<string:name>/<string:id>', branch=True, methods=['GET'])
def api_get(request, name, id=None):
    if not name in database.dbroot:
        return NoResource('item {} not found'.format(name))

    if id:
        result = parse_data(database.dbroot[name][id],
                            database.dbroot[name]['_template'])
    else:
        result = [parse_data(data, database.dbroot[name]['_template'])
                  for key, data in database.dbroot[name].iteritems()
                  if not key.startswith('_')]

    return json.dumps(result)


@route('/<string:name>', branch=True, methods=['POST'])
def api_post(request, name):
    if not name in database.dbroot:
        return NoResource('item {} not found'.format(name))

    data = json.loads(request.content.read())
    database.dbroot[name][data['id']] = parse_data(
        data,
        database.dbroot[name]['_template'])
    transaction.commit()
    return "api call {}".format(name)


@route('/<string:name>', branch=True, methods=['PUT'])
def api_put(request, name):
    data = json.loads(request.content.read())
    database.dbroot[name] = OOBTree()
    database.dbroot[name]['_template'] = data
    transaction.commit()
    return "template saved"


def parse_data(data, template):
    result = {}
    for key, default in template.iteritems():
        try:
            result[key] = data[key]
        except KeyError:
            result[key] = default

    return result
