import urllib.request
from bs4 import BeautifulSoup

url = "https://movie.douban.com/subject/26266893/comments?start=%d&limit=20&sort=new_score&status=P"

star_5 = 0
star_4 = 0
star_3 = 0
star_2 = 0
star_1 = 0
star_0 = 0
start = 20
commit_sum = 0

while True:
    html = None
    try:
        html = urllib.request.urlopen(url%start)
        pass
    except:
        print("open failed") 
        break

    if html.getcode() != 200:
        print("open '"+url+"' failed! errocode: " + str(html.getcode())) 
        break
        pass

    data = html.read()
    html.close()

    soup = BeautifulSoup(data, 'html.parser')
    commit_divs = soup.find_all("div", attrs={"class":"comment"})
    for commit_div in commit_divs:
        commit = commit_div.find("span", attrs={"class":"short"})
        print ("commit: "+commit.string)
        print ("")

        commit_info_span = commit_div.find("span", attrs={"class":"comment-info"})
        # print (commit_info_span)
        commit_info = commit_info_span.find_all("span")
        # print(commit_info[1]["class"])
        commit_star = commit_info[1]["class"][0]

        commit_sum = commit_sum+1
        if commit_star == "allstar10":
            star_1 = star_1 + 1
            continue
            pass

        if commit_star == "allstar20":
            star_2 = star_2 + 1
            continue
            pass
        
        if commit_star == "allstar30":
            star_3 = star_3 + 1
            continue
            pass

        if commit_star == "allstar40":
            star_4 = star_4 + 1
            continue
            pass
        
        if commit_star == "allstar50":
            star_5 = star_5 + 1
            continue
            pass
        
        star_0 = star_0 + 1

        # star_name =" allstar%d0 rating"
        # for i in range(1,6):
        #     star = commit.find("span", attrs={"class":star_name%i})
        #     pass
        pass

    start = start + 20

print ("finished. commit sum: "+str(commit_sum))
print ("5_start: "+str(star_5)+" 比例: "+str(star_5/commit_sum))
print ("4_start: "+str(star_4)+" 比例: "+str(star_4/commit_sum))
print ("3_start: "+str(star_3)+" 比例: "+str(star_3/commit_sum))
print ("2_start: "+str(star_2)+" 比例: "+str(star_2/commit_sum))
print ("1_start: "+str(star_1)+" 比例: "+str(star_1/commit_sum))
print ("0_start: "+str(star_0)+" 比例: "+str(star_0/commit_sum))