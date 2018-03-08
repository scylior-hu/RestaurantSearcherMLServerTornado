# -*- coding: utf-8 -*-
import oz
from oz.testing import OzTestCase
from tornado import escape
import json

from rsearchernlp.handlers.similar_terms import SimilarTermsHandler


@oz.test
class TestSimilarTermsHandler(OzTestCase):

    forced_settings = {
        'allow_jsonp': True
    }

    def get_handlers(self):
        return [
            ('/terms', SimilarTermsHandler)
        ]

    def test_post(self):
        response = self.request(
            '/terms',
            method='POST',
            body=escape.json_encode({'query': '目黒駅の周辺で美味しいカレーが食べたいです'})
        )
        body = escape.json_decode(response.body)
        self.assertEqual(body, {'terms': ['周辺', 'カレー']})
