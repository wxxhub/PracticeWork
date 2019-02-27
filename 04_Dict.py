
# 【1】===字典的使用和创建===
# 字典的存储：Key value的形式存储
dict_01 = {"001":"武汉热干面","002":"长沙臭豆腐","003":"辣条"}
dict_02 = dict(name="狄仁杰",age="18");
print(dict_01);
print(dict_02);
# 使用:
print(dict_01["001"])
print(dict_02["name"]);
# 【2】===数组转换成字典的格式=====
# 数组中的每一个元素：("name","张云雷")
items = [("name","张云雷"),("age","18")];
items.append(("phone","1800000"))
print(items[0])
dict_03 = dict(items);
print(dict_03)
# 【3】===in成员资格===
# 只能查询key值
print("name" in dict_03);
# 【4】===删除===
# 根据Key值可以删除对应的一项数据
del dict_03["age"]
print(dict_03)
# 【5】===清空 ===
# clear没有返回值：dict还是一个字典；只是没有数据；

r = dict_03.clear();
print(r,dict_03)