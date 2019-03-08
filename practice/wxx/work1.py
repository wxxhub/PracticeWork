import urllib.request;
from bs4 import BeautifulSoup
import re

txt = open("test.txt", "w", 1, encoding="utf-8")

url = "https://www.i4.cn/jobs.html#java"

html = urllib.request.urlopen(url)

if html.getcode() != 200:
    print ("conect faile %d"%html.getcode())
    pass

data = html.read()

soup = BeautifulSoup(data, "html.parser")

serctions = soup.find_all("section")
txt.write("岗位数： %d\n"%len(serctions))
print("岗位数： %d\n"%len(serctions))
for section in serctions:
    # print (section)
    title = section.find("div", attrs={"class":"title"}).string
    print (title)
    txt.write(title)
    section_data = section.find("dl")

    txt.write("\n============ 岗位职责: 任职要求： ============\n")
    print("\n============ 岗位职责: 任职要求： ============\n")
    for i in section_data:
        msg = i.string
        if "岗位职责" in msg or "任职要求" in msg:
            continue
        if not re.findall("[1-9]", msg):
            continue
        txt.write(msg+"\n")
        print(msg)
        pass