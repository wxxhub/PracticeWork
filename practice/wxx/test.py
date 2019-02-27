#coding=utf-8

test_str = "afdsfadfsfdsfabaabaab"

# if 'ab' in test_str:
test_str2 = test_str.replace("ab", "AB")

print (test_str2)

while 'ab' in test_str:
    site = test_str.find('ab')
    test_str = test_str.replace("ab", "AB", 1)
    print ("ab site: %d have change to AB"%(site))

print (test_str)
