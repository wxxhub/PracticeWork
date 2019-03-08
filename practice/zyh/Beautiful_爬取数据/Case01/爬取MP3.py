import urllib.request
import os
from bs4 import BeautifulSoup
url = "https://www.i4.cn/ring_3_0_1.html";
html = urllib.request.urlopen(url);
if os.path.exists("铃声.html"):
    print("网页已连接！");
    data = html.read();
    pass;
else:
    if html.getcode() == 200:
        print("访问成功！");
        data = html.read();
        file = open("铃声.html","wb",1)
        file.write(data);
        pass;
    else:
        print("访问异常");
        pass;
pass;
def Get_MP3(data):
    soup = BeautifulSoup(data,"html.parser");
    divs_mp3 = soup.find_all("div",attrs={"class":"list ring_list"});
    file_path = "C:\/Users\/dell\/Desktop\/python实训\/代码\/Python\/Beautiful\/MP3";
    i = 1;
    for div_mp3 in divs_mp3:
        div_name = div_mp3.find("div",attrs = {"class":"title"})["title"];
        print("第%d条音乐:%s"%(i,div_name));
        div_downcount = div_mp3.find("div",attrs = {"class":"downcount"}).string;
        print("下载次数:%s"%div_downcount);
        div_time = div_mp3.find("div",attrs = {"class":"longtime"}).string;
        print("时长:%s"%div_time);
        div_url = div_mp3.find("div",attrs = {"class":"btn audio_play"})["data-mp3"]
        print("下载地址:%s"%div_url);
        mp3_file = open("C:\/Users\/dell\/Desktop\/python实训\/代码\/Python\/Beautiful_爬取数据\/目录.txt","a",1,encoding="utf-8");
        div_name.ljust(80,' ');
        mp3_file.write("曲名:%-70s  下载量:%-10s  时长:%-20s  下载地址:%s\n"%(div_name,div_downcount,div_time,div_url));
        if not os.path.exists("path"):
            os.makedirs("path");
            pass;
        urllib.request.urlretrieve(div_url,"%s%s.mp3"%(file_path,div_name))
        print("第%d首下载成功！\n================"%i);
        i+=1;
        pass
    pass;
Get_MP3(data);
html.close();

