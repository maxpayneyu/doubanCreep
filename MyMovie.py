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


##respose=requests.get('https://www.douban.com/people/')
##
## print(respose.status_code)# 响应的状态码
## print(respose.content)  #返回字节信息
## print(respose.text)  #返回文本内容
##urls=re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)  #re.S 把文本信息转换成1行匹配
##url=urls[5]
##result=requests.get(url)
##mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]
##
##video=requests.get(mp4_url)
##
##with open('D:\\a.mp4','wb') as f:
##    f.write(video.content)

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
    #cursor.execute('SELECT * FROM world.t_moviemine')
    cursor.execute('create table t_movieMine(id INT PRIMARY KEY auto_increment NOT NULL ,movieCode VARCHAR(20) NOT NULL,movieName VARCHAR(200) NOT NULL ,pictrue_address VARCHAR(100))')

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive'}
##    cookies = {'cookie': 'bid=lRMSGS5Kzl8; ue="645247978@qq.com"; __yadk_uid=5Dvpex1kFtIj3I5it17pX079qWPDFLH1; push_noty_num=0; push_doumail_num=0; ll="108296"; _vwo_uuid_v2=D7524D8728538399059CC0C88099FE99A|68f6c840f24d7b5b9a4623a1557a3be4;+\
##               douban-fav-remind=1; gr_user_id=0221eade-5263-47d5-ad8e-6c5c56e04571; douban-profile-remind=1; _ga=GA1.2.195835846.1532935690; ct=y; refer_url=https://read.douban.com/?dcs=login&dcm=anonymous;+\
##               ps=y; _gid=GA1.2.1239701197.1543899775; __utmc=30149280; __utmv=30149280.4591; __utmz=30149280.1543912514.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/54822305/;+\
##               _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1543978023%2C%22https%3A%2F%2Fshanghai.douban.com%2Fevents%2Fweek-1101%3Fstart%3D20%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.195835846.1532935690.1543912514.1543978027.4;+\
##               _pk_id.100001.8cb4=c062f47c88c6bc72.1531214676.119.1543979878.1543916495.; __utmt=1; __utmb=30149280.18.10.1543978027; _gat_UA-7019765-1=1; dbcl2="45911446:74lVttWqKD8"'} #xxx是刚才保存的cookies信息，粘贴在这里
    cookies = {'cookie': 'bid=lRMSGS5Kzl8; ue="645247978@qq.com"; __yadk_uid=5Dvpex1kFtIj3I5it17pX079qWPDFLH1; push_noty_num=0; push_doumail_num=0; ll="108296"; _vwo_uuid_v2=D7524D8728538399059CC0C88099FE99A|68f6c840f24d7b5b9a4623a1557a3be4;+\
douban-fav-remind=1; gr_user_id=0221eade-5263-47d5-ad8e-6c5c56e04571; douban-profile-remind=1; _ga=GA1.2.195835846.1532935690; ct=y; ps=y; _gid=GA1.2.1239701197.1543899775; __utmv=30149280.4591; __utmc=30149280;+\
__utmz=30149280.1544087721.12.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/;+\
_pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1544162804%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3D645247978%2540qq.com%26redir%3Dhttps%253A%252F%252Fwww.douban.com%252F%26source%3Dindex_nav%26error%3D1013%22%5D;+\
_pk_ses.100001.8cb4=*; __utma=30149280.195835846.1532935690.1544157105.1544162808.15; __utmt=1;+\
_gat_UA-7019765-1=1; dbcl2="45911446:dKQXLbIaL2o"; ck=_MYr; _pk_id.100001.8cb4=c062f47c88c6bc72.1531214676.130.1544163656.1544158244.; __utmb=30149280.6.10.1544162808'} #xxx是刚才保存的cookies信息，粘贴在这里
    
    try:
        # 爬取数据
        for urlPath in listURL:
            # 获取网页源代码
            response = requests.get(urlPath,verify=False,cookies = cookies,  headers = headers)
            html = response.text
 
            # 正则表达式
            namePat = r'class="">+\
                            <em>(.*?)</em>'
            imgPat = r'src="(.*?)" class='
            codePat = r'href="https://movie.douban.com/subject/(.*?)/" class="nbg">'
 
            # 匹配正则（排名【用数据库中id代替，自动生成及排序】、电影名、电影海报（图片地址））
            res1 = re.compile(codePat)
            res2 = re.compile(namePat)
            res3 = re.compile(imgPat)
            textList1 = res1.findall(html)
            textList2 = res2.findall(html)
            textList3 = res3.findall(html)
            print(str(len(textList2))+' '+str(len(textList3)))
            
            # 遍历列表中元素,并将数据存入数据库
            for i in range(len(textList1)):
                cursor.execute('insert into t_movieMine(movieCode,movieName,pictrue_address) VALUES("%s","%s","%s")' % (textList1[i],textList2[i],textList3[i]))
 
        #从游标中获取结果
        cursor.fetchall()
 
        #提交结果
        conn.commit()
        print("结果已提交")
 
    except Exception as e:
        #数据回滚
        #conn.rollback()
        print(str(response.status_code)+"数据已回滚"+str(e))
 
    #关闭数据库
    conn.close()
 
#top250所有网页网址
def page(url,p_total):
    urlList = []
    for i in range((p_total//15)+1):
        num = str(15*i)
        #pagePat = r'?start=' + num + '&filter='
        pagePat = r'?start=' + num + '&sort=time&rating=all&filter=all&mode=grid'
        urL = url+pagePat
        urlList.append(urL)
    return urlList
 
 
if __name__ == '__main__':
    url = r"https://movie.douban.com/people/45911446/collect"
    total=759
    listURL = page(url,total)
    resp(listURL)

