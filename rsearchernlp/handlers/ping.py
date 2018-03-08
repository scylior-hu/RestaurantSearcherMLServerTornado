# -*- coding: utf-8 -*-
from oz import RequestHandler
from oz.json_api import ApiMiddleware


class PingHandler(RequestHandler, ApiMiddleware):

    def get(self, *args, **kwargs):
        self.write('pong')
