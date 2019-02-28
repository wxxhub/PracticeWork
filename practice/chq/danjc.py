#单继承
 #class animal(object):
  #  def __init__(self,name,age):
   #     self.name = name;
  #      self.age = age;
   #     pass
    #函数
    #def sit(self):
    #    print(self.name.title() + "蹲下")
    #    pass
   # def roll_over(self):
    #    print(self.name.title() + "打滚")
     #   pass
#实例1
#class my_dog(animal):
 #   def __init__(self,name,age):
  #      self.name = name;
   #     self.age = age;
    #    pass
    #def sit(self):
     #   print(self.name.title() + "蹲下起来")
      #  pass
    #pass
#my_dog = animal("nike",3)
#print("my dog name is " + my_dog.name.title() +".")
#print("my dog is " +str(my_dog.age) +" years old.")
#my_dog.sit()
#my_dog.roll_over()
#实例2
#class your_dog(animal):
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
        pass
    def sit(self):
        print(self.name.title() + "蹲下起来")
        pass
    pass
#your_dog = animal("likey",5)
#print("your dog name is " + your_dog.name.title() +".")
#print("your dog is " +str(your_dog.age) +" years old.")
#your_dog.sit()
#your_dog.roll_over()
