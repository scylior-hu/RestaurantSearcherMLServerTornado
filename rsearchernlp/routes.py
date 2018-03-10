"""Defines application routes"""

import oz

from .handlers.ping import *
from .handlers.similar_terms import *
from .handlers.parse import *

oz.routes(
    (r'^/ping$', PingHandler),
    (r'^/terms$', SimilarTermsHandler),
    (r'^/parse$', KNPParseHandler)
    # Format: (<path>, <handler>, [dict(<request handler kwargs>)])
    # e.g.: (r"^/hello/(\w+)$", handlers.GreetingHandler)
)