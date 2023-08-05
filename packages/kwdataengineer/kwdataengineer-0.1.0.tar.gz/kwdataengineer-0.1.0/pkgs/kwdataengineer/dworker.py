# -*- coding: utf-8 -*-
from datetime import datetime


from ipylib.idebug import *
import trddt


from kwdataengineer import datamodels


# TRModel(시가대비등락률요청)의 당일 데이타를 가져와서
# TRModel(주식일봉차트조회요청)에 업데이트한다
@ctracer
def DayChartUpdater():
    m1 = datamodels.TRModel('시가대비등락률요청')
    f = {'dt': {'$gte': trddt.systrdday('18:00')}}
    data = m1.load(f)
    print({'데이타길이': len(data)})
    _len = len(data)
    for i, d in enumerate(data):
        print(trddt.logtime(), '일봉차트업데이트...', f'{i}/{_len}')
        # print(d)
        m2 = datamodels.TRModel('주식일봉차트조회요청', d['종목명'])
        # m2.info()
        day = trddt.tradeday(d['dt'].strftime('%Y/%m/%d'))
        f = {'일자': day}
        # print(f)
        doc = {c: d[c] for c in m2.outputs if c in d}
        doc.update({'dt': d['dt']})
        # print(doc)
        m2.update_one(f, {'$set': doc}, True)
        # break
