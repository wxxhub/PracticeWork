import requests;
from bs4 import BeautifulSoup;
from openpyxl import Workbook;
import os;


def insert_book(booklist,book_info_list):
    wb = Workbook();
    i = 0;
    for book_item in booklist:
        ws = wb.create_sheet(book_item,i);
        i+=1;
        pass;
    j = 0;
    for item_class_data in book_info_list:
        ws_01 = wb[booklist[j]];
        ws_01.append = (["书名","作者及翻译","时间","出版社","价格","评分","书籍连接","书籍图片"]);
        for item_data in item_class_data:
            ws_01.append(item_data);
            pass;
        j+=1;
        pass
    wb.save("图书.xlsx");
    pass;


def Get_bookdata(douban_url,book,header):
    a = [];
    j = 0;
    book_url = douban_url+book+"/book?start=0";
    print("%s网址：%s"%(book,book_url));
    request_01 = requests.get(book_url,header);
    data = request_01.text;


    if request_01.status_code == 200:
        print("连接成功!")
        soup = BeautifulSoup(data,"html.parser");
        div_list = soup.find("div",attrs={"class":"mod book-list"});
        div_dls = div_list.find_all("dl")
        # print(div_list)
        i = 1;


        for div_dl in div_dls:
            # div_dd = div_dl.find("dd")
            book_name = div_dl.find("a", attrs={"class": "title"}).string;
            info = div_dl.find("div",attrs = {"class":"desc"}).string.replace(" ","");
            print("第%d本书，书名：%s"%(i,book_name));

            book_img = div_dl.dt.a.img["src"]
            print("封面地址：",book_img);



            book_info = str(info).strip().split("/");
            book_jg = str(book_info[-1]).strip();
            book_time = str(book_info[-2]).strip();
            book_author = "";
            book_len = len(book_info);
            book_add = str(book_info[-3]).strip();
            for i in range(0,book_len-3):
                book_author+=book_info[i]+"/";
                pass;
            len_01 = len(book_author);
            book_author = book_author[0:len_01-1]

            for info in book_info:
                print("基本信息:%s" %info);
                pass;



            divs = div_dl.dd.find_all("div")
            book_rate = "0"
            if len(divs) == 2:
                book_rate = div_dl.dd.find("span", attrs={"class":"rating_nums"}).string;
                pass;
            print("书籍评分:%s"%book_rate);
            print("==========================")


            a.append(["《" + str(book_name).strip() + "》"
                                  , str(book_author).strip()
                                  , str(book_time).strip()
                                  , str(book_add).strip()
                                  , str(book_jg).strip()
                                  , str(book_rate).strip()
                                  , str(book_url).strip()
                                  , str(book_img).strip()]);
            print(["《" + book_name + "》", book_author, book_time, book_add, book_jg, book_rate, book_url, book_img])
            i += 1;
            pass;
        file_path = "C:\/Users\/dell\/Desktop\/python实训\/代码\/Python\/自动化办公_02\/%s\/"%book;
        if not os.path.exists(file_path):
            os.makedirs(file_path);
            pass;
        file_book = open(file_path+"%s.html"%book,"w",1,encoding="utf-8");
        file_book.write(data);
        file_book.close;
        pass;
    else:
        print("连接失败%d",request_01.status_code);
        pass;

    j+=1;
    return a;
    pass;
# 书籍分类
def Apart(booklist,douban_url,header):
    book_info_list = [];
    for book in booklist:
        print("开始查询图书种类:",book);
        book_data = Get_bookdata(douban_url,book,header);
        book_info_list.append(book_data);
        print("*****************************")
        print(book_info_list);
        print("*****************************")
        insert_book(booklist,book_info_list);
        pass;

    pass;


# 程序入口
if __name__ == "__main__":

    print("=========豆瓣图书汇总=======")
    booklist = ["小说","历史","爬虫","财经"];
    douban_url = "https://www.douban.com/tag/"
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"};
    Apart(booklist,douban_url,header);

    pass;