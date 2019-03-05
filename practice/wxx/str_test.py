#coding=utf-8

import re
def chinesNum(num):
    dictorition = ['零','一','二']
    return dictorition[num]
    pass;

# def num_to_chinese(num):
#     while True:

#         pass
#     return "test"
#     pass

# test_str = "sadsd123safaf456"
# num = re.search(r'([0-9]+)', test_str,0)
# while num:
#     number = num.group()
#     test_str = test_str.replace(number,num_to_chinese(number))
#     num = re.search(r'([0-9]+)', test_str,0)
#     print (test_str)
# re.sub(num, num_to_chinese(num))

print (chinesNum(0))
print (chinesNum(1))
print (chinesNum(2))