# -*- coding: utf-8 -*-
from rsearchernlp.middlewares.nlp import NLPMiddleware
from tornado import escape


class SimilarTermsHandler(NLPMiddleware):

    def post(self, *args, **kwargs):
        body = escape.json_decode(self.request.body)
        query = body['query']

        self.parser().drop_morph(query)

        word_pairs = self.word2vec().similar_words(self.parser().words)
        word_pairs = self.word2vec().most_significant_word_pairs(word_pairs)

        terms = [word for word, _ in word_pairs]

        response = {'terms': terms}

        self.write(response)
