
# 【1】导包
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook;
import os;


# 【4】进行每个种类的数据爬取 - 带返回值
def Get_book_item_context(book_class_item,douban_book_url,header):
    print("===========%s:数据查询中。。。。========"%book_class_item);
    # 1.创建一个数组-用于存放单个种类的数据
    book_item_data = [];
    # 2.拼接网络地址: - 先爬取一页数据
    # https://www.douban.com/tag/小说/book?start=0
    # ==================================================
    douban_book_url = douban_book_url+book_class_item+"/book?start=0";
    print("%s网址:%s:"%(book_class_item,douban_book_url));
    # 3.开始访问网络
    requests_01 = requests.get(douban_book_url,data=header);
    # 4.判断网络状态
    if requests_01.status_code == 200:
        print("当前网页的编码格式：",requests_01.encoding);
        # 5.可以做修改 - 两种方式
        # requests_01.encoding = "utf-8";
        # 也可以返回访问网络的数据
        # 6.获取网址数据：
        data = requests_01.content.decode("utf-8");
        # print(data)
        # 7.存储到本地
        file_path = "C:\/Users\/Administrator\/Desktop\/WHGC2_2019年2月26日\/09_豆瓣图书_Excel\/豆瓣图书\/%s\/"%book_class_item
        if not os.path.exists(file_path):
            os.makedirs(file_path);
            pass
        file = open(file_path+"%s.html"%book_class_item,"w",1,encoding="utf-8");
        file.write(data);
        file.close();
        # 8.解析数据
        soup = BeautifulSoup(data,"html.parser");
        pass
    else:
        print("网络异常。")
        pass
    # ==================================================





    pass

# 【3】爬数据之前的分工顺序处理
def Do_Spider(book_class_list,douban_book_url,header):
    # 1.创建一个数组用于存放返回的数据：
    book_data_lists=[];
    # 2.进行网络访问 - 通过for循环遍历要访问的数据
    for book_class_item in book_class_list:
        print("开始查询数据种类：",book_class_item);
        # 3.数据爬取 - 将接受到的数据存储到book_data_list数组中
        book_class_data = Get_book_item_context(book_class_item,douban_book_url,header);
        pass

    pass


# 【2】Python程序入口
if __name__ == "__main__":
    print("==========豆瓣图书汇总录入==========");
    # 1.创建一个数组，存储在汇总的数据类型
    book_class_list=["小说","历史","爬虫","财经"];
    # 2.豆瓣网站地址：https://www.douban.com/tag/小说/book?start=0
    douban_book_url = "https://www.douban.com/tag/"
    # 3.用于代理
    """
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.362
    """
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.362"}
    # 4.对书籍数据进行分类访问处理
    Do_Spider(book_class_list=book_class_list,douban_book_url=douban_book_url,header=header);
    pass













