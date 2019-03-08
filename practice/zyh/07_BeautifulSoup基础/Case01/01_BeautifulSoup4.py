import urllib.request;
from bs4 import BeautifulSoup;

url = "https://www.i4.cn/ring_1_0_1.html";
html = urllib.request.urlopen(url);
if html.getcode() == 200:
    data = html.read();
    file = open("爱思助手音乐.html","wb",1);
    file.write(data);
    file.close();
    print("存储成功");
    pass;
else:
    print("访问失败，返回码为%d"%html.getcode());
html.close();
soup = BeautifulSoup(data,"html.parser");
title = soup.title;
print("title:",title);
print("内容:",title.string);
print("标签:",title.name);
link = soup.find_all("link");
for links in link:
    print(links);
    pass;
link_02 = soup.find_all("link",attrs={"rel":"shortcut"});
print("chaxun:",link_02);
divs = soup.find_all("div",attrs={"class":"list"});
print(len(divs));
for div in divs:
    print(div.string);
    pass;