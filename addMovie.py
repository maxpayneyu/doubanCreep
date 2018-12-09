#!/usr/bin/python3
 
print("Hello, World!")

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
print ("False") 

input("\n\n按下 enter 键后退出。")


import re
import requests
import pymysql
import random
import time
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#获取资源并下载
def resp(listURL):
    #连接数据库
    conn = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '3569168',  #数据库密码请根据自身实际密码输入
        database = 'world', 
        charset = 'utf8'
    )
 
    #创建数据库游标
    cursor = conn.cursor()
 
    #创建列表t_movieTOP250（执行sql语句）
    cursor.execute('SELECT * FROM world.t_moviemine')
    #cursor.execute('create table t_movieMine(id INT PRIMARY KEY auto_increment NOT NULL ,movieCode VARCHAR(20) NOT NULL,movieName VARCHAR(200) NOT NULL ,pictrue_address VARCHAR(100))')

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive'}
##    cookies = {'cookie': 'bid=lRMSGS5Kzl8; ue="645247978@qq.com"; __yadk_uid=5Dvpex1kFtIj3I5it17pX079qWPDFLH1; push_noty_num=0; push_doumail_num=0; ll="108296"; _vwo_uuid_v2=D7524D8728538399059CC0C88099FE99A|68f6c840f24d7b5b9a4623a1557a3be4;+\
##               douban-fav-remind=1; gr_user_id=0221eade-5263-47d5-ad8e-6c5c56e04571; douban-profile-remind=1; _ga=GA1.2.195835846.1532935690; ct=y; refer_url=https://read.douban.com/?dcs=login&dcm=anonymous;+\
##               ps=y; _gid=GA1.2.1239701197.1543899775; __utmc=30149280; __utmv=30149280.4591; __utmz=30149280.1543912514.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/54822305/;+\
##               _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1543978023%2C%22https%3A%2F%2Fshanghai.douban.com%2Fevents%2Fweek-1101%3Fstart%3D20%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.195835846.1532935690.1543912514.1543978027.4;+\
##               _pk_id.100001.8cb4=c062f47c88c6bc72.1531214676.119.1543979878.1543916495.; __utmt=1; __utmb=30149280.18.10.1543978027; _gat_UA-7019765-1=1; dbcl2="45911446:74lVttWqKD8"'} #xxx是刚才保存的cookies信息，粘贴在这里
    #朋克已死的cookie
    cookies = {'cookie': 'gr_user_id=22fb76de-643b-45f9-ac7a-a62ca62b684f; __yadk_uid=FDej9xQLULdl3UQO25ccCaEQPWAsSrWo; douban-fav-remind=1; douban-profile-remind=1; ll="108296"; bid=SCRbn6fSziw; _ga=GA1.2.1939067050.1473521379;+\
_vwo_uuid_v2=570ED5F77946F638D57363B406657D0C|0c286db34269d08f6cea0f24a723a225; push_noty_num=0; push_doumail_num=0; ct=y; _gid=GA1.2.455787615.1544193827; ps=y; __utmc=30149280; ue="yuxinmax@163.com"; dbcl2="188413228:En3X9nAVjAs";+\
ck=97fz; __utma=30149280.1939067050.1473521379.1544193851.1544243396.77; __utmz=30149280.1544243396.77.54.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; ap_v=0,6.0;+\
_pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1544243401%2C%22https%3A%2F%2Fmovie.douban.com%2Fcelebrity%2F1274278%2F%22%5D;+\
_pk_ses.100001.8cb4=*; __utmt=1; __utmv=30149280.18841; __utmb=30149280.12.10.1544243396; _pk_id.100001.8cb4=b7d981f717b774c4.1473521376.510.1544243768.1544197483.'} #xxx是刚才保存的cookies信息，粘贴在这里
    
    try:
        # 爬取数据
        for urlPath in listURL:
            # 获取网页源代码
            #response = requests.get(urlPath,verify=False,cookies = cookies,  headers = headers)
            #html = response.text
            data={'ck': '97fz',
                'interest': 'collect',
                'rating': '5',
                'foldcollect': 'F'}
            response = requests.post(urlPath,verify=False,cookies = cookies,  headers = headers,data=data)
 
##            # 正则表达式
##            namePat = r'class="">+\
##                            <em>(.*?)</em>'
##            imgPat = r'src="(.*?)" class='
##            codePat = r'href="https://movie.douban.com/subject/(.*?)/" class="nbg">'
## 
##            # 匹配正则（排名【用数据库中id代替，自动生成及排序】、电影名、电影海报（图片地址））
##            res1 = re.compile(codePat)
##            res2 = re.compile(namePat)
##            res3 = re.compile(imgPat)
##            textList1 = res1.findall(html)
##            textList2 = res2.findall(html)
##            textList3 = res3.findall(html)
##            print(str(len(textList2))+' '+str(len(textList3)))
##            
##            # 遍历列表中元素,并将数据存入数据库
##            for i in range(len(textList1)):
##                cursor.execute('insert into t_movieMine(movieCode,movieName,pictrue_address) VALUES("%s","%s","%s")' % (textList1[i],textList2[i],textList3[i]))
 
        #从游标中获取结果
        cursor.fetchall()
 
        #提交结果
        conn.commit()
        print("结果已提交"+urlPath)
 
    except Exception as e:
        #数据回滚
        #conn.rollback()
        print(str(response.status_code)+"数据已回滚"+str(e))
 
    #关闭数据库
    conn.close()
 
#top250所有网页网址
def page(url,p_total):
    #连接数据库
    conn = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '3569168',  #数据库密码请根据自身实际密码输入
        database = 'world', 
        charset = 'utf8'
    )
 
    #创建数据库游标
    cursor = conn.cursor()
 
    #创建列表t_movieTOP250（执行sql语句）
    cursor.execute('SELECT movieCode FROM world.t_moviemine')
    result = cursor.fetchone()
    while result!=None:
        print(result)
        urlList = []
        urlList.append(url+str(result[0])+'/interest')
        resp(urlList)
        result = cursor.fetchone()
        time.sleep(3)
        
    urlList = []
    for i in range((p_total//15)+1):
        num = str(15*i)
        #pagePat = r'?start=' + num + '&filter='
        pagePat = num
        urL = url+pagePat
        urlList.append(urL)
    return urlList

##import win32api
##import win32con
##import win32gui
##def mouse_click(x=None,y=None):
##    if not x is None and not y is None:
##        mouse_move(x,y)
##        time.sleep(0.05)
##    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
##    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
if __name__ == '__main__':
    url = r"https://movie.douban.com/j/subject/"
    total=759
    listURL = page(url,total)
    

