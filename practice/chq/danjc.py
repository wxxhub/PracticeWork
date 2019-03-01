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
  #  def __init__(self,name,age):
   #     self.name = name;
    #    self.age = age;
     #   pass
    #def sit(self):
     #   print(self.name.title() + "蹲下起来")
      #  pass
    #pass
#your_dog = animal("likey",5)
#print("your dog name is " + your_dog.name.title() +".")
#print("your dog is " +str(your_dog.age) +" years old.")
#your_dog.sit()
#your_dog.roll_over()



#Car 类
class Car():                                
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def message(self):         #汽车整体信息
        long_name = str(self.year) +" " +self.make +" " +self.model
        return long_name.title()
        pass
    def read_odometer(self):   #里程信息          
        print("This car is " + str(self.odometer_reading) +" miles on it")
        pass
    def update_odometer(self,mileage):
        self.odometer_reading =mileage
        pass
    def increment_odometer(self,miles):
        self.odometer_reading +=miles     #将里程表增加到指定的量

my_new_car = Car("audi","a4","2016")
print(my_new_car.message())
my_new_car.odometer_reading = 23  #修改里程方法一
my_new_car.read_odometer()
my_new_car.update_odometer(23)   #修改里程方法二
my_new_car.read_odometer()
my_used_car = Car("subaru","ooutback","2014")
print(my_used_car.message())
my_used_car.update_odometer(246)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#继承
class ElectricCar(Car)