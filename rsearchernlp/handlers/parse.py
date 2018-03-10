# -*- coding: utf-8 -*-
from rsearchernlp.middlewares.nlp import NLPMiddleware
from tornado import escape


class KNPParseHandler(NLPMiddleware):

    def post(self, *args, **kwargs):
        review = escape.json_decode(self.request.body)

        assert 'id' in review
        assert 'body' in review

        candidates, morphs = self.analyst().parse(review['body'])

        response = {
            'candidates': candidates,
            'morphs': morphs
        }

        self.write(response)
