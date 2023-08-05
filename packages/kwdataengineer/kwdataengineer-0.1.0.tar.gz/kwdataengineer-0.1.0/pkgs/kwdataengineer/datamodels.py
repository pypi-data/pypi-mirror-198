# -*- coding: utf-8 -*-
import os
import re
import json
from datetime import datetime, timedelta
import math
import itertools

import pandas as pd
import numpy as np
from PyQt5.QtCore import *
from pymongo import ASCENDING, DESCENDING

from ipylib.idebug import *

from ipylib.ifile import get_filenames
from ipylib.ipath import clean_path
from ipylib.iparser import *
from ipylib.inumber import *
from ipylib.idatetime import DatetimeParser

import trddt

from dataengineer.database import get_db
db = get_db()
from dataengineer import models
from dataengineer.datafile import FileReader, FileWriter
from dataengineer.datacls import BaseDataClass


from kwdataengineer import conf
from kwdataengineer import devguide


from kwdataengineer.Lib.dtype import WordDtypeAssigner
from kwdataengineer.Lib import finder



############################################################
"""베이스모델"""
############################################################
class SchemaModel(models.SchemaModel):

    @ctracer
    def create(self, schemaName=None):
        # CSV파일 --> DB
        schemaName = self.modelName if schemaName is None else schemaName
        file = os.path.join(conf.SCHEMA_FILE_PATH, f'{schemaName}.csv')
        data = FileReader.read_csv(file)
        if data is None: pass
        else:
            # 컬럼 순서를 정해준다
            for i,d in enumerate(data): d['seq'] = i
            pp.pprint(data)
            # self.drop()
            # self.insert_data(data)


class DataModel(models.DataModel):

    def __init__(self, modelName=None, extParam=None):
        super().__init__(modelName, extParam)
        self.schema = SchemaModel(modelName)

    def backup(self, f=None, p=None, s=None, id=False):
        file = f"C:\pypjts\KiwoomTrader\BKData\{self.modelName}.json"
        data = self.load(f, p, sort=s)
        for d in data:
            if id: d.update({'_id':str(d['_id'])})
            else: del d['_id']
        FileWriter.write_json(file, data)

"""스키마정의없이 사용하는 모델의 datetime컬럼을 파싱"""
def data_astimezone(data, cols):
    for d in data:
        for c in cols:
            d.update({c:d[c].astimezone()})
    return data


############################################################
"""스키마모델"""
############################################################
class TRSchemaModel(models.SchemaModel):
    # TR코드 별로 스키마를 생성하는 모델

    def __init__(self, trcode): super().__init__(trcode)
    @ctracer
    def State(self, *args): pass
    def create(self):
        f = {'trcode':self.modelName}
        c = models.DataModel('TRItem').find(f)
        data = list(c)
        if len(data) > 0:
            # 원천데이타를 그대로 저장
            self.drop()
            # 추가 스키마 정의
            data.append({'column':'dt', 'desc':'키움데이타 수신시간', 'dtype':'datetime'})
            self.insert_many(data)
            # SchemaStructure 정규화
            self.update_many({}, {'$rename':{'item':'column'}})
            self.update_dtype()
            self.update_role()
            self.State(self.collName, '스키마생성완료')
        else:
            logger.warning([self.collName, 'TRItem에 해당 데이타 없음'])
    def update_dtype(self):
        WordDtypeAssigner.assign(self.collName, 'column')
    def update_role(self):
        self.update_many({}, {'$set':{'role':'key'}})
        f = {'column':{'$regex':'체결시간'}}
        self.update_many(f, {'$set':{'role':'keytime'}})


class RealSchemaModel(models.SchemaModel):

    def __init__(self, realtype): super().__init__(realtype)
    @ctracer
    def State(self, *args): pass
    @ctracer
    def create(self):
        c = models.DataModel('RealFID').find({'realtype':self.modelName})
        data = list(c)
        if len(data) > 0:
            # 원천데이타를 그대로 저장
            self.drop()
            # 추가 스키마 정의
            data.append({'column':'dt', 'desc':'키움데이타 수신시간', 'dtype':'datetime'})
            self.insert_many(data)
            # SchemaStructure 정규화
            self.update_many({}, {'$rename':{'name':'column'}})
            self.update_dtype()
            self.update_role()
            self.State(self.collName, '스키마생성완료')
        else:
            logger.warning([self.collName, 'RealFID에 해당 데이타 없음'])
    def update_dtype(self):
        WordDtypeAssigner.assign(self.collName, 'column')
    def update_role(self):
        self.update_many({}, {'$set':{'role':'key'}})


############################################################
"""DevGuideText 모델계열"""
############################################################
class DevGuideTextModelBase(DataModel):

    def __init__(self): super().__init__()
    def create(self):
        self.schema.create()
        self.__create__()
    def __create__(self):
        data = devguide.parse(self.modelName)
        if len(data) > 0:
            self.drop()
            self.insert_many(data)


class MarketOptGubun(DevGuideTextModelBase):

    DevGuideParserType = 'A'

    def __init__(self): super().__init__()
    @ctracer
    def State(self, *args): pass
    @ctracer
    def create(self): super().create()


class OrderType(DevGuideTextModelBase):

    def __init__(self): super().__init__()
    @ctracer
    def create(self): super().create()
    def update_model(self):
        db.OrderType.update_many({}, {'$set':{'supported':True}})
        db.OrderType.update_many({'name':{'$regex':'정정'}}, {'$set':{'supported':False}})


class HogaGubun(DevGuideTextModelBase):

    def __init__(self): super().__init__()
    @ctracer
    def create(self):
        super().create()
        self.update_model()
    def update_model(self):
        db.HogaGubun.update_many({}, {'$set':{'realActive':True}})
        db.HogaGubun.update_many({}, {'$set':{'testActive':False}})
        f = {'name':{'$regex':'지정가|시장가'}}
        db.HogaGubun.update_many(f, {'$set':{'testActive':True}})


"""마켓코드"""
class MarketGubun(DevGuideTextModelBase):

    def __init__(self): super().__init__()
    @ctracer
    def create(self): super().create()



############################################################
"""TR계열"""
############################################################
class TRList(DataModel):

    def __init__(self): super().__init__()
    @ctracer
    def State(self, *args): pass

    def create(self):
        self.schema.create()
        self.__create__()
        self.update_model()
        self._delete_docs()
        self.State('모델데이타 생성 완료')
        return self
    def __create__(self):
        data = devguide.parse(self.modelName)
        if len(data) > 0:
            self.drop()
            self.insert_many(data)
    def update_model(self):
        self._update_markettype()
        self._update_ids_column()
        self._update_modelExt()
        self._update_groupKey()
        self._update_screenNo()
        self.State('모델데이타 업데이트 완료')
    def _update_markettype(self):
        """시장종류 업데이트"""
        li = []

        f,v = {}, '주식'
        li.append((f,v))

        f = {'trname':{'$regex':'선물|옵션|선옵'}}
        v = '파생상품'
        li.append((f,v))

        f = {'trname':{'$regex':'업종|지수'}}
        v = '지수'
        li.append((f,v))

        f = {'trname':{'$regex':'ETF'}}
        v = '증권상품ETF'
        li.append((f,v))

        f = {'trname':{'$regex':'ELW'}}
        v = '증권상품ELW'
        li.append((f,v))

        p = '계좌|예수금|자산|위탁.+거래|비밀번호|잔고현황|인출가능|증거금|신용융자|매매일지'
        f = {'$or':[
            {'trname':{'$regex':p}},
            {'trcode':{'$regex':'^opw', '$options':'i'}},
            {'ids':{'$regex':'계좌번호'}}
        ]}
        v = '자산정보'
        li.append((f,v))

        for f,v in li: self.update_many(f, {'$set':{'markettype':v}})
    def _update_ids_column(self):
        """INPUT-ids컬럼을 추가"""
        _ids = self.distinct('_id')
        for _id in _ids:
            inputs = self.distinct('inputs', {'_id':_id})
            df = pd.DataFrame(inputs)
            try:
                idList = list(df.id)
            except Exception as e:
                pass
            else:
                self.update_one({'_id':_id}, {'$set':{'ids':idList}})
    def _update_modelExt(self):
        """일괄업데이트"""
        # [0] 모든 TR을 미확장모델이라고 가정한다
        self.update_many({}, {'$set':{'modelExt':0}})

        li = []
        # [1] INPUTs에는 종목코드가 있는데, OUTPUTs에는 종목명/코드/번호 가 없으면 컬렉션을 확장시킨다
        keys = ['종목명','종목코드','종목번호']
        pat1 = '종목명|종목코드|종목번호'
        f = {'$or':[
            {'ids':{'$regex':'종목코드'}},
            {'trname':{'$regex':'^주식.+봉차트'}},
        ]}
        li.append([f, 1])

        """미확장모델로 강제변경"""
        # 특정TR들은 미확장모델이다
        # 자산관련 TR들은 전부 미확장모델이다
        pat2 = '^테마|프로그램매매추이차트요청|주식기본정보요청|변동성완화장치발동종목요청'
        f = {'$or':[
            {'modelExt':1, 'trname':{'$regex':pat2}},
            {'markettype':'자산정보'},
        ]}
        li.append([f, 0])

        for f, v in li: self.update_many(f, {'$set':{'modelExt':v}})
    def _update_groupKey(self):
        self.update_many({}, {'$set':{'grkey':None}})

        tpls = []
        # [B] 그룹키=계좌번호+날짜
        f = {'grkey':None,'ids':{'$regex':'계좌번호'},'trname':{'$regex':'당일'}}
        tpls.append((f, 'B'))
        # [C] 그룹키=계좌번호
        f = {'grkey':None,'ids':{'$regex':'계좌번호'}}
        tpls.append((f, 'C'))
        # [A] 그룹키=날짜
        pat = """
            거래량급증|예상체결등락률|전일대비등락률|거래대금상위|당일거래량상위|시가대비등락|
            분봉|당일전일체결
        """
        pat = re.sub('\s', repl='', string=pat)
        f = {'grkey':None,'trname':{'$regex':pat}}
        tpls.append((f, 'A'))

        for f, v in tpls: self.update_many(f, {'$set':{'grkey':v}})
    def _update_modelKey(self):
        self.update_many({}, {'$unset':{'modelKey':''}})
        tpls = []
        items = ['날짜','일자','시간','체결시간','주문시간','호가시간','호가잔량기준시간']
        for item in items: tpls.append(({'outputs':{'$in':[item]}}, item))
        for f,v in tpls: self.update_many(f, {'$set':{'modelKey':v}})
    def _update_screenNo(self):
        trcodes = sorted(self.distinct('trcode'))
        for i,tr in enumerate(trcodes):
            no = str(8000 + i)
            self.update_one({'trcode':tr}, {'$set':{'screen_no':no}})
    def _update_issueDatum(self):
        trs = ['시세표성정보요청','주식거래원요청','주식기본정보요청']
        self.update_many({'trname':{'$in':trs}}, {'$set':{'issueDatum':True}})

        # 제거용
        trs = ['체결정보요청']
        self.update_many({'trname':{'$in':trs}}, {'$unset':{'issueDatum':''}})
    def _delete_docs(self):
        self.delete_many({'caution':{'$regex':'지원.+않는|없는'}})
    def add_outputs(self, trcode, s):
        li = s.strip().split(',')
        self.update_one({'trcode':trcode}, {'$set':{'outputs':li}})
    def isin(self, trcode):
        o = self.select({'trcode':trcode})
        return True if hasattr(o, 'trcode') else False

    def select(self, trcdnm, type='dcls'):
        s = trcdnm.strip()
        m = re.search('^op', s, flags=re.I)
        if m is None:
            for p, repl in zip(['\(', '\)'], ['\(', '\)']):
                s = re.sub(p, repl=repl, string=s)
            f = {'trname':{'$regex':s}}
        else:
            f = {'trcode':s}
        f.update({'outputs':{'$ne':None}})
        try:
            d = self.load(f)[0]
        except Exception as e:
            logger.error([self, f'{trcdnm} 에 해당하는 데이타없음'])
        else:
            if type == 'dict': return d
            elif type == 'dcls': return BaseDataClass(**d)
    """장종료후 시장데이타 일괄수집대상"""
    def target01(self, col='trcode'):
        f = {'markettype':'주식',
            'modelExt':0,
            'outputs':{'$ne':None},
            'trname':{'$nin':['예상체결등락률상위요청']},
        }
        return self.distinct(col, f)
    """장종료후 종목데이타 일괄수집대상"""
    def target02(self, col='trcode'):
        f = {'markettype':'주식',
            'modelExt':1,
            'outputs':{'$ne':None},
            'trname':{'$nin':['순매수거래원순위요청']},
        }
        return self.distinct(col, f)
    def target03(self, col='trcode'):
        f = {
            'markettype':'주식',
            'modelExt':0,
            'outputs':{'$regex':'종목코드'},
            'trname': {'$regex': '상위|순위|등락|거래량|고저|매매'},
            'ids':{'$not':{'$regex':'종목코드'}},
        }
        return self.distinct(col, f)
    def target04(self, col='trcode'):
        f = {'markettype':'주식',
            'modelExt':0,
            'outputs':{'$regex':'종목코드|종목명'},
            'trname': {'$not':{'$regex': '테마|주식기본정보요청'}},
        }
        return self.distinct(col, f)


class TRInput(DataModel):
    # TRList 컬렉션의 inputs 컬럼의 데이타를 재해석한 INPUT 중심 컬렉션
    def __init__(self): super().__init__()
    @ctracer
    def State(self, *args): pass
    def create(self):
        self.schema.create()
        self.__create__()
        self.update_model()
    def __create__(self):
        # 실전투자에서 사용가능한 TR만 대상이다.
        p = {c:1 for c in ['trcode','trname','inputs','markettype']}
        f = {'realActive':True, 'outputs':{'$ne':None}}
        c = TRList().find(f, p)
        _data = list(c)
        if len(_data) > 0:
            self.drop()
            for d in _data:
                trcode, trname, inputs, markettype = d['trcode'],d['trname'],d['inputs'],d['markettype']
                for i in inputs:
                    id, value = i['id'], i['value']
                    f = {'trname':trname, 'trcode':trcode, 'id':id}
                    d = f.copy()
                    d.update({
                        'value_info':value,
                        'values':self._parse_inputValueStr(value),
                        'markettype':markettype,
                    })
                    self.update_one(f, {'$set':d}, True)
        else: raise
    def _parse_inputValueStr(self, value_info):
        values = []
        if value_info is None:
            pass
        else:
            p_value = "[A-Za-z\d]+"
            p_desc = "[0-9A-Z가-힣\(\)\s\+~]+"
            pairs = re.findall(f"({p_value})\s*:\s*({p_desc})", value_info)
            if len(pairs) > 0:
                for v in pairs:
                    values.append({'value':v[0], 'desc':v[1]})
            else:
                pairs = re.findall(f"({p_desc})\s*:\s*({p_value})", value_info)
                if len(pairs) > 0:
                    for v in pairs:
                        values.append({'value':v[1], 'desc':v[0]})
                else:
                    pass
        return values
    def update_model(self):
        """초기값 설정"""
        self.update_many({}, {'$unset':{'value':''}})
        self._update_value01()
        self._update_value02()
        self._update_fmt()
        self.State('모델업데이트 완료')
    """values의 첫번째 값을 초기값으로 설정"""
    def _update_value01(self):
        c = self.find({'values':{'$ne':[]}}, {'values':1})
        for d in list(c):
            e = d['values'][0]
            doc = {'value':e['value']}
            f = {'value':None, '_id':d['_id']}
            self.update_one(f, {'$set':doc})
    """수작업"""
    def _update_value02(self):
        li = []

        f = {'$or':[
            {'id':{'$regex':'계좌번호|비밀번호|기준일자|[끝|시작]*일자|날짜|시간|주문번호|테마명'}},
            {'value_info':{'$regex':'공백허용|사용안함|공백|지원안함'}},
            {'id':'종목코드', 'value_info':{'$regex':'코스피|코스닥'}},
            {'id':'시장구분', 'value_info':{'$regex':'^001|^P00101|^P10101'}},
        ]}
        li.append([f, ''])
    	# '삼성전자'로 일괄 셋업
        f = {'id':{'$regex':'종목코드|종목번호'}}
        li.append([f, '005930'])
        # "ETF+ETN제외"로 일괄설정
        f = {'id':{'$regex':'종목조건|관리종목'}}
        li.append([f, '16'])
        # 회원사코드는 키움증권으로 일괄 셋업
        f = {'id':'회원사코드'}
        li.append([f, '050'])

        f = {'id':'매물대수'}
        li.append([f, '10'])

        f = {'id':'제외종목'}
        li.append([f, '000000000'])

        f = {'$or':[
            {'trname':'공매도추이요청', 'id':'시간구분'},
        ]}
        li.append([f, '0'])

        f = {'$or':[
            {'value_info':{'$regex':'설정값|허용안함'}},
            {'id':{'$regex':'상하한포함|거래대금구분|거래량구분'}},
            {'trname':'종목시간별프로그램매매추이요청', 'id':'시간일자구분'},
            {'trname':'가격급등락요청', 'id':'시간'},
        ]}
        li.append([f, '1'])

        f = {'$or':[
            {'id':'시간구분', 'trname':{'$regex':'프로그램매매추이요청|가격급등락요청|거래량급증요청'}},
            {'trname':'종목일별프로그램매매추이요청', 'id':'시간일자구분'},
            {'trname':'테마그룹별요청', 'id':'검색구분'},
        ]}
        li.append([f, '2'])

        f = {'trname':'프로그램매매추이차트요청', 'id':'종목코드'}
        li.append([f, 'P10101'])

        f = {'trname':'시가대비등락률요청', 'id':'정렬구분'}
        li.append([f, '4'])

        f = {'trname':{'$regex':'^테마'}, 'id':'날짜구분'}
        li.append([f, '5'])

        for f, v in li: self.update_many(f, {'$set':{'value':v}})

        self.delete_many({'value_info':{'$regex':'사용안함$'}})
    def _update_fmt(self):
        self.update_many({}, {'$unset':{'fmt':''}})

        li = []
        f = {'$or':[
                {'id':{'$regex':'일자$|시작일$|종료일$|조회일'}},
                {'value_info':{'$regex':'Y{4}M{2}D{2}|Y{3}M{2}D{2}'}}
        ]}
        li.append([f, '%Y%m%d'])

        f = {'value_info':{'$regex':'조회시간\s*4자리'}}
        li.append([f, '%H%M'])

        f = {'value_info':{'$regex':'Y{4}M{2}(?!D)'}}
        li.append([f, '%Y%m'])

        for f, fmt in li: self.update_many(f, {'$set':{'fmt':fmt}})
    """value컬럼만 업데이트"""
    def update_value(self, tr, i, v):
        o = TRList().select(tr, type='dcls')
        self.update_one({'trcode':o.trcode,'id':i}, {'$set':{'value':v}})


class TRItem(DataModel):

    def __init__(self): super().__init__()
    def create(self):
        self.schema.create()
        self.__create__()
        self.update_model()
    def __create__(self):
        def __build_data_v1():
            cursor = db.TRList.find({'realActive':True, 'outputs':{'$ne':None}}, {'trcode':1, 'trname':1, 'outputs':1})
            srcdata = list(cursor)
            data = []
            for d in srcdata:
                for item in d['outputs']:
                    data.append({'item':item, 'trcode':d['trcode']})

            df = pd.DataFrame(data)
            data = []
            for n, g in df.groupby('item'):
                data.append({'item':n, 'trcodes':list(g.trcode)})
            return data
        def __build_data_v2():
            cursor = db.TRList.find({'realActive':True, 'outputs':{'$ne':None}}, {'trcode':1, 'trname':1, 'outputs':1})
            srcdata = list(cursor)
            df = pd.json_normalize(srcdata, 'outputs', ['trcode','trname'])
            df = df.rename(columns={0:'item'})
            return df.to_dict('records')

        data = __build_data_v2()
        if len(data) > 0:
            self.drop()
            self.insert_many(data)
    def update_model(self):
        self._update_dtype()
        self._update_unit()
    def _update_dtype(self):
        WordDtypeAssigner.assign(self.modelName, 'item')
    def _update_unit(self):
        tpls = []
        p1 = '거래[대금$|금액$]|프로그램순매수금액증감'
        tpls.append(({'item':{'$regex':p1}, 'dtype':{'$regex':'int'}}, 6))
        for f,v in tpls: self.update_many(f, {'$set':{'unit':v}})
    """OUTPUT이 새롭게 추가된 TR을 찾아서 Docs를 추가"""
    def add_newItems(self): pass


class TRModel(DataModel):

    def __init__(self, trcdnm, isscdnm=None):
        d = TRList().select(trcdnm, type='dict')
        if d is None: raise
        else:
            for k,v in d.items(): setattr(self, k, v)
            if self.outputs is None: raise

            if self.modelExt == 1:
                if isscdnm is None: raise
                else:
                    o = Issue().select(isscdnm)
                    if o is None: raise
                    else: extParam = o.code
            else: extParam = None

            super().__init__(self.trcode, extParam)
            self.schema = TRSchemaModel(self.trcode)
    @ctracer
    def State(self, *args):pass
    # @ctracer
    def save_data(self, data):
        if len(data) > 0: self.insert_many(data)
        else: pass
    @ctracer
    def dedup_data(self):
        if self.trname == '시가대비등락률요청':
            c = self.find({'dt':{'$gt':trddt.systrdday('18:00')}}, sort=[('dt',-1)])
            df = pd.DataFrame(list(c))
            TF = df.duplicated(keep='first', subset=['종목명'])
            df1 = df[TF]
            if len(df1) > 0: self.delete_many({'_id':{'$in':list(df1._id)}})
        else: pass



############################################################
"""Real계열"""
############################################################
class RTList(DataModel):

    def __init__(self): super().__init__()
    @ctracer
    def State(self, *args): pass
    def create(self):
        self.schema.create()
        self.__create__()
        self.update_model()
        self.State('모델생성완료.')
    def __create__(self):
        data = devguide.parse(self.modelName)
        if len(data) > 0:
            self.drop()
            self.insert_many(data)
    def update_model(self):
        self._update_errors()
        self._update_modelExt()
        self._update_markettype()
        self._update_typeNo()
        self._update_fids()
    def _update_errors(self):
        self.update_one({'realtype':'VI발동'}, {'$set':{'realtype':'VI발동/해제'}})
    def _update_markettype(self):
        """시장종류 업데이트"""
        self.update_many({}, {'$set':{'markettype':'주식'}})

        li = [
            ('자산정보','^잔고|주문체결'),
            ('시장','장시작|VI'),
            ('파생상품','선물|옵션|선옵|파생'),
            ('지수','업종'),
            ('증권상품','ETF|ELW')
        ]
        for v,p in li:
            self.update_many({'realtype':{'$regex':p}}, {'$set':{'markettype':v}})
    def _update_typeNo(self):
        f = {'markettype':{'$regex':'시장|주식|자산정보|지수'}}
        realtypes = self.distinct('realtype', f)
        nos = [str(i).zfill(2) for i in range(1, len(realtypes)+1)]
        for no, realtype in zip(nos, realtypes):
            f = {'realtype':realtype}
            d = {'typeNo':no}
            self.update_one(f, {'$set':d})
    def _update_modelExt(self):
        # 0:미확장모델 | 1:CID확장모델 | 2:ACC확장모델
        # (0) 일단 해당 컬럼들 청소
        self.update_many({}, {'$unset':{'modelExt':''}})
        # [1] 모든 실시간타입에 대해 일단 모델을 확장시키지 않는다
        self.update_many({}, {'$set':{'modelExt':0}})
        # [2] 종목에 종속적이면, 모델을 확장시킨다. (실시간타입명에 '주식'|'종목'이란 단어가 들어있다)
        f = {'realtype':{'$regex':'^[주식|종목]'}}
        self.update_many(f, {'$set':{'modelExt':1}})
        # [3] 계좌번호에 종속적이면, 모델을 확장시킨다. ('fid = 계좌번호' 인 경우)
        f = {'fid_data':{'$elemMatch':{'name':'계좌번호'}}}
        self.update_many(f, {'$set':{'modelExt':2}})
        return self
    def _update_fids(self):
        c = self.find()
        for d in list(c):
            df = pd.DataFrame(d['fid_data'])
            fids = list(df.fid)
            self.update_one({'realtype':d['realtype']}, {'$set':{'fids':fids}})


class RealFID(DataModel):
    # RTList, ChejanFID 로부터 모든 fid를 추출하여 관리하는 fid 중심 컬렉션
    def __init__(self): super().__init__()
    @ctracer
    def State(self, *args): pass
    def create(self):
        self.schema.create()
        self.__create__()
        self.update_model()
        self.State('모델생성완료')
    def __create__(self):
        c = db.RTList.find()
        df = pd.json_normalize(list(c), 'fid_data', ['realtype','markettype'])
        if len(df) > 0:
            self.drop()
            self.insert_many(df.to_dict('records'))
        else: raise
    def update_model(self):
        self._modify_errors()
        self._update_unit()
        self._update_desc()
        # self._delete_uncertain_fids()
        self._update_useful()
        self._assign_screenNo()
        return self
    """키움증권개발오류정정"""
    def _modify_errors(self):
        # 병신같은 키움개발자들 때문에 잘못된 용어를 수동으로 강제 변환해야한다
        self.update_one({'name':'당일총매도손일'}, {'$set':{'name':'당일총매도손익','dtype':'int'}})
    def _update_dtype(self):
        WordDtypeAssigner.assign(self.modelName, 'name')
        f = {'name':{'$regex':'전일거래량대비\(계약,주\)'}}
        self.update_many(f, {'$set':{'dtype':'int'}})
    def _update_unit(self):
        self.update_many({'name':{'$regex':'\(억\)'}}, {'$set':{'unit':8}})
    def _update_desc(self):
        li = [
            ('매도호가1','=최우선매도호가'),
            ('매수호가1','=최우선매수호가')
        ]
        for name, desc in li:
            self.update_one({'name':name}, {'$set':{'desc':desc}})
    def _delete_uncertain_fids(self): self.delete_many({'name':{'$regex':'Extra.*Item'}})
    def _update_useful(self):
        self.update_many({}, {'$set':{'useful':False}})

        """useful = True"""
        p = 'VI|장시작|잔고|주문체결|프로그램|당일거래원|주식시세|예상체결|우선호가|주식체결|호가잔량'
        f = {'realtype':{'$regex':p}}
        self.update_many(f, {'$set':{'useful':True}})

        """useful = False"""
        f = {'realtype':{'$regex':'ELW|ETF|업종|선물|옵션|파생'}}
        self.update_many(f, {'$set':{'useful':False}})
        p = """
            전일대비|전일대비기호|[상하]한가발생시간|시가총액|시가|거래비용|Extra Item|^LP|색깔|
            통화단위|투자자별ticker
        """
        p = re.sub('\s', repl='', string=p)
        f = {'name':{'$regex':p}}
        self.update_many(f, {'$set':{'useful':False}})
    def _assign_screenNo(self):
        fids = self.distinct('fid', {'useful':True})

        def __view(f):
            f.update({'useful':True})
            v = self.distinct('fid', f)
            print(len(v), v, f)

        tpls = []
        f = {'markettype':{'$regex':'시장|지수'}}
        __view(f)
        tpls.append((f, '5000'))

        f = {'realtype':{'$regex':'주식체결|주식시세|주식우선호가|주식종목정보|주식호가잔량'}}
        __view(f)
        tpls.append((f, '5001'))

        f = {'realtype':{'$regex':'종목프로그램매매|주식당일거래원'}}
        __view(f)
        tpls.append((f, '5002'))

        f = {'realtype':{'$regex':'주식예상체결|주식시간외호가'}}
        __view(f)
        tpls.append((f, '5003'))

        self.update_many({}, {'$unset':{'screen_no':''}})
        for f, v in tpls:
            f.update({'useful':True})
            self.update_many(f, {'$set':{'screen_no':v}})


class RealModelV1(DataModel):

    # @ctracer
    def __init__(self, realtype, extParam=None):
        try:
            d = RTList().load({'realtype':realtype})[0]
        except Exception as e:
            logger.error([self, e, realtype, extParam])
            raise
        else:
            for k,v in d.items(): setattr(self, k, v)
            if self.modelExt == 0: extParam = None
            elif self.modelExt == 1:
                o = Issue().select(extParam)
                if o is None: raise
                else: extParam = o.code
            elif self.modelExt == 2:
                o = Account().select(extParam)
                if o is None: raise
                else: extParam = o.AccountNo
            else: raise
            super().__init__(self.realtype, extParam)
            self.schema = RealSchemaModel(self.realtype)
    @ctracer
    def State(self, *args): pass

    """날짜별로 하루치를 로딩"""
    def load_one(self, dt=None, **kw):
        f = kw
        sdt = trddt.today() if dt is None else DatetimeParser(dt)
        edt = sdt + timedelta(days=+1)
        f.update({'체결시간':{'$gte':sdt, '$lt':edt}})
        return self.load(f)
    """과거 하루치를 더 로딩"""
    def load_more(self):
        # 하루씩 더 로딩하도록 필터를 업데이트
        """filter.update({})"""
        cursor = self.find()
        return self.schema.astimezone(list(cursor))
    def clean_collection(self):
        keycols = self.schema.distinct('column', {'role':{'$in':['key']}})
        print('keycols:', keycols)
        f = {c:None for c in keycols}
        pretty_title('삭제할 도큐먼트들')
        print('filter:', f)
        cnt = self.count_documents(filter=f)
        print('cnt:', cnt)
        self.delete_many(f)
    def clean_collection_1(self):
        PartGubun('무의미한 데이타 삭제')
        f = {'체결시간':None, '매수금액':None}
        self.delete_many(f)


class RealModelV2(RealModelV1):

    def __init__(self, realtype, extParam=None):
        try:
            d = RTList().load({'realtype':realtype})[0]
        except Exception as e:
            logger.error([self, e, realtype, extParam])
            raise
        else:
            for k,v in d.items(): setattr(self, k, v)
            if self.modelExt == 0: extParam = None
            elif self.modelExt == 1:
                o = Issue().select(extParam)
                if o is None: raise
                else: extParam = o.code
            elif self.modelExt == 2:
                o = Account().select(extParam)
                if o is None: raise
                else: extParam = o.AccountNo
            else: raise
            super().__init__('RealModel', extParam)
            self.schema = RealSchemaModel(self.realtype)








class ScreenNumber(DataModel):

    def __init__(self): super().__init__()

    def update_model(self):
        # BY TRList 생성
        # TR-계열
        self._by_TRList({'trcode':{'$regex':'^opt', '$options':'i'}}, 1000)
        # ACCT-계열
        self._by_TRList({'trcode':{'$regex':'^opw', '$options':'i'}}, 2000)

        logger.info(f'{self} | Done.')
    def _by_TRList(self, filter, n):
        cursor = db.TRList.find(filter, {'trname':1, '_id':0}, sort=[('trname',ASCENDING)])
        df = pd.DataFrame(list(cursor))
        df.index = df.index + n
        df.index = df.index.astype('str')
        df = df.reset_index(drop=False).rename(columns={'index':'code', 'trname':'name'})
        db.ScreenNumber.insert_many(df.to_dict('records'))


class WordDtype(DataModel):
    seqNoMap = {
        'str':0,
        'time':1,
        'date':2,
        'datetime':3,
        'pct':4,
        'float':5,
        'int_abs':6,
        'int':7,
    }
    def __init__(self): super().__init__()

    @ctracer
    def create(self):
        self.schema.create()
        self.create()
        self.mig()
    def mig(self):
        db.WordDtypeBK.drop()
        db.WordDtype.rename('WordDtypeBK')
        m = DataModel('WordDtypeBK').info()
        data = m.load()
        df = pd.json_normalize(data, 'regex', ['order','dtype'])
        df = df.rename(columns={0:'pat', 'order':'seq'})
        print(df)
        self.drop()
        self.insert_many(df.to_dict('records'))

    def add(self, dtype, pat):
        pats = pat.split('|')
        n = self.seqNoMap[dtype]
        for p in pats:
            f = {'pat':pat}
            d = f.copy()
            d.update({'dtype':dtype, 'seq':n})
            self.update_one(f, {'$set':d}, True)


class Account(DataModel):

    def __init__(self): super().__init__()
    def select(self, s, type='dcls'):
        m = re.search('\d{10}', s)
        if m is None: f = {'AccountBank':{'$regex':s}}
        else: f = {'AccountNo':s}
        try:
            d = self.load(f, sort=[('created_dt',-1)])[0]
        except Exception as e:
            logger.error([self, e, s])
        else:
            if type == 'dcls': return BaseDataClass(**d)
            elif type == 'dict': return d


############################################################
"""일반모델 계열"""
############################################################
class Issue(DataModel):

    def __init__(self): super().__init__()
    def create(self):
        self.schema.create()
    def clean_model(self):
        f = {'code':{'$in':[None, '']}}
        self.delete_many(f)
    def _update_banned(self):
        self.update_many({}, {'$set':{'banned':False}})

        pat = '우$|선물|ETF|ETN|인버스|2X|액티브|\d{3}|스팩|\d+호|KOSEF|iSelect|채\d+년|채권|배당|KODEX|\(합성.*\)|레버리지|MV$|TOP|^WOORI|^HANARO|^ARIRANG|리츠$|홀딩스$|^TIGER|^KBSTAR|^ACE'
        f = {'$or':[
                {'name':{'$regex':pat}},
                {'supervision':{'$regex':'투자주의|투자경고'}},
                {'state1':{'$regex':'거래정지'}},
        ]}
        self.update_many(f, {'$set':{'banned':True}})
    def _update_nameGroup(self):
        d = {'우$': '우선주',
            '선물': '선물',
            'ETF': 'ETF',
            'ETN': 'ETN',
            '인버스': '인버스',
            '2X': '2X',
            '액티브': '액티브',
            '스팩': '스팩',
            '\\d+호': '스팩',
            'KOSEF': 'KOSEF',
            'iSelect': 'iSelect',
            '채\\d+년': '채권',
            '채권': '채권',
            '배당': '배당',
            'KODEX': 'KODEX',
            '\\(합성.*\\)': '',
            '레버리지': '레버리지',
            'MV$': 'MV',
            'TOP': 'TOP',
            '^WOORI': 'WOORI',
            '^HANARO': 'HANARO',
            '^ARIRANG': 'ARIRANG',
            '리츠$': '리츠',
            '홀딩스$': '홀딩스',
            '^TIGER': 'TIGER',
            '^KBSTAR': 'KBSTAR',
            '^ACE': 'ACE',
            '^SOL':'SOL',
            '^마이다스':'마이다스',
            '\\d{3}$': '인덱스',
        }
        self.update_many({}, {'$unset':{'nameGroup':''}})
        for k,v in d.items():
            self.update_many({'nameGroup':None, 'name':{'$regex':k}}, {'$set':{'nameGroup':v}})
    def select(self, cdnm='삼성전자', type='dcls'):
        v = cdnm.strip()
        m = re.search('\d{6}|(^[A-Z]*)(\d{6}$)|^\d{5}[A-Z]$', v)
        if m is None: f = {'name':v}
        else:
            # print(v, m, m.groups())
            if m.groups() == (None, None): f = {'code':v}
            else: f = {'code':m[2]}

        try: d = self.load(f)[0]
        except Exception as e: logger.error([self, e, cdnm])
        else:
            d.update({'cdnm': f"{d['name']}({d['code']})"})
            if type == 'dcls': return BaseDataClass(**d)
            elif type == 'dict': return d
    def exclude_ETF_ETN(self, codes):
        f = {'code':{'$in':codes}, 'stock_info':{'$not':{'$regex':'ETF|ETN'}}}
        return self.distinct('code', f)
    def exclude_ETF_ETN_names(self, names):
        f = {'name':{'$in':names}, 'stock_info':{'$not':{'$regex':'ETF|ETN'}}}
        return self.distinct('name', f)
    def get_ETFETN_names(self):
        return self.distinct('name', {'stock_info':{'$regex':'ETF|ETN'}})
    def exclude_warning(self, codes):
        f = {'$or':[
                {'code':{'$in':codes}},
                {'banned':False},
                {'전일종가':{'$gte':1000, '$lte':50000}},
        ]}
        return self.distinct('code', f)
    def trade_target(self, codes=None):
        f = {
            'banned':False,
            '전일종가':{'$gte':1000, '$lte':50000},
        }
        if isinstance(codes, list): f.update({'code':{'$in':codes}})
        else: pass
        return self.distinct('code', f)


class FidParsingError(DataModel):

    def __init__(self): super().__init__()


class ErrorLog(DataModel):

    def __init__(self): super().__init__()


class WorkerSchedule(DataModel):

    def __init__(self): super().__init__()
    def create(self):
        self.schema.create()
        self.__create__()
        self.update_model()
    def __create__(self): super().create()
    def update_model(self): pass
    def backup(self):
        file = f"C:\pypjts\KiwoomTrader\Data\ManDataJSON\{self.modelName}.json"
        p = {c:0 for c in ['_id','lastRuntime']}
        data = self.load({}, p, sort=[('worker',1),('start_dt',1)])
        FileWriter.write_json(file, data, colseq=self.schema.colseq)
    def add(self, worker, **d):
        f = {'worker':worker}
        self.delete_one(f)

        d.update(f)
        n = self.count_documents({})
        d.update({'id':str(n+1).zfill(3)})
        self.update_one(f, {'$set':d}, True)
    def select(self, f, type='dcls'):
        try: d = self.load(f, limit=1)[0]
        except Exception as e: return None
        else:
            if type == 'dcls': return BaseDataClass(**d)
            elif type == 'dict': return d


class TradingAlgorithm(DataModel):

    def __init__(self): super().__init__()
    def create(self):
        self.schema.create()
        super().create()
        self.update_model()
    def update_model(self): pass

    """#################### DBAdmin ####################"""
    def add_algo(self, doc):
        # 기존저장된 문서가 있으면 패스, 없으면 새로 생성
        data = self.load(doc)
        if len(data) > 0: pass
        else:
            n = self.count_documents({})
            id = str(n).zfill(2)
            f = {'id':id}
            doc.update(f)
            self.update_one(f, {'$set':doc}, True)
    def change_dts_for_developer(self):
        d = {'stime':'00:00', 'etime':'23:59'}
        self.update_many({}, {'$set':d})


class TradingSimulationAlgorithm(DataModel):

    def __init__(self): super().__init__()

    @ctracer
    def backup(self):
        file = f"C:\pypjts\KiwoomTrader\Data\ManDataJSON\{self.modelName}.json"
        data = self.load({}, {'_id':0})
        FileWriter.write_json(file, data)


class ConditionSearchHistory(DataModel):

    def __init__(self, dt=None):
        extParam = trddt.systrdday(dt).strftime('%Y%m%d')
        super().__init__(self.__class__.__name__, extParam)
    def record(self, ConditionName, Type, Code, Name):
        state = 1 if Type == 'I' else 0
        dt = trddt.now().replace(microsecond=0)
        d = {'name':Name, 'code':Code, 'dt':dt, 'condition':ConditionName, 'state':state}
        self.insert_one(d)


class Variables(DataModel):

    def __init__(self):
        super().__init__()
        self._variables = [('a','변화율'), ('b','변곡률')]
        self._seqdigit = 4
    @ctracer
    def create(self):
        self.___create__()
        self._addup_vnames()
    def ___create__(self):
        m = TRItem()

        """TRItem컬렉션에 var컬럼 생성"""
        m.update_many({}, {'$unset':{'var':''}})
        data = m.load({'dtype':{'$regex':'int|float|pct'}}, {'_id':1})
        print(len(data))
        for i, d in enumerate(data):
            seq = str(i).zfill(self._seqdigit)
            m.update_one({'_id':d['_id']}, {'$set':{'var':'v'+seq}})

        """DB생성"""
        data = m.load({'var':{'$ne':None}}, {'var':1,'item':1})
        if len(data) > 0:
            df = pd.DataFrame(data)
            data = df.rename(columns={'var':'vid', 'item':'vname'}).to_dict('records')
            self.drop()
            self.insert_many(data)
        else:
            logger.error(['data 개수오류. TRItem컬렉션을 확인하라', self])
    def _addup_vnames(self):
        # self.delete_many({'vname':{'$regex':'가차$|BB'}})
        # df = self.view({'vname':{'$regex':'가차$'}}, sort=[('vid',1)])
        # print(df)

        """변수명생성"""
        li = []
        # 봉차트가격변화변수명
        iterables = ['시가고가','시가종가','시가저가','저가고가'], ['차','변화율']
        for e in itertools.product(*iterables):
            li.append(e[0]+e[1])
        # 봉차트이동평균변수명
        iterables = ['분','일','주','월','연'],['봉'],['MA'], [3,5,10,20,40,60,120]
        for e in itertools.product(*iterables):
            li.append(e[0]+e[1]+e[2]+str(e[3]))
        # 볼린저밴드변수명
        iterables = ['분','일','주','월','연'],['봉'],['BB'],[10,20],['상','중','하']
        for e in itertools.product(*iterables):
            li.append(e[0]+e[1]+e[2]+str(e[3])+e[4])

        """변수추가"""
        for vname in li: self.add(vname)
    def select(self, f, type='dcls'):
        try: d = self.load(f, limit=1)[0]
        except Exception as e: pass
        else:
            if type == 'dcls': return BaseDataClass(**d)
            elif type == 'dict': return d
    def add(self, vname):
        o = self.select({'vname':vname})
        if o is None:
            seq = self._get_vseq()
            vid = 'v'+seq
            doc = {'vname':vname,'vid':vid}
            print(doc)
            self.update_one(doc, {'$set':doc}, True)
        else:
            print(f"기등록된 variableName--> '{vname}'")
    def _get_vseq(self):
        vids = self.distinct('vid')
        if len(vids) > 0:
            nums = []
            for v in vids:
                m = re.search('v(\d+)', v)
                nums.append(int(m[1]))
                nums = sorted(set(nums))
            seq = nums[-1] + 1
        else:
            seq = 0
        return str(seq).zfill(self._seqdigit)
    def get_renameDict(self, type='a', reverse=False):
        data = self.load({}, {'vid':1, 'vname':1, '_id':0})
        dic = {}
        for d in data:
            if reverse:
                vid, vname = d['vid']+type, d['vname']+type
                dic.update({vid: vname})
            else:
                vid, vname = d['vid']+type, d['vname']
                dic.update({vname: vid})
        return dic

"""일자별종목변수데이타"""
class IssueVariableData01(DataModel):

    def __init__(self, isscdnm):
        self.Issue = Issue().select(isscdnm, type='dcls')
        super().__init__(extParam=self.Issue.code)
    def save_data(self, df, var, tcol):
        m = Variables()
        dic = m.get_renameDict(type=var)
        df = df.rename(columns=dic)
        df = df.rename(columns={tcol: '일자'})
        df = df.reset_index(drop=False)

        for d in df.to_dict('records'):
            f = {'일자':d['일자']}
            self.update_one(f, {'$set':d}, True)


class Target05(DataModel):

    def __init__(self): super().__init__()
    @ctracer
    def update_model(self):
        self.update_nSrc()
        self.update_banned()
        self._update_group()
    @ctracer
    def update_nSrc(self):
        c = self.find()
        for d in list(c):
            self.update_one({'_id':d['_id']}, {'$set':{'n_src':len(d['src'])}})
    @ctracer
    def update_banned(self):
        codes = self.distinct('code')
        codes = Issue().exclude_warning(codes)
        self.update_many({}, {'$set':{'banned':True}})
        self.update_many({'code':{'$in':codes}}, {'$set':{'banned':False}})
    @ctracer
    def _update_group(self):
        li = []
        f = {'src':{'$nin':['전일대비등락률상위요청'], '$in':['예상체결등락률상위요청']}}
        li.append([f, 'A'])
        f = {'src':{'$in':['전일대비등락률상위요청'], '$nin':['예상체결등락률상위요청']}}
        li.append([f, 'B'])
        f = {'src':{'$all':['전일대비등락률상위요청','예상체결등락률상위요청']}}
        li.append([f, 'C'])
        # f = {'src':{'$regex':'전일대비등락률상위요청|예상체결등락률상위요청'}}
        # li.append([f, 'D'])
        for f, v in li: self.update_many(f, {'$set':{'group':v}})
    @ctracer
    def target01(self, type='code'):
        f,s = {}, [('n_src',-1)]
        f.update({'n_src':{'$gte':3}})
        f.update({'banned':False})
        data = self.load(f, sort=s)
        df = pd.DataFrame(data)
        return list(df[type])
    @ctracer
    def target02(self, type='code'):
        f,s = {}, [('n_src',-1)]
        f.update({'dt':trddt.systrdday()})
        f.update({'group':'C'})
        data = self.load(f, sort=s, limit=256)
        df = pd.DataFrame(data)
        return list(df[type])
    @ctracer
    def target03(self, type='code'):
        f,s = {}, [('n_src',-1)]
        f.update({'dt':trddt.systrdday()})
        f.update({'group':'D'})
        f.update({'n_src':{'$gt':1}})
        data = self.load(f, sort=s, limit=256)
        df = pd.DataFrame(data)
        return list(df[type])


class Target01(DataModel):

    def __init__(self): super().__init__()


class IssueDailyData(DataModel):

    def __init__(self, isscdnm):
        self.Issue = Issue().select(isscdnm)
        super().__init__(extParam=self.Issue.code)
    def gather(self):
        self._gather01()
        self._gather02()
    def _gather01(self):
        f1 = {'markettype':{'$regex':'주식|자산'}, 'modelExt':0, 'outputs':{'$ne':None}}
        trnames = TRList().distinct('trname', f1)
        for trname in trnames:
            m = TRModel(trname)
            li = m.schema.distinct('column', {'column':{'$regex':'종목명|종목코드|종목번호'}})
            if len(li) > 0:
                f2 = {'$or':[
                    {'종목명':self.Issue.name},
                    {'종목코드':self.Issue.code},
                    {'종목번호':self.Issue.code},
                ]}
                data = m.load(f2, sort=[('dt',1)])
                for d in data:
                    key = d['dt'].strftime('%Y-%m-%d')
                    key = trddt.systrdday(key)
                    f3 = {'일자':key}
                    d.update(f3)
                    self.update_one(f3, {'$set':d}, True)
            else: pass
    def _gather02(self):
        f1 = {'markettype':{'$regex':'주식'}, 'modelExt':1, 'outputs':{'$ne':None}}
        trnames = TRList().distinct('trname', f1)
        for trname in trnames:
            m = TRModel(trname, self.Issue.name)
            li = m.schema.distinct('column', {'column':{'$regex':'일자|날짜'}})
            if len(li) > 0:
                data = m.load(sort=[('dt',1)])
                for d in data:
                    try: f3 = {'일자':d['일자']}
                    except Exception as e: f3 = {'일자':d['날짜']}
                    finally:
                        d.update(f3)
                        self.update_one(f3, {'$set':d}, True)
            else: pass
