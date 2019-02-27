str = input("请输入：")
for n in range(0,len(str)):
    if(str.find("ab")!=-1):
        str = str.replace("ab","AB",1)
        pass
    pass
print(str)