"""Defines application routes"""

import oz

from .handlers.ping import *
from .handlers.similar_terms import *
from .handlers.score import *

oz.routes(
    (r'^/ping$', PingHandler),
    (r'^/terms$', SimilarTermsHandler),
    (r'^/scores$', ScoreHandler)
    # Format: (<path>, <handler>, [dict(<request handler kwargs>)])
    # e.g.: (r"^/hello/(\w+)$", handlers.GreetingHandler)
)