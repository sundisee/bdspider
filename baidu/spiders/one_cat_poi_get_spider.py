#coding:utf-8
import urllib
import MySQLdb
from urlparse import urlparse
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
import re
import time
import os
#jingdian_urls = []
jingdian_url = 'http://lvyou.baidu.com/%s/'
conn=MySQLdb.connect(host='54.201.192.244',user='qyer',passwd='qyer',db='mafengwo',port=3306,charset='utf8')
cur=conn.cursor()
#2
cur.execute('select two_cat_url,id from baidu_poi where need_spider =1 and one_cat_url is not null and two_cat_url is not null and three_cat_url is null and total_pingjia is not null')
#3
#cur.execute('select three_cat_url,id  from baidu_poi where need_spider =1 and two_cat_url is not null and three_cat_url is not null and four_cat_url is null and total_pingjia is not null')
#4
#cur.execute('select four_cat_url,id  from baidu_poi where need_spider =1 and four_cat_url is not null and three_cat_url is not null and total_pingjia is not null')
result = cur.fetchall()
jingdian_urls = [jingdian_url % i[0] for i in result if i]
##判断有无重复
print len(jingdian_urls)
print len(list(set(jingdian_urls)))
#jingdian_urls = list(set(jingdian_urls))
#cur.close()
#conn.close()
#从db读取城市列表拼装景点url
class ProvinceSpider(BaseSpider):
    """
    get poi
    """
    name = "poi_get"
    allowed_domains = ["lvyou.baidu.cn"]
    start_urls = jingdian_urls
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        baidu_poi_id = -1
        for i in result:
             if  i[0] in response.url:
                 baidu_poi_id = i[1]
                 print baidu_poi_id
        sites = hxs.xpath('//div[@id="J_slide-holder"]/figure')
        for site in sites:
            poi_pic = site.xpath('a/img/@src').extract()[0]
            print poi_pic
            sql = 'insert into baidu_poi_pic_url(poi_pic_url,baidu_poi_id) values(%s,%s)'
            params = (poi_pic,int(baidu_poi_id))
            cur.execute(sql,params)
