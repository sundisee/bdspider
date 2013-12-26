#coding:utf-8
import urllib2
import MySQLdb
from urlparse import urlparse
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
import re
import time
import json
#jingdian_urls = []
#jingdian_url = 'http://lvyou.baidu.com/destination/ajax/allview?surl=%s&format=ajax&cid=0&pn=%s'
#conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
#cur=conn.cursor()
#cur.execute('select one_cat_url from baidu_poi where one_cat_url is not NULL')
#result = cur.fetchall()
#jingdian_urls = [jingdian_url % i for i in result if i]
#判断有无重复
#print (jingdian_urls)
#print len(list(set(jingdian_urls)))
#jingdian_urls = list(set(jingdian_urls))
#cur.close()
#conn.close()

for k,one_cat_url in enumerate(result):
    not_end_page = True
    start = 1
    while not_end_page:
        ajax_url = jingdian_url%(one_cat_url[0],start)
        print one_cat_url[0],ajax_url
        try:
            res = urllib2.urlopen(ajax_url)
            json_data = json.loads(res.read())
        except Exception,e:
            print e
        finally:
            pass
        i = 16*(start-1)+1
        print json_data['data']['scene_list']
        if len(json_data['data']['scene_list']):
            for sc in json_data['data']['scene_list']:
                two_cat_url = sc['surl']
                two_cat_name = sc['sname']
                #        city_description = sc['data']['ext']['abs_desc']
                two_cat_rank = i
                i = i +1
                print two_cat_name,two_cat_url,two_cat_rank
                #        cur.execute('update  baidu_poi set one_cat_name = %s, one_cat_url = %s,one_cat_rank = %s where baidu_poi')
                sql = 'insert into baidu_poi(one_cat_url,two_cat_name,two_cat_url,two_cat_rank) values(%s,%s,%s,%s)'
                params = (one_cat_url[0],two_cat_name,two_cat_url,two_cat_rank)
                cur.execute(sql,params)
                print 'success'
                time.sleep(0.01)
            start = start +1
        else:
            not_end_page = False
