import unittest

import donkey.server

class ManagerAPITestCase(unittest.TestCase):

    def test_main_page(self):
        c = Client(donkey.core.DonkeyApp, BaseResponse)
        resp = c.get('/')
        resp.status_code
