
# 在使用Beautiful soup第三方，必须要加载到本项目的开发环境中
# 【1】===导包-urllib====
import urllib.request;
from bs4 import BeautifulSoup;
# 【2】===目标网址====
url = "https://www.i4.cn/ring_1_0_1.html";
# 【3】===把网址读取到本地
html = urllib.request.urlopen(url);
# 【4】===判断网络状态的返回码===
if html.getcode() == 200:
    # 【5】===读取网址信息
    data = html.read();
    # 【6】===本地存储
    file = open("01_爱思助手音乐下载.html","wb",1);
    file.write(data)
    file.close();
    print("数据存储成功;")
    pass
else:
    print("网络访问失败，返回码为：%d"%html.getcode())
    pass
# 【7】===关闭网络
html.close();
# =====================解析当前网站：Beautiful soup的使用===================
# soup = BeautifulSoup(open("01_爱思助手音乐下载.html"))
# 1.创建一个soup对象
# 第一个参数：网页源码数据：第二参数：解析器的模式:html.parser标准模式
soup = BeautifulSoup(data,"html.parser");
# 2.获取标签选择器整体：
title = soup.title;
print("标签内容：",title)
#  <title>苹果铃声_苹果铃声下载_苹果铃声免费下载_资源中心</title>
# 3.获取标签中的内容
print("中文本信息：",title.string);
# 4.获取标签的名称
print("标签的名称：",title.name);
#获取link标签内容
# 【注意】通过标签获取的时候，默认查找第一个数据；
link = soup.link;
print("标签信息：",link)
# 5.获取link标签中href对应的值
print("link标签中href：",link["href"]);
# 6.查找标签的父容器标签名称
print("父容器标签名称：",link.parent.name);
# 7.查询到所有的link标签
links = soup.find_all("link");
# 会得到一个数组格式
print("文件中所有的link标签为:",links)
print(len(links))
print("=========遍历所有link标签=============")
for link_01 in links:
    print(link_01)
    print(link_01["href"])
    pass
# 8.只匹配全文中第一个数据:可以添加条件
# rel="shortcut icon"/
link_02 = soup.find("link",attrs={"rel":"shortcut icon"});
print("条件查询：",link_02);
# 查询
div_01s =soup.find_all("div",attrs={"class":"options"});
print(div_01s)
print(len(div_01s))
print(type(div_01s[0]))
div_02s = div_01s[0].find_all("div",attrs={"class":"list"});
print(div_02s)
print(len(div_02s))
# 循环输出文字
for name in div_02s:
    print(name.string);
    pass



















