##-*- coding: utf-8 -*-
# encoding=utf8  
import re
import sys
reload(sys)

sys.setdefaultencoding('utf8')
text = '''大赛地点：常州西太湖国际博览中心A2馆3号会议室（常州西太湖大道与长虹西路交界处）
大赛规模： 300人'''
# m = re.search(u"时间[^\u4e00-\u9fa5\d]*(\d{4}年)?(\d{1,2}月\d{1,2}日)", text.decode('utf8')) #时间：11月20日
# if (m == None):
#     m = re.search(u"(\d{4}年)?(\d{1,2}月\d{1,2}日\s*(\W?(周|星期).\W?)?\s*\d{2}[:：]\d{2}[^a-zA-Z0-9\u4e00-\u9fa5]{1,2}\d{2}[:：]\d{2})", text.decode('utf8')) #10月10日 10:12-12:33
# if (m == None):
#     m = re.search(u"(时间\D{0,2})(.{0,10}\d{1,2}([:：]\d{2})?(am|pm)?[^a-zA-Z0-9\u4e00-\u9fa5]{1,2}\d{1,2}([:：]\d{2})?(am|pm)?)", text.decode('utf8')) #时间：12/2 (周二) 8pm－9:14pm
# # print (m.group())
# print m.group(2)

m = re.search(u"[\u4e00-\u9fa5]{0,2}地[点址]\n?[^\u4e00-\u9fa5a-zA-Z]{0,3}([\u4e00-\u9fa5a-zA-Z0-9()（） ]+)\n", text.decode('utf8'))

print m.group(1)



# import json
# time = "aaa我是"
# addr = "bbb"
# rel = {}
# rel['time'] = time
# rel['addr'] = addr
# print json.dumps(rel,ensure_ascii=False)


