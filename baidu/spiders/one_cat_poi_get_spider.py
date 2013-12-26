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
conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
cur=conn.cursor()
#2
cur.execute('select two_cat_url,id from baidu_poi where need_spider =1 and one_cat_url is not null and two_cat_url is not null and three_cat_url is null and total_pingjia is not null')
#3
#cur.execute('select three_cat_url,id  from baidu_poi where need_spider =1 and two_cat_url is not null and three_cat_url is not null and four_cat_url is null and total_pingjia is not null')
#4
#cur.execute('select four_cat_url,id  from baidu_poi where need_spider =1 and four_cat_url is not null and three_cat_url is not null and total_pingjia is not null')
result = cur.fetchall()
jingdian_urls = [jingdian_url % i[0] for i in result if i]
ids = [i[1] for i in result ]
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
        baidu_poi_id = 0
        for i in result:
             if  i[0] in response.url:
                 baidu_poi_id = i[1]
                 print baidu_poi_id
        #simple template
        sites = hxs.xpath('//div[@id="J_slide-holder"]/figure')
        for site in sites:
            poi_pic = site.xpath('a/img/@src').extract()
            print poi_pic
            sql = 'insert into baidu_poi_pic_url(poi_pic_url,baidu_poi_id) valuse(%s,%s)'
            params = (poi_pic,)
            cur.execute(sql,params)
#        jingdian_gonglue = hxs.xpath('//div[@id="J-Wrap-geography_history"]').extract()
#        jingdian_gonglue2 = hxs.xpath('//section[@id="scene-middle-tab"]').extract()
#        for site in sites:
#            #simple template eg:anze
#            if jingdian_gonglue:
#                poi_pic = site.xpath('a/img/@src').extract()
#            #normal template eg:yonghegong
#            if jingdian_gonglue2:
#                poi_pic = site.xpath('div/meta/@content').extract()
##                content = os.popen('curl %s'% response.url).read()
##                poi_lightspot_title = re.compile(r'title',re.S).search(content)
##                print poi_lightspot_title.groups()
##                poi_lightspot_title = site.xpath('div').extract()
##                poi_lightspot_desc = site.xpath('div').extract()
#                print poi_pic
#        if jingdian_gonglue2:
#            menpiao = hxs.xpath('//div[@id="J-aside-info-price"]/div/p/text()').extract()
#            open_time = hxs.xpath('//div[@class="val opening_hours-value"]').extract()
#            addr = hxs.xpath('//div[@id="J-aside-info-address"]/span[2]/text()').extract()
#            suggest_play_time = hxs.xpath('//div[@id="J-aside-info-recommend_visit_time"]/span[@class="val recommend_visit_time-value"]/text()').extract()
#            phone = hxs.xpath('//div[@id="J-aside-info-phone"]/span[@class="val phone-value"]/text()').extract()
#            print menpiao,open_time,addr,phone