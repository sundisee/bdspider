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
jingdian_url = 'http://lvyou.baidu.com/destination/ajax/allview?surl=%s&format=ajax&cid=0&pn=%s'
conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
cur=conn.cursor()
cur.execute('select province_url from baidu_poi')
result = cur.fetchall()
#jingdian_urls = [jingdian_url % i for i in result if i]
#判断有无重复
#print (jingdian_urls)
#print len(list(set(jingdian_urls)))
#jingdian_urls = list(set(jingdian_urls))
#cur.close()
#conn.close()

for k,province_url in enumerate(result):
    not_end_page = True
    start = 1
    while not_end_page:
        ajax_url = jingdian_url%(province_url[0],start)
        print province_url[0],ajax_url
        try:
            res = urllib2.urlopen(ajax_url)
            json_data = json.loads(res.read())
        except Exception,e:
            print e
        finally:
            pass
        i = 16*(start-1)+1
        if len(json_data['data']['scene_list']):
            for sc in json_data['data']['scene_list']:
                one_cat_url = sc['surl']
                one_cat_name = sc['sname']
        #        city_description = sc['data']['ext']['abs_desc']
                one_cat_rank = i
                i = i +1
                print one_cat_name,one_cat_url,one_cat_rank
        #        cur.execute('update  baidu_poi set one_cat_name = %s, one_cat_url = %s,one_cat_rank = %s where baidu_poi')
                sql = 'insert into baidu_poi(province_url,one_cat_name,one_cat_url,one_cat_rank) values(%s,%s,%s,%s)'
                params = (province_url[0],one_cat_name,one_cat_url,one_cat_rank)
                cur.execute(sql,params)
                print 'success'
                time.sleep(0.01)
            start = start +1
        else:
            not_end_page = False

#从db读取城市列表拼装景点url
#class ProvinceSpider(BaseSpider):
#    name = "poi_city"
#    allowed_domains = ["lvyou.baidu.com"]
#    start_urls = jingdian_urls
##    start_urls = ['http://lvyou.baidu.com/qitaihe/',]
#
#    def parse(self, response):
#        hxs = HtmlXPathSelector(response)
#        print response.read()
#        sites = hxs.xpath('//div[id="J_slide-holder"]')
#        print sites
#        for site in sites:
#            p = site.xpath('//text')
#            print p
#            url = site.select('ul/li/div[2]/h3/a/@href').extract()
#            name = site.select('ul/li/div[2]/h3/a/text()').extract()
#            city_id = re.search('\d+',response.url).group()
#            for i in zip(url,name):
#                sql = 'insert into poinfo(city_id,poi_id,poi_name,poi_type) values(%s,%s,%s,%s)'
#                poi_id = re.search('\d+',i[0]).group()
#                params = (city_id,poi_id,i[1],u'购物')
#                n = cur.execute(sql,params)
#                conn.commit()
#                #                print i[0],i[1]
                #            cur.close()
                #            conn.close()
#        last_page = hxs.select('//a[@class="last-page"]/@href').extract()
#        if last_page:
#            last_page =  int((last_page[0].split('-')[-1]).split('.')[0])
#            page_url = response.url+'0-0-0-0-0-2.html'
#            if int(last_page) > 1:
#                yield Request(url=page_url,callback=self.parse_page_url,meta={'i':2,'last_page':last_page})
#    def parse_page_url(self,response):
#    #        conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
#    #        cur=conn.cursor()
#        hxs = HtmlXPathSelector(response)
#        i = response.meta['i']
#        last_page = response.meta['last_page']
#        sites = hxs.select('//div[@class="shop-list"]')
#        city_id  = re.search('\d+',response.url).group()
#        for site in sites:
#            url = site.select('ul/li/div[2]/h3/a/@href').extract()
#            name = site.select('ul/li/div[2]/h3/a/text()').extract()
#            for un in zip(url,name):
#                sql = 'insert into poinfo(city_id,poi_id,poi_name,poi_type) values(%s,%s,%s,%s)'
#                poi_id = re.search('\d+',un[0]).group()
#                params = (city_id,poi_id,un[1],u'购物')
#                n = cur.execute(sql,params)
#                print n
#                print un[0],un[1]
#        page_base_url = 'http://www.mafengwo.cn/jd/%s/0-0-0-0-0-%s.html'
#        i = i+1
#        page_url = page_base_url % (city_id, i)
#        print last_page
#        if i <= last_page:
#            yield Request(url=page_url,callback=self.parse_page_url,meta={'i':i,'last_page':last_page})
