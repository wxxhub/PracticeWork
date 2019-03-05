
# 【1】====导入包
import urllib.request;
from bs4 import BeautifulSoup;
import os
# 【2】===目标网址
url = "https://www.i4.cn/ring_23_0_1.html"
# 【3】===网络链接-检查网络
# 创建一个遍历判断是否已经有文件
# 变量暂时存储网络数据或文档数据
data = "";

if os.path.exists("爱思助手2.html"):
    print("文件已经存储：不用继续链接");
    file_01 = open("爱思助手2.html","rb",1);
    data = file_01.read();
    print(data);

    pass
else:
    html = urllib.request.urlopen(url);
    if html.getcode() == 200:
        data = html.read();
        print(data)
        file = open("爱思助手2.html", "wb", 1);
        file.write(data);
        file.close();
        pass
    else:
        print("网络访问异常！！！")
        pass
    html.close();
    pass

def Get_data_mp3(data):
    # 1.将数据转换成soup类型
    soup = BeautifulSoup(data,"html.parser");
    #2.查找相同数据
    divs_mp3 = soup.find_all("div",attrs={"class":"list ring_list"});
    # print("===========================\n",divs_mp3);
    print("音乐数目：",len(divs_mp3));
    # 查询出每一条音乐
    i = 1;
    for div_mp3_item in divs_mp3:
        print("第%d条音乐：%s"%(i,"=================================="));
        # 01.获取音乐名称：iPhone超赞铃声 - 大自然的声音
        mp3_name = div_mp3_item.find("div",attrs={"class":"title"})["title"];
        print("第%d首音乐名称：%s"%(i,mp3_name));
        # 02.下载量：
        mp3_downcount = div_mp3_item.find("div",attrs={"class":"downcount"}).string;
        print("第%d首音乐下载量：%s" % (i, mp3_downcount));
        # 03.音乐时长：
        mp3_longtime = div_mp3_item.find("div", attrs={"class": "longtime"}).string;
        print("第%d首音乐下载量：%s" % (i, mp3_longtime));
        # 04.音乐mp3文件：
        mp3_url = div_mp3_item.find("div", attrs={"class": "btn audio_play"})["data-mp3"];
        print("第%d首音乐下载地址：%s" % (i, mp3_url));
        # 存储到本地目录
        mp3_file = open("爱思助手-铃声目录.txt","a",1,encoding="utf-8");
        mp3_file.write("音乐名称：%s  下载量：%s  时长：%s  下载地址:%s\n"%(mp3_name,mp3_downcount,mp3_longtime,mp3_url))
        # 铃声本地存储：
        file_path = "07_Beautiful_爱思助手MP3\/Case01\/mp3\/"
        if not os.path.exists(file_path):
            os.makedirs(file_path);
            pass
        urllib.request.urlretrieve(mp3_url,"%s%s.mp3"%(file_path,mp3_name));
        print("第%d首音乐下载完毕。。。")


        i+=1;
        pass




    pass
# 调用函数
Get_data_mp3(data);









