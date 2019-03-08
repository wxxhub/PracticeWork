"""
1、确定网页url
2、利用url建立连接
    request = requests.get(url)
    request = urllib.request.urlopen(url)
3、打开网页源代码
    data = request.text
    data = request.read()
4、定位某个数据的位置（利用HTML标签定位）
    urllib利用正则表达式对网页代码进行匹配，将匹配后的url循环访问或者下载
    BeautifulSoup步骤
    创建soup变量 soup = BeautifulSoup（data（网页代码），html.parser（解码方式））
    利用find方法查找对应元素所在的HTML标签位置
    目标 = soup.find("标签(例如div)"，attrs = {"标签中特定属性，例如id或class":"id或class在标签中的值"})
    若要提取某标签中特定元素的值，例如href的值，则与访问数组类似，目标.["属性名"]
"""


import requests;
from bs4 import BeautifulSoup;
import os;

url = "https://www.biqukan.com/%s/";

# ==========================获取章节内容====================
def Get_text(title,url,header):
    requests.g
    requests_02 = requests.get(url,header);
    if requests_02.status_code == 200:
        requests_02.encoding = "gdk";
        data = requests_02.text;
        soup = BeautifulSoup(data,"html.parser");
        xiaoshuo_text = soup.find("div",attrs={"id":"content"}).get_text();
        file_xiaoshuo = open("%s.txt"%title,"w",1);
        file_xiaoshuo.write(str(xiaoshuo_text).replace("\xa0",""));
        print(xiaoshuo_text);
        pass;
    else:
        print("%s连接失败：%d"%(title,requests_02.status_code));
    pass;


# ===================获取目录==========================
def Get_mulu(url,xiaoshuo_name,header):
    requests_01 = requests.get(url,header);
    if(requests_01.status_code == 200):
        print("连接成功！");
        print("编码格式为：",requests_01.encoding);
        requests_01.encoding = "gbk";
        data = requests_01.text;
        file_path = "C:\/Users\/dell\/Desktop\/python实训\/代码\/Python\/爬虫基础_小说爬取\/%s\/"%xiaoshuo_name;
        if not os.path.exists(file_path):
            os.makedirs(file_path);
            pass;
        file_xiaoshuo = open("%s%s.html" % (file_path, xiaoshuo_name), "w", 1);
        file_xiaoshuo.write(data);
        file_xiaoshuo.close();
        print("已保存到本地文件中");

    #     解析数据
        soup = BeautifulSoup(data,"html.parser");
        div_listmain = soup.find("div",attrs={"class":"listmain"});
        div_01 = div_listmain.dl;
        i = 1;
        start_down = False;
        for div_dd in div_01:
            if div_dd == "\n":
                pass;
            elif div_dd.string.replace(" ","") == "《道君》正文卷":
                start_down = True;
                pass;
            elif start_down:
                # print("第%d行数据：%s" % (i, div_dd));
                title = div_dd.string;
                title_url = "https://www.biqukan.com"+div_dd.a["href"]
                print("%s下载地址 %s"%(title,title_url));
                Get_text(title,title_url,header);
                pass;
            i+=1;
            pass;
        pass;
    else:
        print("连接错误：",requests_01.status_code);
        pass;
    pass;




if __name__ == "__main__":
    print("=======进入程序========")
    print("welcome!")
    print("本软件目前只支持http://www.biqukan.com小说网站");
    print("请输入小说编号，格式为:(37_37651)");
    xiaoshuo_code = input();
    print("输入小说名称：");
    xiaoshuo_name = input();
    url = url%xiaoshuo_code;
    print("小说地址为：",url);
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
    Get_mulu(url,xiaoshuo_name.replace(" ", ""),header);
    pass;