#coding:utf-8
import urllib2
import MySQLdb
import time
import json
def get_poi_details():
    jingdian_url = 'http://lvyou.baidu.com/destination/ajax/allview?surl=%s&format=ajax&cid=0'
    conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
    cur=conn.cursor()
    cur.execute('select three_cat_url,two_cat_url,two_cat_rank,two_cat_name,three_cat_name,three_cat_rank from baidu_poi where three_cat_url is not null and two_cat_url is not null and addr is null and total_pingjia is null  order by id')
    result = cur.fetchall()
    print len(result)
    for k,cat_name in enumerate(result[6326:]):
        ajax_url = jingdian_url%(cat_name[0])
        print cat_name[0],ajax_url
        try:
            res = urllib2.urlopen(ajax_url)
            json_data = json.loads(res.read())
        except Exception,e:
            print e
        finally:
            pass
        if 'ticket_info' in  json_data['data']['content']:
            if 'open_time_desc' in json_data['data']['content']['ticket_info']:
                open_time_desc = json_data['data']['content']['ticket_info']['open_time_desc']
            else:
                open_time_desc = ''
            if 'price_desc' in json_data['data']['content']['ticket_info']:
                price_desc = json_data['data']['content']['ticket_info']['price_desc']
            else:
                price_desc = ''
        else:
            open_time_desc = ''
            price_desc = ''
        addr = json_data['data']['ext']['address']
        total_pingjia = ''
        if 'more_desc' in json_data['data']['ext']:
            total_pingjia = json_data['data']['ext']['more_desc']
        simple_desc = more_desc = recommend_visit_time = ''
        if 'besttime' in json_data['data']['content']:
            if 'recommend_visit_time' in json_data['data']['content']['besttime']:
                recommend_visit_time = json_data['data']['content']['besttime']['recommend_visit_time']
            if 'simple_desc' in json_data['data']['content']['besttime']:
                simple_desc = json_data['data']['content']['besttime']['simple_desc']
            if 'more_desc' in json_data['data']['content']['besttime']:
                more_desc = json_data['data']['content']['besttime']['more_desc']
        if json_data and 'high_light_album' in json_data['data']:
            if 'pic_list' in json_data['data']['high_light_album'] and len(json_data['data']['high_light_album']['pic_list']) > 1:
                for pl in json_data['data']['high_light_album']['pic_list']:
                    if 'desc' in pl['desc']:
                        poi_lightspot_desc = pl['desc']
                    else:
                        poi_lightspot_desc = ''
                    poi_pic = 'http://hiphotos.baidu.com/lvpics/pic/item/%s.jpg'% pl['pic_url']
                    if 'ext' in pl and 'title' in pl['ext']:
                        poi_lightspot_title = pl['ext']['title']
                    else:
                        poi_lightspot_title = ''
                    print addr,open_time_desc,price_desc,simple_desc,more_desc,recommend_visit_time
                    sql = 'insert into baidu_poi(three_cat_url,two_cat_url,two_cat_rank,two_cat_name,three_cat_name,three_cat_rank,poi_pic,poi_lightspot_title,poi_lightspot_desc,addr,open_time_desc,price_desc,simple_desc,more_desc,recommend_visit_time,total_pingjia) \
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    params = (cat_name[0],cat_name[1],cat_name[2],cat_name[3],cat_name[4],cat_name[5],poi_pic,poi_lightspot_title,poi_lightspot_desc,addr,open_time_desc,price_desc,simple_desc,more_desc,recommend_visit_time,total_pingjia)
                    print params
                    cur.execute(sql,params)
                    print 'success'
                    time.sleep(0.01)
        else:
            need_spider = 1
            sql = 'insert into baidu_poi(three_cat_url,two_cat_url,two_cat_rank,two_cat_name,three_cat_name,three_cat_rank,addr,open_time_desc,price_desc,simple_desc,more_desc,recommend_visit_time,need_spider,total_pingjia) \
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            params = (cat_name[0],cat_name[1],cat_name[2],cat_name[3],cat_name[4],cat_name[5],addr,open_time_desc,price_desc,simple_desc,more_desc,recommend_visit_time,need_spider,total_pingjia)
            print params
            cur.execute(sql,params)
        print len(result)
        print 'running to:%s'%k
if __name__ == '__main__':
    get_poi_details()