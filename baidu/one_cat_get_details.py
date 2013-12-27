#coding:utf-8
import urllib2
import MySQLdb
import time
import json
#sql = 'insert into baidu_poi(province_url,one_cat_url,one_cat_rank,one_cat_name,,city_pic,city_lightspot_title,city_lightspot_desc,city_desctiption) values(%s,%s,%s,%s,%s)'
def get_city_details():
    jingdian_url = 'http://lvyou.baidu.com/destination/ajax/allview?surl=%s&format=ajax&cid=0'
#    conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
    conn=MySQLdb.connect(host='54.201.192.244',user='qyer',passwd='qyer',db='mafengwo',port=3306,charset='utf8')
    cur=conn.cursor()
    cur.execute('select one_cat_url,id from baidu_poi where province_url is not null and one_cat_url is not null and two_cat_url is null and addr is null  and total_pingjia is null order by id')
    result = cur.fetchall()
    print result
    for k,cat_name in enumerate(result):
        ajax_url = jingdian_url%(cat_name[2])
        print cat_name[2],ajax_url
        try:
            res = urllib2.urlopen(ajax_url)
            json_data = json.loads(res.read())
        except Exception,e:
            print e
        finally:
            pass
        sql = 'update baidu_poi set jingdian_gonglue=%s where id=%s;'
        content =json.dumps(json_data['data']['content'])
        print content
        params = (content,cat_name[1])
        cur.execute(sql,params)
#        city_description = json_data['data']['ext']['abs_desc']
#        total_pingjia = ''
#        if 'more_desc' in json_data['data']['ext']:
#            total_pingjia = json_data['data']['ext']['more_desc']
#        if 'high_light_album' in json_data['data']:
#            if 'pic_list' in json_data['data']['high_light_album'] and len(json_data['data']['high_light_album']['pic_list']) > 1:
#                for pl in json_data['data']['high_light_album']['pic_list']:
#                    city_pic = 'http://hiphotos.baidu.com/lvpics/pic/item/%s.jpg'% pl['pic_url']
#                    city_lightspot_desc = pl['desc']
#                    if 'ext' in pl and 'title' in pl['ext']:
#                        city_lightspot_title = pl['ext']['title']
#                    else:
#                        city_lightspot_title = ''
#                    sql = 'insert into baidu_poi(province_url,one_cat_url,one_cat_rank,one_cat_name,city_pic,city_lightspot_title,city_lightspot_desc,city_description,total_pingjia) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#                    params = (one_cat_name[0],one_cat_name[2],one_cat_name[3],one_cat_name[4],city_pic,city_lightspot_title,city_lightspot_desc,city_description,total_pingjia)
#                    print params
#                    cur.execute(sql,params)
#                    print 'success'
#                    time.sleep(0.0001)
        print len(result)
        print 'running to:%s'%k
if __name__ == '__main__':
    get_city_details()