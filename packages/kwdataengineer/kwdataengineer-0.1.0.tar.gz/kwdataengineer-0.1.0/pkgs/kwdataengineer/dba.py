# -*- coding: utf-8 -*-
import os
import sys
import re

import pandas as pd

from ipylib.idebug import *
from ipylib.idatetime import *
from ipylib.iparser import *

from dataengineer.database import *
db = get_db()


from kwdataengineer import datamodels







@ctracer
def create_tr_related_models():
    datamodels.TRList().create()
    datamodels.TRInput().create()
    datamodels.TRItem().create()
    create_TrSchemaModels()
    logger.info('TR 관련 모델 생성 완료')

@ctracer
def create_TrSchemaModels():
    trcodes = datamodels.TRList().distinct('trcode', {'realActive':True})
    for tr in trcodes:
        datamodels.TRSchemaModel(tr).create()

@ctracer
def create_real_related_models():
    datamodels.RTList().create()
    datamodels.RealFID().create()
    create_RealSchemaModels()

@ctracer
def create_RealSchemaModels():
    realtypes = datamodels.RTList().distinct('realtype')
    for realtype in realtypes:
        datamodels.RealSchemaModel(realtype).create()

@ctracer
def init_db():
    create_tr_related_models()
    create_real_related_models()
############################################################
"""DATABASE LEVEL"""
############################################################
class CollNameParser:

    def __init__(self, collName):
        if isinstance(collName, str):
            pat = f'(_Schema_)*([a-zA-Z가-힣0-9\s]+)_*([a-zA-Z\d가-힣\.\(\)]+)*$'
            m = re.search(pat, collName)
            # print(m.groups(), name)
            modelType, modelName, param = m[1], m[2], m[3]

            self.modelType = 'Data' if modelType is None else modelType.replace('_','')
            self.modelName = modelName
            self.param = param
            self.collName = collName

            if re.match('^op[tw]', modelName, flags=re.I) is not None:
                self.modelCate = 'TR'
            elif re.search('[가-힝]+|^Chejan$|^OrderResult$', modelName) is not None:
                self.modelCate = 'RT'
            else:
                self.modelCate = 'Meta'
        else:
            logger.error(f'{self} | collName은 반드시 문자열이어야 한다')
    @property
    def dict(self): return {
        'modelType':self.modelType,
        'modelName':self.modelName,
        'param':self.param,
        'collName':self.collName,
        'modelCate':self.modelCate}

class CollectionList(datamodels.DataModel):

    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.create()
    def create(self):
        self.schema.create()
        names = db.list_collection_names(filter=None)
        data = []
        for name in names:
            p = CollNameParser(name)
            data.append(p.dict)
        self.drop()
        self.insert_many(data)
        return self
    def search(self, f=None, p={'_id':0}, sort=None, **kw):
        sort = self.sort if sort is None else sort
        data = self.load(f, p, sort=sort, **kw)
        df = pd.DataFrame(data).reindex(columns=self.colOrder)
        df.info()
        return df
    def stat(self):
        def __stat__(f):
            pretty_title(f'컬럼별 유니크값[{f}]')
            cols = self.schema.distinct('column')
            for c in cols:
                values = self.distinct(c, f)
                if len(values) < 10: print(c, '|', len(values), '|', values)
                else: print(c, '|', len(values))

        filters = [
            {},
            self.f_schema,
            self.f_data,
            self.f_Rt,
            self.f_Tr,
            self.f_meta,
            self.f_Tr_param,
            self.f_Rt_param,
            self.f_Tr_no_param,
            self.f_Rt_no_param,
            self.f_asset,
        ]
        for f in filters: __stat__(f)

    @property
    def colOrder(self): return ['modelType','modelCate','modelName','param','collName']
    @property
    def sort(self): return [('modelType',1), ('modelCate',1), ('modelName',1), ('param',1)]
    @property
    def f_schema(self): return {'modelType':'Schema'}
    @property
    def f_data(self): return {'modelType':'Data'}
    @property
    def f_Tr(self): return {'modelCate':'TR', 'modelType':'Data'}
    @property
    def f_Rt(self): return {'modelCate':'RT', 'modelType':'Data'}
    @property
    def f_meta(self): return {'modelCate':'Meta', 'modelType':'Data'}
    @property
    def f_Tr_no_param(self): return {'modelCate':'TR', 'modelType':'Data', 'param':None}
    @property
    def f_Rt_no_param(self): return {'modelCate':'RT', 'modelType':'Data', 'param':None}
    @property
    def f_Tr_param(self): return {'modelCate':'TR', 'modelType':'Data', 'param':{'$ne':None}}
    @property
    def f_Rt_param(self): return {'modelCate':'RT', 'modelType':'Data', 'param':{'$ne':None}}
    @property
    def f_asset(self): return {'modelType':'Data', 'modelCate':{'$regex':'TR|RT'}, 'modelName':{'$regex':'^opw|^che|^order', '$options':'i'}}

    @property
    def SchemaCollections(self): return self.search(self.f_schema)
    @property
    def DataCollections(self): return self.search(self.f_data)
    @property
    def TRCollections(self): return self.search(self.f_Tr)
    @property
    def TrParamCollections(self): return self.search(self.f_Tr_param)
    @property
    def TrNoParamCollections(self): return self.search(self.f_Tr_no_param)
    @property
    def RTCollections(self): return self.search(self.f_Rt)
    @property
    def RtParamCollections(self): return self.search(self.f_Rt_param)
    @property
    def RtNoParamCollections(self): return self.search(self.f_Rt_no_param)
    @property
    def MetaCollections(self): return self.search(self.f_meta)
    @property
    def AssetCollections(self): return self.search(self.f_asset)



def change_collName():
    # p = re.compile('(.*)_([A-Z가-힣0-9]+)\((\d{6})\)')
    p = re.compile('([가-힝]+)_([A-Z가-힣0-9\(\)]+)\((\d{5}[A-Z])\)')
    f = {'name':{'$regex':p}}
    names = db.list_collection_names(filter=f)
    for i, oldname in enumerate(names):
        m = p.search(oldname)
        if m is None:
            print(i, oldname, m)
        else:
            # print(m, m.groups())
            modelName = m[1]
            param = m[3]
            newname = f"{modelName}_{param}"
            print(i, oldname, newname)
            try:
                db[oldname].rename(newname)
            except Exception as e:
                logger.error(e)
                try:
                    newname = newname + 'BK'
                    db[oldname].rename(newname)
                except Exception as e:
                    logger.critical(e)

def intergrate_realdata():
    pat = '([가-힝]+_\d{6})(BK)'
    p = re.compile(pat)
    f = {'name':{'$regex':pat}}
    names = db.list_collection_names(filter=f)
    names = names[77:]
    for i, oldname in enumerate(names):
        m = p.search(oldname)
        newname = m[1]
        print(i, oldname, m.groups(), newname)
    #
    #     try:
    #         cursor = db[oldname].find({}, {'_id':0})
    #         # pp.pprint(list(cursor))
    #         db[newname].insert_many(list(cursor))
    #     except Exception as e:
    #         logger.error(e)
    #     # break

def rename_realdata_columns():
    p = re.compile('[가-힝]+_\d{6}')
    f = {'name':{'$regex':p}}
    names = db.list_collection_names(filter=f)
    trsl = handlers.FidTranslator()

    for i, collName in enumerate(names):
        print(i, collName)
        for fid, name in trsl.items():
            db[collName].update_many({}, {'$rename':{fid:name}})
        # break


############################################################
"""COLLECTION LEVEL"""
############################################################
def modify_database(n):
    if n == 1:
        names = db.list_collection_names(filter={'name':{'$regex':'_Schema_op', '$options':'i'}})
        for name in names:
            db[name].drop()

def modify_collection(n):
    if n == 1:
        filter = {'colName':'input'}
        update = {'$set':{'colName':'id'}}
        SchemaModel('TRInput').update_one(filter, update)
    elif n == 2:
        update = {'$set':{'updated_dt':datetime(2021,5,4).astimezone()}}
        db.Company.update_many({}, update)

def postparse_data(model):
    cursor = model.find()
    data = model.schema.parse_data(list(cursor))
    for d in data:
        try:
            filter = {'_id':d['_id']}
            update = {'$set':d}
            model.update_one(filter, update)
        except Exception as e:
            logger.error(e)
            pp.pprint(d)
    print('Done')

def drop_duplicates(modelName):
    model = datamodels.DataModel(modelName)
    keycols = model.schema.keycols
    projection = {k:1 for k in keycols}
    data = model.load(None, projection)
    df = pd.DataFrame(data)

    TF = df.duplicated(subset=keycols, keep='first')
    print(len(df[TF]))
    print(df[TF])

    if len(df[TF]) > 0:
        ids = list(df[TF]._id)
        model.delete_many({'_id':{'$in':ids}})
    logger.info('완료')

def view_TR_rawdata(trcode):
    filter = {'input':{'$regex':trcode, '$options':'i'}}
    projection = {'input':1, 'output':1}
    cursor = db.TRList.find(filter, projection)
    for d in list(cursor):
        for k,v in d.items():
            if k == 'input':
                for line in v.splitlines():
                    print(line)
            else:
                print(v)

def inspect_DataModel(modelName):
    pretty_title(modelName)
    model = datamodels.DataModel(modelName)
    dbg.dict(model.schema)
    model.schema.view()
    dbg.dict(model)
    model.view()

def analyze_RealFID():
    PartGubun('analyze_RealFID')

    data = datamodels.DataModel('RealFID').load(None, {'_id':0})
    df = pd.DataFrame(data)

    # RealFID 분석
    df['cnt'] = df.realtypes.apply(lambda x: len(x))
    df['realtype'] = df.realtypes.apply(lambda x: x[0] if len(x) == 1 else '_None')
    # df = df.sort_values('cnt')
    _df1 = df.query('cnt == 1')
    _df2 = df.query('cnt > 1')

    pretty_title('1개의 Realtype에만 존재하는 FIDs')
    _df1.info()
    _df1 = _df1.sort_values(['name','fid']).reset_index(drop=True)
    print(_df1[:60])
    if len(_df1) > 60: print(_df2[-60:])

    pretty_title('2개 이상의 Realtype에 존재하는 FIDs')
    _df2.info()
    _df2 = _df2.sort_values(['cnt','name','fid'], ascending=False).reset_index(drop=True)
    print(_df2[:60])
    if len(_df2) > 60: print(_df2[-60:])

    return df

def modify_dtype(collName, col, dtype):
    m = db[collName]
    cursor = m.find({col:{'$ne':None}}, {col:1})
    for d in list(cursor):
        id, v = d['_id'], d[col]
        try:
            _v = DtypeParser(v, dtype)
            print(v, type(v), _v, type(_v))
        except Exception as e:
            logger.error(e)
            print(v, type(v), _v, type(_v), e)
        else:
            if _v is not None:
                m.update_one({'_id':id}, {'$set':{col:_v}})

def drop_empty_col(collName, cols):
    m = db[collName]
    if isinstance(cols, str): cols = [cols]
    for col in cols:
        cursor = m.find({col:''}, {col:1})
        pp.pprint(list(cursor))
        m.update_many({col:''}, {'$unset':{col:""}})

"""스키마 컬럼별 유일값 개수"""
def each_column_unique_cnt(self):
    # f = {'dtype':{'$nin':['list','dict','data']}}
    cols = self.columns
    data = []
    for c in cols:
        values = self.model.distinct(c)
        data.append({'colName':c, 'unq_cnt':len(values)})
    df = pd.DataFrame(data)
    return view.view_df(df, title=f'[{self.model.collName}]컬럼별 유일값 개수')
def each_column_unique_values(self):
    cols = self.columns
    data = []
    for c in cols:
        values = self.model.distinct(c)
        SectionGubun()
        print('colName:', c)
        pp.pprint(values)
def count_daily_docs(self, filter=None, **kw):
    try:
        data = self.model.load(filter, projection={'dt':1}, **kw)
        df = pd.DataFrame(data)
        df = df.set_index('dt').resample('1D').count()
        return df
    except Exception as e:
        logger.error(e)
"""스키마 컬럼별 None|Not None 개수"""
def None_each_column(self):
    cols = self.model.schema.distinct('column')
    data = []
    for c in cols:
        cnt1 = self.model.count_documents({c:None})
        cnt2 = self.model.count_documents({c:{'$ne':None}})
        data.append({'column':c, 'n_None':cnt1, 'n_NotNone':cnt2})
    return view.view_df(pd.DataFrame(data), title='스키마 컬럼별 None|Not None 개수')
"""카테고리 컬럼의 값에 의한 문서 개수"""
def count_docs_by_categoryValue(self):
    cols = self.model.schema.distinct('column', {'role':{'$regex':'category'}})
    data = []
    for c in cols:
        cate_values = self.model.distinct(c)
        for v in cate_values:
            cnt = self.model.count_documents({c:v})
            data.append({'column':c, 'value':v, 'n_docs':cnt})
    return view.view_df(pd.DataFrame(data), title='카테고리 컬럼의 값에 의한 문서 개수')
############################################################
"""마이그레이션"""
############################################################
def opt10001():
    trname = '주식기본정보'

    names = db.opt10001.distinct('종목명')
    print(len(names))
    pp.pprint(names)

    if len(names) == 0: db.opt10001.drop()

    for name in names:
        f = {'종목명':name}
        cursor = db.opt10001.find(f, {'_id':0})
        data = list(cursor)
        print(len(data))
        # pp.pprint(data)

        m = TRModel(trname, name)
        m.info()
        m.drop()
        m.insert_many(data)
        m.view()

        db.opt10001.delete_many(f)

def change_fid_colnames():
    h = FidTranslator()
    m = datamodels.DataModel('Chejan')
    for fid, name in h.items():
        print(fid, name)
        if name is None: pass
        elif name == 'Extra Item':
            name == f'Extra{fid}'
        else:
            m.update_many({}, {'$rename':{fid:name}})
        # break
