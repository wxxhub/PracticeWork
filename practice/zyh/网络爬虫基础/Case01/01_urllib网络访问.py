import urllib.request;
url = "https://www.i4.cn/ring_22_0_1.html";
html = urllib.request.urlopen(url);
data = html.read();
file = open("i4.html","wb",1);
file.write(data);
file.close();
html.close();