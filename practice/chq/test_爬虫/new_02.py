import urllib.request;
import re
url = "https://www.i4.cn/ring_22_0_1.html"
html =urllib.request.urlopen(url);
if html.getcode() == 200:
    print("网站返回码: %d,网络访问成功"%html.getcode());
    data = html.read()
    file =open("图片源码.html","wb",1)
    file.write(data);
    file.close();
    pass
html.close();

#解析源码的图片
def Get_data_img(data):
     # 【3】创建一个正则表达式进行数据筛选
    # 匹配小图 -- 网络不好
    #https://d-paper.i4.cn/middle/2019/03/01/11/1551410394777_063148.jpg
    r = r'[a-zA-z]+://[^\s]*.jpg';
    # r = r'https://d-paper.i4.cn/middle[^\s]*.jpg';
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
        urllib.request.urlretrieve(urlimg,"F:\practicework\practice\chq/图片_%d.jpg"%i);
        print("下载成功。。\n========================");
        i+=1;
        pass




    pass
# 【2】调用函数
Get_data_img(data)

        


