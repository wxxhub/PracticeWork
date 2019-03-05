import urllib.request
from bs4 import BeautifulSoup

url = "https://www.i4.cn/ring_1_0_1.html"

html = urllib.request.urlopen(url)

if html.getcode() == 200:
    data = html.read()
    file = open("01_爱思助手音乐下载.html","wb",1);
    file.write(data)
    file.close();
    soup = BeautifulSoup(data,"html.parser")
    title = soup.title
    link = soup.link
    div_01s =soup.find_all("div",attrs={"class":"options"})
    links = soup.find_all("link")
    print("中文本信息： ",title.string)
    print("标签的名称： ",title.name)

    print("标签信息：",link)
    print("link标签中href：",link["href"])
    print("父容器标签名称：",link.parent.name)

    print("文件中所有的link标签为:",links)
    print(len(links))
    
    print("=========遍历所有link_01标签=============")
    for link_01 in links:
        print(link_01)
        print(link_01["href"])
        print(link_01["rel"])
        pass
    pass

    print("=========遍历所有div_01s标签=============")
    print(div_01s)
    print("size of div_01s: ",len(div_01s))
    print(type(div_01s[0]))
else:
    print ("open "+url+" failed! "+str(html.getcode()))
    pass