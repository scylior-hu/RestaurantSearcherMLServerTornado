# -*- coding: utf-8 -*-
import oz
from oz.testing import OzTestCase
from tornado import escape
import json

from rsearchernlp.handlers.parse import KNPParseHandler


@oz.test
class TestKNPParseHandler(OzTestCase):

    forced_settings = {
        'allow_jsonp': True
    }

    def get_handlers(self):
        return [
            ('/parse', KNPParseHandler)
        ]

    def test_post(self):
        response = self.request(
            '/parse',
            method='POST',
            body=escape.json_encode(
                {
                    'id': 0,
                    'body': '智に働けば角が立つ。情に棹させば流される。'
                }
            )
        )

        body = escape.json_decode(response.body)
        excepted = {
            'candidates': ['智に働けば角が立つ', '情に棹させば流される'],
            'morphs': [[[], []], [['情', '棹'], ['さ']]]
        }

        self.assertEqual(body, excepted)

#                         'body': '''
#                         名前は忘れましたが、札幌で食べたお店よりも、全然こっちの方が美味しかったので、載せました。お店も綺麗（新規オープン・・）でランチは結構混んでいます。個人的にはゆったりと食事
# できるので夜の方がオススメです。  辛さが０倍から５０倍まで選べるのもＧＯＯＤ！、スープも２種類みたいで、友達は黄色がオススメと言っていましたが、自分は赤の方を食べました。かなり美味しかったです。店長も好感のも
# てるお兄さんでした。  駅近くなので一度お試しあれです！
#                         '''