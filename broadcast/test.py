#!/usr/bin/python

import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)  #打开一个url
    html = page.read()  #读取全部内容生成一个字符串
    return html

def getImg(html):
    reg = r'src="(http://.+?\.jpg)"'
    
    imgre = re.compile(reg)   # 将一个正则表达式生成为响应的对象
    imglist = re.findall(imgre,html) # 从html字符串中找到符合imgre正则表达式的项，返回一个列表
    print(imglist)

    x = 0

    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%x)  #将网络内容取回本地并且重命名
        x+=1

html = getHtml('http://tieba.baidu.com/p/4229162765')

print (getImg(html))

