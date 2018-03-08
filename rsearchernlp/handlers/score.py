# -*- coding: utf-8 -*-
from rsearchernlp.middlewares.nlp import NLPMiddleware
from tornado import escape
import numpy as np


class ScoreHandler(NLPMiddleware):

    def post(self, *args, **kwargs):
        body = escape.json_decode(self.request.body)

        reviews = body['reviews']
        query_words = body['query_words']

        assert 'id' in reviews[0]
        assert 'body' in reviews[0]

        relevant_reviews = []   # 提示すべきお店の情報 (Elasticのid, 口コミbodyを含む)
        # relevant_reviews[0] -> 最も推薦すべきお店の情報
        candidates = []         # 候補となるお店の口コミ一覧 (relevant_reviews に対応)
        # candidates[0] -> 最も推薦すべきお店の口コミが最大3件入ったリスト
        # candidates[1] -> 次に推薦すべきお店の口コミが最大3件入ったリスト

        all_sum_scores = []
        all_scores = []
        all_candidates = []

        for review in reviews[0:1]:
            self.analyst().parse(review['body'])
            candidate_scores = np.array(self.analyst().calc_candidate_score())
            query_base_scores = np.array(self.analyst().calc_query_base_score(query_words))

            scores = list(candidate_scores + query_base_scores)

            all_sum_scores.append(sum(scores) / (len(scores) if len(scores) != 0 else 1))
            all_scores.append(scores)
            all_candidates.append(self.analyst().candidates)

        indices = np.argsort(all_sum_scores)[::-1]

        for index in indices:
            relevant_reviews.append(reviews[index])
            candidates_ = self.analyst().most_significant_candidates(
                all_scores[index],
                all_candidates[index]
            )

            candidates.append(candidates_)

        response = {
            'reviews': relevant_reviews,
            'candidates': candidates
        }

        self.write(response)
