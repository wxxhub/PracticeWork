
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
        div_book_list = soup.find("div",attrs={"class":"mod book-list"});
        # print(div_book_list)
        tag_dls = div_book_list.find_all("dl");
        # print(tag_dls)
        print("书籍数目为：",len(tag_dls));
        # 9.遍历数组
        i = 1;
        for tag_dl in tag_dls:
            # print("书籍%d为：%s"%(i,tag_dl));
            print("===================================")
            # 9-1.获取书籍图片
            book_imgurl = tag_dl.dt.a.img["src"];
            print("%s书籍图片：%s"%(i,book_imgurl));
            # 9-2.获取书名：
            book_name = tag_dl.dd.a.string;
            # 获取书籍链接
            book_url = tag_dl.dd.a["href"];
            print("%s书籍名称：%s"%(i,book_name));
            # 9-3.出版社信息
            book_desc = tag_dl.dd.find("div",attrs={"class":"desc"}).string;
            print("%s书籍出版信息：：%s" % (i, str(book_desc).strip().split("/")));
            # ===============================================================
            # 余华 / 作家出版社 / 2012-8-1 / 20.00元
            # ['余华 ', ' 作家出版社 ', ' 2012-8-1 ', ' 20.00元']

            book_array = str(book_desc).strip().split("/");
            # 针对于数据不完整：不进行录入：
            if len(book_array)<4:
                book_array = ['', '', '', ''];
                pass
            # 价格
            book_jg =str(book_array[-1]).strip();
            # 出版时间
            book_time = str(book_array[-2]).strip();
            # 出版社
            book_add = str(book_array[-3]).strip();
            # 作者或翻译
            book_author = "";
            # ['[哥伦比亚] 加西亚·马尔克斯 ', ' 杨玲 ', ' 南海出版公司 ', ' 2012-9-1 ', ' 39.50元']
            book_len = len(book_array);  # 5-3 = 2
            for i in range(0,book_len-3):
                book_author+=book_array[i]+"/"
                pass
            # "abc/"
            len_01 = len(book_author);
            print(type(len_01))
            book_author = book_author[0:len_01-1];
            print(book_jg,book_time,book_add,book_author);

            # ===============================================================
            # 9-4.评分
            book_rating_nums = tag_dl.dd.find("span",attrs={"class":"rating_nums"}).string;
            print("%s书籍评分：%s" % (i,book_rating_nums));
            # ["书籍名称","作者及翻译"，"时间","出版社","价格","评分","书籍链接"，"书籍图片"]
            book_item_data.append(["《"+book_name+"》", book_author, book_time, book_add, book_jg,book_rating_nums,book_url,book_imgurl]);

            i+=1;
            pass

        pass
    else:
        print("网络异常。")
        pass
    # ==================================================
    return book_item_data;
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
        book_data_lists.append(book_class_data);
        print("*****************************")
        print(book_data_lists);
        print("*****************************")
        pass

    pass


# 【2】Python程序入口
if __name__ == "__main__":
    print("==========豆瓣图书汇总录入==========");
    # 1.创建一个数组，存储在汇总的数据类型
    book_class_list=["小说"];
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













