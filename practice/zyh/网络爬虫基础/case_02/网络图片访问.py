import urllib.request;
import re;
import os;
url = "https://www.i4.cn/wper_1_0_0_1.html";
html = urllib.request.urlopen(url)
if html.getcode() == 200:
    print("连接成功")
    data = html.read();
    file = open("图片网站.html","wb",1);
    file.write(data);
    file.close();
    pass;
def get_img(data):
    i = 1;
    path = "图片1"
    r= r'[a-zA-z]+://[^\s]*.jpg';
    pat = re.compile(r);
    imgurls = re.findall(pat,str(data));
    print(imgurls);
    print(len(imgurls));
    for imgurl in imgurls:
        if not os.path.exists(path):
            os.makedirs(path);
            print("文件夹创建成功");
            pass
        else:
            print("文件已存在");
            pass
        print("下载第%d张图片..." % i);
        urllib.request.urlretrieve(imgurl,path+"/%d.jpg"%i);
        print("第%d张下载成功\n===================="%i);
        i+=1;
        pass;
    pass;
get_img(data);