#!/usr/bin/python3
 
print("Hello, World!")

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
print ("False") 

input("\n\n按下 enter 键后退出。")

##import sys
##print('================Python import mode==========================');
##print ('命令行参数为:')
##for i in sys.argv:
##    print (i)
##print ('\n python 路径为',sys.path)
##
##from sys import argv,path  #  导入特定的成员
## 
##print('================python from import===================================')
##print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


import re
import requests
import pymysql
import random


#respose=requests.get('https://www.douban.com/people/')

# print(respose.status_code)# 响应的状态码
# print(respose.content)  #返回字节信息
# print(respose.text)  #返回文本内容
##urls=re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)  #re.S 把文本信息转换成1行匹配
##url=urls[5]
##result=requests.get(url)
##mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]
##
##video=requests.get(mp4_url)
##
##with open('D:\\a.mp4','wb') as f:
##    f.write(video.content)

###获取资源并下载
##def resp(listURL):
##    #连接数据库
##    conn = pymysql.connect(
##        host = 'localhost',
##        port = 3306,
##        user = 'root',
##        password = '3569168',  #数据库密码请根据自身实际密码输入
##        database = 'world', 
##        charset = 'utf8'
##    )
## 
##    #创建数据库游标
##    cursor = conn.cursor()
## 
##    #创建列表t_movieTOP250（执行sql语句）
##    cursor.execute('create table t_movieTOP250(id INT PRIMARY KEY auto_increment NOT NULL ,movieName VARCHAR(20) NOT NULL ,pictrue_address VARCHAR(100))')
## 
##    try:
##        # 爬取数据
##        for urlPath in listURL:
##            # 获取网页源代码
##            response = requests.get(urlPath)
##            html = response.text
## 
##            # 正则表达式
##            namePat = r'alt="(.*?)" src='
##            imgPat = r'src="(.*?)" class='
## 
##            # 匹配正则（排名【用数据库中id代替，自动生成及排序】、电影名、电影海报（图片地址））
##            res2 = re.compile(namePat)
##            res3 = re.compile(imgPat)
##            textList2 = res2.findall(html)
##            textList3 = res3.findall(html)
## 
##            # 遍历列表中元素,并将数据存入数据库
##            for i in range(len(textList3)):
##                cursor.execute('insert into t_movieTOP250(movieName,pictrue_address) VALUES("%s","%s")' % (textList2[i],textList3[i]))
## 
##        #从游标中获取结果
##        cursor.fetchall()
## 
##        #提交结果
##        conn.commit()
##        print("结果已提交")
## 
##    except Exception as e:
##        #数据回滚
##        conn.rollback()
##        print("数据已回滚")
## 
##    #关闭数据库
##    conn.close()
## 
###top250所有网页网址
##def page(url):
##    urlList = []
##    for i in range(10):
##        num = str(25*i)
##        pagePat = r'?start=' + num + '&filter='
##        urL = url+pagePat
##        urlList.append(urL)
##    return urlList
## 
## 
##if __name__ == '__main__':
##    url = r"https://movie.douban.com/top250"
##    listURL = page(url)
##    resp(listURL)

import time
import sys



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
    #cursor.execute('create table t_usersInDouban(id INT PRIMARY KEY auto_increment NOT NULL ,movieName VARCHAR(200) NOT NULL ,pictrue_address VARCHAR(1000))')
    cursor.execute('select * from t_usersInDouban')

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
##    cookies = {'cookie': 'bid=lRMSGS5Kzl8; ue="645247978@qq.com"; __yadk_uid=5Dvpex1kFtIj3I5it17pX079qWPDFLH1; push_noty_num=0; push_doumail_num=0; ll="108296"; _vwo_uuid_v2=D7524D8728538399059CC0C88099FE99A|68f6c840f24d7b5b9a4623a1557a3be4;+\
##               douban-fav-remind=1; gr_user_id=0221eade-5263-47d5-ad8e-6c5c56e04571; douban-profile-remind=1; _ga=GA1.2.195835846.1532935690; ct=y; refer_url=https://read.douban.com/?dcs=login&dcm=anonymous;+\
##               ps=y; _gid=GA1.2.1239701197.1543899775; __utmc=30149280; __utmv=30149280.4591; __utmz=30149280.1543912514.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/54822305/;+\
##               _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1543978023%2C%22https%3A%2F%2Fshanghai.douban.com%2Fevents%2Fweek-1101%3Fstart%3D20%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.195835846.1532935690.1543912514.1543978027.4;+\
##               _pk_id.100001.8cb4=c062f47c88c6bc72.1531214676.119.1543979878.1543916495.; __utmt=1; __utmb=30149280.18.10.1543978027; _gat_UA-7019765-1=1; dbcl2="45911446:74lVttWqKD8"'} #xxx是刚才保存的cookies信息，粘贴在这里
    cookies = {'cookie': 'bid=lRMSGS5Kzl8; ue="645247978@qq.com"; __yadk_uid=5Dvpex1kFtIj3I5it17pX079qWPDFLH1; push_noty_num=0; push_doumail_num=0; ll="108296"; _vwo_uuid_v2=D7524D8728538399059CC0C88099FE99A|68f6c840f24d7b5b9a4623a1557a3be4;+\
douban-fav-remind=1; gr_user_id=0221eade-5263-47d5-ad8e-6c5c56e04571; douban-profile-remind=1; _ga=GA1.2.195835846.1532935690; ct=y; ps=y; _gid=GA1.2.1239701197.1543899775; __utmv=30149280.4591;+\
__utmz=30149280.1543912514.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/54822305/; __utmc=30149280; ap_v=0,6.0;+\
_pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1544066611%2C%22https%3A%2F%2Fshanghai.douban.com%2Fevents%2Fweek-1101%3Fstart%3D20%22%5D; _pk_ses.100001.8cb4=*;+\
__utma=30149280.195835846.1532935690.1544060310.1544066613.9; __utmt=1; dbcl2="45911446:eWnA+KOIvdY"; ck=5ePc; _pk_id.100001.8cb4=c062f47c88c6bc72.1531214676.124.1544066691.1544060411.; __utmb=30149280.3.10.1544066613'} #xxx是刚才保存的cookies信息，粘贴在这里
                        
    #r = requests.get(url, cookies = cookies, headers = headers)
    #用不同IP去访问要爬去的网站

    #在https://proxy.coderbusy.com/找到的IP地址（不停刷新即可）
    pro=['122.152.196.126','114.215.174.227','119.185.30.75']
##    #头信息
##    head={
##     'user-Agent':'Mozilla/5.0(Windows NT 10.0;Win64 x64)AppleWebkit/537.36(KHTML,like Gecko) chrome/58.0.3029.110 Safari/537.36'
##    }
##    url='http://www.whatismyip.com.tw/'
##    r=requests.get(url,proxies={'http':random.choice(pro)},headers=head)
##    #用随机生成的一个IP去访问这个网页
##    r.encoding=r.apparent_encoding
##    print(r.status_code)
##    print(r.text)
    randomchoice=random.choice(pro)
        # 爬取数据
    for urlPath in listURL:
        try:
            
            # 获取网页源代码
            response = requests.get(urlPath,proxies={'http':randomchoice}, cookies = cookies, headers = headers)
            html = response.text
##            captcha=response.xpath('//*[@id="captcha_image"]/@src').extract()  #获取验证码图片的链接
##            print(captcha)
##            if len(captcha)>0:
##                
##                #人工输入验证码
##                #urllib.urlretrieve(captcha[0],filename="C:/Users/pujinxiao/Desktop/learn/douban20170405/douban/douban/spiders/captcha.png")
##                #captcha_value=raw_input('查看captcha.png,有验证码请输入:')
##     
##                #用快若打码平台处理验证码--------验证码是任意长度字母，成功率较低
##                captcha_value=ruokuai.get_captcha(captcha[0])
##                reg=r'<Result>(.*?)</Result>'
##                reg=re.compile(reg)
##                captcha_value=re.findall(reg,captcha_value)[0]
##                print('验证码为：'+captcha_value)
##     
##                data={
##                     "form_email": "645247978@qq.com",
##                     "form_password": "max3569168",
##                     "captcha-solution": captcha_value,
##                     #"redir": "https://www.douban.com/people/151968962/",      #设置需要转向的网址，由于我们需要爬取个人中心页，所以转向个人中心页
##                }

            # 正则表达式
            #namePat = r'alt="(.*?)" src='
            #imgPat = r'src="(.*?)" class='
            numPat = r'共同的喜好\((.*?)\)'
            namePat = r'alt="(.*?)"/>'
            imgPat = r'">(.*?)</a><br />'
            # 匹配正则（排名【用数据库中id代替，自动生成及排序】、电影名、电影海报（图片地址））
            res1 = re.compile(numPat)
            res2 = re.compile(namePat)
            res3 = re.compile(imgPat)
            textList1 = res1.findall(html)
            textList2 = res2.findall(html)
            textList3 = res3.findall(html)
            #print(html)
            #with open(r'C:\douban.txt', 'wb+') as f:
            #    f.write(response.content) #把登陆主页后返回的数据保存到文件中
            print(str(len(textList1))+' ID='+urlPath+' 代理：'+randomchoice)
            if response.status_code==200 or response.status_code==404:
                if len(textList1)>0 :
    ##                with open(r'C:\douban.txt', 'wb+') as f:
    ##                    f.write(response.content) #把登陆主页后返回的数据保存到文件中
                    # 遍历列表中元素,并将数据存入数据库
                    for i in range(len(textList1)):
                        print(str(textList1[i])+' ID='+urlPath)
                        if len(textList2)>0 and len(textList3)>0 :
                            print('insert into t_usersInDouban(same,movieName,pictrue_address,user) VALUES("%s","%s","%s","%s")' % (textList1[i],textList2[i],textList3[i],urlPath))
                            cursor.execute('insert into t_usersInDouban(same,movieName,pictrue_address,user) VALUES("%s","%s","%s","%s")' % (textList1[i],textList2[i],textList3[i],urlPath))
            else:
                print("cookie失效:"+str(response.status_code))
                time.sleep(10)
                input("\n\n按下 enter 键后退出。")
                #sys.exit()
                #response = requests.get(urlPath)

            #生成随机数，浮点类型
            a = random.uniform(1, 4)
            #控制随机数的精度round(数值，精度)
            b=round(a, 2)+1    
            time.sleep(b)    
 
            #从游标中获取结果
            cursor.fetchall()
     
            #提交结果
            conn.commit()
            print("结果已提交,等待"+str(b))
 
        except Exception as e:
            #数据回滚
            #conn.rollback()
            response = requests.get(r"https://www.douban.com")
            print(str(response.status_code)+"数据已回滚"+str(e))
            time.sleep(10)
            #换个IP
            randomchoice=random.choice(pro)
 
    #关闭数据库
    conn.close()
 
#遍历区间内的豆瓣ID
def page(url,default):
    urlList = []
    lista=[i for i in range(100)]
    #print lista 
    #随机后
    random.shuffle(lista)
    #print lista
    for i in lista:
        pagePat = str(default+i+1)
        urL = url+pagePat
        urlList.append(urL)
    
##    for i in range(default,default+100):
##    #for i in range(14822305,76822308):    
##        pagePat = str(i)
##        urL = url+pagePat
##        urlList.append(urL)
    return urlList
 
 
if __name__ == '__main__':
##    url = r"https://www.douban.com/people/54822305"14822505
##    urlList = []
##    urlList.append(url)
##    resp(urlList)
    
    url = r"https://www.douban.com/people/"
    urlList = []
    urlList.append(url)
    default=54822305
    for i in range(200000):
        default=default+i*100
        listURL = page(url,default)
        print("url收集完毕")
        resp(listURL)
        #input("\n\n按下 enter 键后退出。")

##headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
##cookies = {'cookie': 'bid=lRMSGS5Kzl8; ue="645247978@qq.com"; __yadk_uid=5Dvpex1kFtIj3I5it17pX079qWPDFLH1; push_noty_num=0; push_doumail_num=0; ll="108296"; _vwo_uuid_v2=D7524D8728538399059CC0C88099FE99A|68f6c840f24d7b5b9a4623a1557a3be4;+\
##           douban-fav-remind=1; gr_user_id=0221eade-5263-47d5-ad8e-6c5c56e04571; douban-profile-remind=1; _ga=GA1.2.195835846.1532935690; ct=y; refer_url=https://read.douban.com/?dcs=login&dcm=anonymous;+\
##           ps=y; _gid=GA1.2.1239701197.1543899775; __utmc=30149280; __utmv=30149280.4591; __utmz=30149280.1543912514.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/54822305/;+\
##           _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1543978023%2C%22https%3A%2F%2Fshanghai.douban.com%2Fevents%2Fweek-1101%3Fstart%3D20%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.195835846.1532935690.1543912514.1543978027.4;+\
##           _pk_id.100001.8cb4=c062f47c88c6bc72.1531214676.119.1543979878.1543916495.; __utmt=1; __utmb=30149280.18.10.1543978027; _gat_UA-7019765-1=1; dbcl2="45911446:74lVttWqKD8"'} #xxx是刚才保存的cookies信息，粘贴在这里
##url = 'https://www.douban.com'
##r = requests.get(url, cookies = cookies, headers = headers)
##with open(r'C:\douban.txt', 'wb+') as f:
##    f.write(r.content) #把登陆主页后返回的数据保存到文件中


input("\n\n按下 enter 键后退出。")
