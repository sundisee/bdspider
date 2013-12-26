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
import threading
#jingdian_urls = []
jingdian_url = 'http://lvyou.baidu.com/destination/ajax/allview?surl=%s&format=ajax&cid=0&pn=%s'
conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
cur=conn.cursor()
cur.execute('select three_cat_url from baidu_poi where three_cat_url is not NULL')
result = cur.fetchall()
#result = [i[0] for i in result]
#jingdian_urls = [jingdian_url % i for i in result if i]
#判断有无重复
#print (jingdian_urls)
#print len(list(set(jingdian_urls)))
#jingdian_urls = list(set(jingdian_urls))
#cur.close()
#conn.close()
def run1():
    for k,three_cat_url in enumerate(result[612:2000]):
        conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
        cur=conn.cursor()
        not_end_page = True
        start = 1
        while not_end_page:
            ajax_url = jingdian_url%(three_cat_url[0],start)
            print three_cat_url[0],ajax_url
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
                    four_cat_url = sc['surl']
                    four_cat_name = sc['sname']
                    #        city_description = sc['data']['ext']['abs_desc']
                    four_cat_rank = i
                    i = i +1
                    print four_cat_name,four_cat_url,four_cat_rank
#                    #        cur.execute('update  baidu_poi set one_cat_name = %s, three_cat_url = %s,one_cat_rank = %s where baidu_poi')
                    sql = 'insert into baidu_poi(three_cat_url,four_cat_name,four_cat_url,four_cat_rank) values(%s,%s,%s,%s)'
                    params = (three_cat_url[0],four_cat_name,four_cat_url,four_cat_rank)
                    cur.execute(sql,params)
                    print 'success'
                    time.sleep(0.01)
                start = start +1
            else:
                not_end_page = False
        print 'run1:%s' % k
def run2():
    for k,three_cat_url in enumerate(result[2495:4000]):
        conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
        cur=conn.cursor()
        not_end_page = True
        start = 1
        while not_end_page:
            ajax_url = jingdian_url%(three_cat_url[0],start)
            print three_cat_url[0],ajax_url
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
                    four_cat_url = sc['surl']
                    four_cat_name = sc['sname']
                    #        city_description = sc['data']['ext']['abs_desc']
                    four_cat_rank = i
                    i = i +1
                    print four_cat_name,four_cat_url,four_cat_rank
                    #                    #        cur.execute('update  baidu_poi set one_cat_name = %s, three_cat_url = %s,one_cat_rank = %s where baidu_poi')
                    sql = 'insert into baidu_poi(three_cat_url,four_cat_name,four_cat_url,four_cat_rank) values(%s,%s,%s,%s)'
                    params = (three_cat_url[0],four_cat_name,four_cat_url,four_cat_rank)
                    cur.execute(sql,params)
                    print 'success'
                    time.sleep(0.01)
                start = start +1
            else:
                not_end_page = False
        print 'run2:%s' % k

def run3():
    for k,three_cat_url in enumerate(result[4885:6000]):
        conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
        cur=conn.cursor()
        not_end_page = True
        start = 1
        while not_end_page:
            ajax_url = jingdian_url%(three_cat_url[0],start)
            print three_cat_url[0],ajax_url
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
                    four_cat_url = sc['surl']
                    four_cat_name = sc['sname']
                    #        city_description = sc['data']['ext']['abs_desc']
                    four_cat_rank = i
                    i = i +1
                    print four_cat_name,four_cat_url,four_cat_rank
                    #                    #        cur.execute('update  baidu_poi set one_cat_name = %s, three_cat_url = %s,one_cat_rank = %s where baidu_poi')
                    sql = 'insert into baidu_poi(three_cat_url,four_cat_name,four_cat_url,four_cat_rank) values(%s,%s,%s,%s)'
                    params = (three_cat_url[0],four_cat_name,four_cat_url,four_cat_rank)
                    cur.execute(sql,params)
                    print 'success'
                    time.sleep(0.01)
                start = start +1
            else:
                not_end_page = False
        print 'run3:%s' % k

def run4():
    for k,three_cat_url in enumerate(result[71361:8000]):
        conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
        cur=conn.cursor()
        not_end_page = True
        start = 1
        while not_end_page:
            ajax_url = jingdian_url%(three_cat_url[0],start)
            print three_cat_url[0],ajax_url
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
                    four_cat_url = sc['surl']
                    four_cat_name = sc['sname']
                    #        city_description = sc['data']['ext']['abs_desc']
                    four_cat_rank = i
                    i = i +1
                    print four_cat_name,four_cat_url,four_cat_rank
                    #                    #        cur.execute('update  baidu_poi set one_cat_name = %s, three_cat_url = %s,one_cat_rank = %s where baidu_poi')
                    sql = 'insert into baidu_poi(three_cat_url,four_cat_name,four_cat_url,four_cat_rank) values(%s,%s,%s,%s)'
                    params = (three_cat_url[0],four_cat_name,four_cat_url,four_cat_rank)
                    cur.execute(sql,params)
                    print 'success'
                    time.sleep(0.01)
                start = start +1
            else:
                not_end_page = False
        print 'run4:%s' % k
#thread1 = threading.Thread(target= run1)
#thread2 = threading.Thread(target= run2)
#thread3 = threading.Thread(target= run3)
#thread4 = threading.Thread(target= run4)
#thread5 = threading.Thread(target= run5)
#thread1.start()
#thread2.start()
#thread3.start()
#thread4.start()
#thread5.start()
