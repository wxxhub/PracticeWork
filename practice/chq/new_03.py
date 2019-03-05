#使用Beautiful soup第三方库
import urllib.request;
from bs4 import BeautifulSoup;
#网络地址读取到本地
url ="https://www.i4.cn/ring_1_0_1.html";
html = urllib.request.urlopen(url);
if html.getcode() == 200:
    data = html.read();
    file = open("01_爱思助手音乐下载.html","wb",1);
    file.write(data)
    file.close();
    print("数据存储成功")
    pass
else:
    print("网络访问失败，返回码为：%d"%html.getcode())
    pass

html.close();

#========解析当前网站：Beautiful soup的使用=======
#创建一个soup对象
#第一个参数：网络源码数据; 第二个参数:解析器的模式：html.parser标准模式
soup = BeautifulSoup(data,"html.parser");
#获取标签选择器整体
title = soup.title;
print("标签内容：",title)
#获取标签中的内容
print("中文本信息:",title.string);
#获取标签的名称
print("标签的名称：",title.name);
#获取link标签内容
#通过标签获取的时候，默认查找第一数据
link =soup.link;
print("标签信息：",link)
#获取link标签中href对应的值
print("link标签中href:",link["href"]);
#查找标签的父容器标签名称
print("父容器标签名称：",link.parent.name);
#查询到所有的link标签
links = soup.find_all("link");
#得到一个数组格式
print("文件中所有的link标签为：",links)
print(len(links))
print("遍历所有link标签")
for link_01 in links:
    print(link_01)
    print(link_01["href"])
    pass
#只匹配全文第一个数据：可以添加条件
#rel="shortcut icon"/
link_02 = soup.find("link",attrs={"rel":"shortcut icon"});
print("条件查询：",link_02);
#查询
div_01s =soup.find_all("div",attrs={"class":"options"});
print(div_01s)
print(len(div_01s))
div_02s = div_01s[0].find_all("div",attrs={"class":"list"});
print(div_02s)
print(len(div_02s))
#循环输出文字
for name in div_02s:
    print(name.string);
    pass





