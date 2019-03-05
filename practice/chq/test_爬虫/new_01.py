#urllib库的使用
#导入包
import urllib.request;
#设定目标网站
url ="https://www.i4.cn/ring_22_0_1.html"
#开始网络链接访问
html = urllib.request.urlopen(url)
#读取网站源码
data = html.read()
#将源码存储到本地项目
#由于数据为bytes所以写入方式: wb
file = open("01_urllib源码.html","wb",1)
#写入文件
file.write(data)
#关闭文件，关闭网络访问
file.close()
html.close()


#urllib 常规用法
#获取访问网站地址
print("当前访问网站的地址:%s"%html.geturl())

#获取网站状态的返回码:
print("当前访问网络的状态: %s"%html.getcode())
#网站中中文乱码
url_01 = "http://tieba.baidu.com/photo/p?kw=武汉工程大学%A6&tid=2125163782&pic_id=f8c5a0cc7cd98d106764055d213fb80e7aec90c6"
#乱码如何生成-加密
html_01 =urllib.request.quote(url_01)
print("生成的网络地址为: %s"%html_01)
#如何修正中文乱码--解码
html_02 =urllib.request.unquote(url_01)
print("解码后网站地址:"%html_02)
