
# 【1】===文本文件的读取====
# 第一个参数：打开文件的绝对路径或者相对路径
# 第二个参数：读写权限: r表示读取 w表示写入 a表示追加 ；
# 第三个参数：缓存：默认情况下：1 缓存  ，0 不缓存
# 第四个参数：编码格式
# 打开一个文件
file = open("C:\/Users\/Administrator\/Desktop\/123.txt","r",1);
# 读取文件
print(file.read())
# 关闭文件
file.close()
# 读取项目中的文本
print("==========读取项目中的文本==============")
file1 = open("2019年2月27日.txt","r",1,encoding="utf-8");
# # 读取文件

print(file1.read())
# # 关闭文件
file1.close()
# 【2】===写入文本===

# open打开一个文件，在写入权限中如果找不到该文件会重新创建；
file_01 = open("C:\/Users\/Administrator\/Desktop\/2019年2月27日.txt","a",1,encoding="utf-8");
file_01.write("\n2019年2月27日 15:30:36 武汉工程大学Python实训\n")
file_01.close()

# open打开一个文件，在写入权限中如果找不到该文件会重新创建；
file_01 = open("2019年2月27日.txt","a",1,encoding="utf-8");
file_01.write("\n2019年2月27日 15:30:36 武汉工程大学Python实训\n")
file_01.close()

