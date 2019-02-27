#练习题测试
sums = input("请输入字符串:")
print(sums)
print(sums.count("ab"))
if(sums.count("ab")>0):
    print("有匹配文本")
    sums2 =sums.replace("ab","AB")
    print(sums2)
    while "ab" in sums:
        site =sums.find('ab')
        sums=sums.replace("ab","AB",1)
        print("ab site:%d have change to AB"%(site))
        pass
else:
    print("无匹配文本")
pass