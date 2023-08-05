# -*- coding: utf-8 -*-
import re

from bson.objectid import ObjectId

from ipylib.idebug import *
from ipylib.idatetime import DatetimeParser, timedelta, datetime
import trddt

from dataengineer import models
from dataengineer import base


__all__ = [
    'AutoFilter',
    'FidFilter','FidProjection','FidTranslator',
]

def lastdt(model):
    li = model.distinct('dt')
    if len(li) > 0:
        t = sorted(li)[-1]
        return t.astimezone()
    else: pass

class AutoFilter(base.BaseClass):

    def __init__(self, modelName):
        self.schema = models.SchemaModel(modelName)
        self.filter = {}
        # CollectionColumns
        self.collcols = list(set(self.schema.distinct('column') + ['_id']))
        self.strcols = self.schema.distinct('column', {'dtype':'str'})
        self.dtcols = self.schema.dtcols
        self.boolcols = self.schema.distinct('column', {'dtype':'boolean'})

    def clear(self):
        self.filter.clear()
        return self
    def _autoclean(self, f):
        # 스키마컬럼에 없는 필터조건을 제거한다
        return {c:f[c] for c in self.collcols if c in f}
    def _set(self, f):
        f = self._autoclean(f)
        self.clear()
        self.filter.update(f)
        return self
    def search(self, filter):
        # MongoDB 검색 오퍼레이션을 최대한 사용하라.
        # 데이타 타입 자동변환만 사용하되, ipylib 를 먼저 활용하라
        # -> 더 직관적이고, MongoDB 를 더 잘 이해할 수 있다
        f = {} if filter is None else filter
        return self._set(f)

    """불필요한 기능같다?"""
    def today(self):
        self.clear()
        t = datetime.today().astimezone()
        t = t.replace(hour=0, minute=0, second=0, microsecond=0)
        filters = []
        for c in self.dtcols:
            filters.append({c:{'$gte':t}})
        if len(filters) > 0:
            self.filter.update({'$or':filters})
        return self
    def oneday(self, **kw):
        self.clear()
        for k,v in kw.items():
            if k in self.dtcols:
                fromdt = self.schema.parse_value(k, v)
                todt = fromdt + timedelta(days=+1)
                self.filter.update({k:{'$gte':fromdt, '$lt':todt}})
        return self
    def period(self, fromdt, todt):
        self.clear()
        fromdt = DatetimeParser(fromdt)
        todt = DatetimeParser(todt)
        filters = []
        for c in self.dtcols:
            filters.append({c:{'$gte':fromdt, '$lt':todt}})
        if len(filters) > 0:
            self.filter.update({'$or':filters})
        return self
    def lastday(self):
        self.clear()
        filters = []
        for c in self.dtcols:
            filters.append({c:{'$gte':datetime.today().astimezone()}})
        if len(filters) > 0:
            self.filter.update({'$or':filters})
        return self

class AutoFilterV2(dict):

    def oneday(self, **kw):
        for k,v in kw.items():
            t1 = trddt.tradeday(v)
            t2 = t1 + timedelta(days=1)
            self.update({k:{'$gte':t1, '$lt':t2}})
    def period(self, k, t1, t2):
        t1 = DatetimeParser(t1)
        t2 = DatetimeParser(t2)
        self.update({k:{'$gte':t1, '$lte':t2}})

class FidTranslator:
    # 컬럼명이 fid 숫자형태로 저장되어 있으므로, 문자열로 검색하도록 인터페이스를 제공하고
    # 문자열을 fid로 자동변환하여 DB검색할 수 있어야 한다.

    def __init__(self, schema):
        self.schema = schema
        self._build_FHdict()
        self._build_HFdict()
    """{Fid:Hangeul}"""
    def _build_FHdict(self):
        cursor = self.schema.find({'column':{'$nin':['dt','cid']}}, {'_id':0, 'column':1, 'desc':1})
        self.FHdict = {}
        for d in list(cursor):
            self.FHdict.update({d['column']: d['desc']})
    """{Hangeul:Fid}"""
    def _build_HFdict(self):
        self.HFdict = {v:k for k,v in self.FHdict.items()}
    def to_fid(self, d):
        if not isinstance(d, dict): raise
        for k,v in d.copy().items():
            if k in self.HFdict:
                del d[k]
                d.update({self.HFdict[k]: v})
        return d
    def to_name(self, d):
        if not isinstance(d, dict): raise
        for k,v in d.copy().items():
            if k in self.FHdict:
                del d[k]
                d.update({self.FHdict[k]: v})
        return d
    def translate(self, dic):
        if not isinstance(dic, dict): raise
        d = {}
        for k,v in dic.items():
            if k in self.HFdict:
                d.update({self.HFdict[k]: v})
            elif k in self.FHdict:
                d.update({self.FHdict[k]: v})
            else:
                d.update({k: v})
        return d

class FidFilter(AutoFilter):

    def __init__(self, schema):
        self.translator = FidTranslator(schema)
        super().__init__(schema)

    def set(self, d):
        f = {} if d is None else d
        f = self.translator.to_fid(d)
        return self._set(f)
    def update(self, d):
        f = self.translator.to_fid(d)
        self.filter.update(f)
        return self

class FidProjection(dict):

    def set(self, schema, p=None):
        self.clear()
        if p is None: pass
        else:
            translator = FidTranslator(schema)
            p = translator.to_fid(p)
            self.update(p)
    def make(self, schema, li, v=1, _id=0):
        self.clear()
        d = {e:v for e in li}
        translator = FidTranslator(schema)
        p = translator.to_fid(d)
        self.update(p)
        self.update({'_id':_id})
