str = input("请输入：")
if(str.find("ab")!=-1):
    a = str.find("ab")
    str1 = str[0:a]+str[a:a+2].upper()
    while str.find("ab",a+2)!=-1:
        x = a+2
        a = str.find("ab",a+2)
        str1 += str[x:a]+str[a:a+2].upper()
        pass
    str1 += str[a+2:]
    pass
else:
    print("找不到匹配的文本！！")
    pass
print(str1)
print(============================)