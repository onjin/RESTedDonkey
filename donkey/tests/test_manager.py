from twisted.trial import unittest

from donkey.core import resource

from .utils import requestMock, _render


class ManagerAPITestCase(unittest.TestCase):

    def test_main_page(self):
        request = requestMock('/_manager/', 'GET')
        res = resource()
        d = _render(res, request)

        def _cb(result):
            html = request.write.call_args[0][0]
            self.assertTrue('>Resources</a>' in html)

        d.addCallback(_cb)
        return d
