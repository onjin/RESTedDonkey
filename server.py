from klein import Klein
from twisted.web.static import File
from storage import Database
from BTrees.OOBTree import OOBTree
import transaction
import json

database = Database('database.fs')


class Donkey(object):
    app = Klein()

    @app.route('/_static', branch=True)
    def static(self, request):
        return File('./static')

    @app.route('/_static/<string:subdir>', branch=True)
    def static_js(self, request, subdir):
        return File('./static/' + subdir)

    @app.route('/_manager/', branch=True)
    def manager_home(self, request):
        """Manager / admin / dashboard"""
        return open('index.html', 'r').read()

    @app.route('/_manager/resources', branch=True)
    @app.route('/_manager/resources/<string:name>.json', branch=True)
    def manager_resources(self, request, name=None):
        """Manager / admin / dashboard"""
        if name and name != '_list':
            result = {'name': name, 'template': database.dbroot[name]['_template']}
        else:
            result = [{'name': key, 'template': database.dbroot[key]['_template']} for key in database.dbroot.keys()]
        return json.dumps(result)

    @app.route('/<string:name>', branch=True, methods=['GET'])
    @app.route('/<string:name>/<string:id>', branch=True, methods=['GET'])
    def api_get(self, request, name, id=None):
        if not name in database.dbroot:
            return json.dumps({'error': 404, 'message': 'item {} not found'.format(name)})

        if id:
            result = database.dbroot[name][id]
        else:
            result = [data for key, data in database.dbroot[name].iteritems() if not key.startswith('_')]

        return json.dumps(result)

    @app.route('/<string:name>', branch=True, methods=['POST'])
    def api_post(self, request, name):
        if not name in database.dbroot:
            return json.dumps({'error': 404, 'message': 'item {} not found'.format(name)})
        data = json.loads(request.content.read())
        database.dbroot[name][data['id']] = parse_data(data, database.dbroot[name]['_template'])
        transaction.commit()
        return "api call {}".format(name)

    @app.route('/<string:name>', branch=True, methods=['PUT'])
    def api_put(self, request, name):
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


if __name__ == '__main__':
    donkey = Donkey()
    donkey.app.run('localhost', 8080)
