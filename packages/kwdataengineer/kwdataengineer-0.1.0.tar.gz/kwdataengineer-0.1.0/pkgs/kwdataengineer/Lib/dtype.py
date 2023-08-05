# -*- coding: utf-8 -*-
from datetime import datetime

from ipylib.idebug import *

from dataengineer.models import *


__all__ = [
    'WordDtypeAssigner',
]

class WordDtypeAssignerV1:

    @classmethod
    def assign(self, modelName, column):
        model = Collection(modelName)
        WordDtype = Collection('WordDtypeBK')
        # 일단 dtype 컬럼만 드랍
        model.update_many({}, {'$unset':{'dtype':''}})
        # 단계1: 수동으로 정한 룰(오름차순으로)을 적용
        cursor = WordDtype.find(None, {'_id':0}).sort('order', ASCENDING)
        for d in list(cursor):
            order, dtype, pat = d['order'], d['dtype'], "|".join(d['regex'])
            # print(order, dtype, pat)
            filter = {'dtype':None, column:{'$regex':pat}}
            model.update_many(filter, {'$set':{'dtype':dtype}})

        # 단계2: 룰 적용을 받지않은 예상하지 못한 것들은 모두 문자열로 일괄 업데이트
        model.update_many({'dtype':None}, {'$set':{'dtype':'str'}})

        logger.info(f'{self} | Done. collName: {model.collName}')

class WordDtypeAssigner:

    @classmethod
    def assign(self, modelName, column):
        model = Collection(modelName)
        WordDtype = Collection('WordDtype')
        # dtype 컬럼만 드랍
        model.update_many({}, {'$unset':{'dtype':''}})
        # 단계1: WordDtype의 Rule을 적용
        nos = sorted(WordDtype.distinct('seq'))
        for seq in nos:
            f = {'seq':seq}
            dtype = WordDtype.distinct('dtype', f)[0]
            pats = WordDtype.distinct('pat', f)
            regex = "|".join(pats)
            # print(seq, dtype, pats)
            filter = {'dtype':None, column:{'$regex':regex}}
            model.update_many(filter, {'$set':{'dtype':dtype}})

        # 단계2: 룰 적용을 받지않은 예상하지 못한 것들은 모두 문자열로 일괄 업데이트
        model.update_many({'dtype':None}, {'$set':{'dtype':'str'}})
    @classmethod
    @ctracer
    def State(self, *args): pass
