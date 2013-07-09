from twisted.trial import unittest

from donkey.core import resource

from .utils import requestMock, _render


class RestAPITestCase(unittest.TestCase):

    def test_access_inexisting_resource_page(self):
        request = requestMock('/none', 'GET')
        res = resource()
        d = _render(res, request)

        def _cb(result):
            html = request.write.call_args[0][0]
            self.assertTrue('404' in html)

        d.addCallback(_cb)
        return d

    def test_create_resource(self):
        """
        request = requestMock('/products', 'POST', "{'id': 'xxx',\
                              'description': 'desc', 'password': '',\
                              'is_active': false}")
        res = resource()
        d = _render(res, request)

        def _cb(result):
            html = request.write.call_args[0][0]
            self.assertTrue('users' in html)

        d.addCallback(_cb)
        return d
        """
