##-*- coding: utf-8 -*-
# encoding=utf8  
import re
import sys
reload(sys)

sys.setdefaultencoding('utf8')
# s = "11月1日 14:00~17:00"
# m =  re.search(u"(\d{4}年)?(\d{1,2}月\d{1,2}日)\s*\d{2}[:：]\d{2}.{0,2}\d{2}[:：]\d{2}", s.decode('utf8'))
# print (m.group())
# print (m.group(2))

import json
time = "aaa我是"
addr = "bbb"
rel = {}
rel['time'] = time
rel['addr'] = addr
print json.dumps(rel,ensure_ascii=False)


