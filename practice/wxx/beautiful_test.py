import urllib.request
from bs4 import BeautifulSoup

url = "https://www.i4.cn/ring_1_0_1.html"

html = urllib.request.urlopen(url)

if html.getcode() == 200:
    date = html.read()
    soup = BeautifulSoup(html)
    print (soup.title)
    pass
else:
    print ("open "+url+" failed! "+str(html.getcode()))
    pass