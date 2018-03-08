# -*- coding: utf-8 -*-
import oz
from oz.testing import OzTestCase

from rsearchernlp.handlers import PingHandler


@oz.test
class TestPingHandler(OzTestCase):

    def get_handlers(self):
        return [
            ('/ping', PingHandler)
        ]

    def test_get(self):
        response = self.request('/ping')
        self.assertEqual(response.body, b'pong')
