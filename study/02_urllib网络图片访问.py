
# 1.导入urllib库
import urllib.request;
# 导入正则表达的包
import re
# 2.目标网址
url = "https://www.i4.cn/wper_1_0_0_1.html"
# 3.检验网址时候可以访问
html = urllib.request.urlopen(url);
if html.getcode() == 200:
    print("网站返回码：%d,网络访问成功"%html.getcode())
    # 4.读取网站源码
    data = html.read();
    # 5.存储到本地
    file = open("02_爱思助手图片网站.html","wb",1);
    # 6.写入数据
    file.write(data);
    # 7.关闭文件写入
    file.close();
    pass
# 8.关闭网络
html.close();
# =====================开始解析源码中的图片============================
# 【1】创建一个函数：
def Get_data_img(data):
    # 【3】创建一个正则表达式进行数据筛选
    # 匹配小图 -- 网络不好
    # https://d-paper.i4.cn/middle/2019/03/01/11/1551410394777_063148.jpg
    # r = r'[a-zA-z]+://[^\s]*.jpg';
    r = r'https://d-paper.i4.cn/middle[^\s]*.jpg';
    # 【4】创建一个正则表达式的模板
    pat = re.compile(r);
    # 【进行数据匹配】
    # 第一个参数：正则表示式模板，第二参数：字符串类似的数据
    imgurls = re.findall(pat,str(data));
    # 返回数据为：数组格式
    print(imgurls);
    print("图片个数：%d"%len(imgurls));
    # 图片遍历下载：
    i = 1;
    for urlimg in imgurls:
        print("第%d图片地址：%s"%(i,urlimg));
        print("开始下载第%d张图片。。。"%i)
        urllib.request.urlretrieve(urlimg,"爱思助手手机图片/图片_%d.jpg"%i);
        print("下载成功。。\n========================");
        i+=1;
        pass




    pass
# 【2】调用函数
Get_data_img(data)