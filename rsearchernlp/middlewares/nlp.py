# -*- coding: utf-8 -*-
import oz
from oz import RequestHandler
from oz.json_api import ApiMiddleware
from rsearcher.query import QueryParser
from rsearcher.word2vec import Word2VecModel
from rsearcher.analyst import Analyst


class NLPMiddleware(RequestHandler, ApiMiddleware):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.trigger_listener('prepare', self._on_parser_prepare)

    def parser(self):
        return self._parser

    def word2vec(self):
        return self._word2vec

    def analyst(self):
        return self._analyst

    def _on_parser_prepare(self):
        self._parser = oz.settings['parser']
        self._word2vec = oz.settings['word2vec']
        self._analyst = oz.settings['analyst']
