"""Defines application options"""

import oz
import os
import sys

from rsearcher.query import *
from rsearcher.word2vec import *
from rsearcher.analyst import *


pardir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
word2vec = Word2VecModel(os.path.join(pardir, 'models/word2vec.gensim.model'))

oz.options(
    # Format: <option name> = dict(<option kwargs>)
    # e.g.: port = dict(type=int, default=8000, help="Server port")
    parser=dict(
        type=QueryParser,
        default=QueryParser(),
        help='QueryParser model'
    ),
    word2vec=dict(
        type=Word2VecModel,
        default=word2vec,
        help='Word2Vec model'
    ),
    analyst=dict(
        type=Analyst,
        default=Analyst(word2vec),
        help='Analyst Model'
    )
)