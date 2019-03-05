s1 = input("请输入一段字符串：")
if s1.find("ab") != -1:
    m = s1.find("ab")
    s1 = s1[:m] + s1[m:m+2].upper() + s1[m+2:]
    while s1.find("ab",m+1) != -1:
        m = s1.find("ab")
        s1 = s1[:m] + s1[m:m + 2].upper() + s1[m + 2:]
        pass
    print(s1)
    pass
else:
    print("找不到匹配的文本")
    pass
# print(s1.replace("ab", "AB"))