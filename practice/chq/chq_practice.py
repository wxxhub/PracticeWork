# 合并字符串
first_name = "chq"
last_name = "love cs"
full_name = first_name+""+last_name
print(full_name)

print("think,"+full_name.title()+"!")

#添加换行符
print("python")
print("\tpython")
print("read:\n\tI\n\tlove\n\tcs")

#删除空白 rstrip()
my_language ='python  '
my_language =my_language.rstrip()
my_language

#整数运算 + - * / **

#浮点运算

#str() 非字符串转化
age = 21
message = str(age) +"years old"
print(message)

#访问列表元素
#print(bicycles[0])

#对列表的操作
bicycles = ['chq','wxx','hhc','zyh']
message ="my first bicycle was a" +bicycles[0].title() +"."
print(message)
bicycles[2]='dds'
print(bicycles)
bicycles.append('sfw')
print(bicycles)
bicycles.insert(2,'fhd')
print(bicycles)
del bicycles[3]
print(bicycles)

popped_bicycles =bicycles.pop()
print(bicycles)
print(popped_bicycles) #pop()删除列表末尾元素

# del删除后不再使用，pop删除元素后还可以继续使用
bicycles.remove('chq')
print(bicycles)













