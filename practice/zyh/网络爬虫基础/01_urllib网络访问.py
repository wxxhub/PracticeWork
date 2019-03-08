
# 【1】===urllib库的使用===
# 导入包
import urllib.request;
# python2.x中使用
# import urllib,urllib2;
# 【2】===设定目标网址====
url = "https://www.i4.cn/ring_22_0_1.html";
# 【3】===开始网络链接访问===
html = urllib.request.urlopen(url);
# 【4】===读取网站源码===
data =html.read();
# 【5】===将源码存储到本地项目中===
# 由于data数据为bytes所有写入方式：wb
file = open("01_爱思助手.html","wb",1);
# 【6】===写入文件===
file.write(data);
# 【6】===关闭文件，关闭网络访问===
file.close();
html.close();

# ========================urllib常规用法======================
# 【1】===获取访问网站的网址===
print("当前访问的网址：%s"%html.geturl());
# 获取网站网络状态的返回码:
print("访问网络的状态：%s"%html.getcode());
# 网站中中文乱码
url_01 = "http://tieba.baidu.com/photo/p?kw=武汉工程大学%A6&tid=2125163782&pic_id=f8c5a0cc7cd98d106764055d213fb80e7aec90c6"
# 乱码如何生产 - 加密
html_01 = urllib.request.quote(url_01);
print("生产的网络地址为：%s"%html_01);
# 如何修正中文乱码问题---解码
html_02 = urllib.request.unquote(html_01);
print("解码后的网站地址：%s"%html_02)
















