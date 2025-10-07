

def printfizzbuzz(n):
    list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(i)
    return list

# print(printfizzbuzz(100))

def uppercase_string(my_str):
    myVowels=['a','e','i','o','u']
    for i in range(len(my_str)):
        if my_str[i] in myVowels:
            my_str = my_str[:i] + my_str[i].upper() + my_str[i+1:]
    return my_str

# print(uppercase_string("helloworld my name is khan"))

def second_max(list_num):
   mylist = list_num.copy()
   for num in mylist:
       if num == max(mylist):
           mylist.remove(num)
   return max(mylist)

# print(second_max([1,2,3,4,5,6,7,8,9,10]))

mydict1={'a': 100, 'b': 200, 'c':300}
mydict2={"gaurav": 300, "ashish": 200, "sachin":400, "rahul":600}

# mydict1=mydict1+mydict2
# mydict1.update(mydict2)
# mydict1={**mydict1, **mydict2}

mydict1 = mydict1 | mydict2  

# print(mydict1)    




class Car:
    def __init__(self,model,year,color,name):
        self.model = model
        self.year = year
        self.color = color
        self.name = name

    def car_info(self):
        return f"{self.name} is a {self.color} {self.model} manufactured in {self.year}"
    def start(self):
        print(f"{self.name} car is starting")
        return f"{self.name} car is starting"
    
    def stop(self):
        print(f"{self.name} car is stopping")
        return f"{self.name} car is stopping"
    
    
mycar_BMW = Car("BMW",2020,"Black","X5")
# mycar_BMW.start()
mycar_Audi = Car("Audi",2021,"White","Q7")
# mycar_Audi.start()

def car_details(car:Car):
   print(car.start())  
   print(car.car_info())
   print(car.stop())

# car_details(mycar_BMW)


class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def person_info(self):
        return f"{self.name} is a {self.age} year old {self.gender}"
    
class Employee(Person):
    def __init__(self,name,age,gender,employee_id,department):
        super().__init__(name,age,gender)
        self.employee_id = employee_id
        self.department = department

    def employee_info(self):
        return f"{self.name} works in {self.department} department and has employee ID {self.employee_id}"
    
def employee_details(emp:Employee):
    print(emp.person_info())    
    print(emp.employee_info())

emp1 = Employee("Singh",30,"Male",101,"HR")
emp2 = Employee("Gaurav",54,"Male",102,"Development")
# employee_details(emp1)
# employee_details(emp2)


class Shape:
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        print("Area of Rectangle:" ,self.length * self.width)
        return self.length * self.width
    
class Circle(Shape):
    
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        print("Area of Circle:" ,3.14 * self.radius * self.radius)
        return 3.14 * self.radius * self.radius
    # 
print("Calculating area of shapes:")

# Rect = Rectangle(10,5)
# print(Rect.area())
# shapes = [Rectangle(10,5), Circle(7)]
# for shape in shapes:
#     shape.area()
    
    
    
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


# dog2 = Dog()
# cat2 = Cat()
# print(dog2.speak())
# print(cat2.speak())

class Movie:
    def show(self):
        print("you are watching movie")

class ActionMovie(Movie):
    def show(self):
        print("you are watching action movie")
        
class ComedyMovie(Movie):
    def show(self):
        print("you are watching comedy movie")
        
class DramaMovie(Movie):
    def show(self):
        print("you are watching drama movie")


movie1 = ActionMovie()
movie2 = ComedyMovie()
movie3 = DramaMovie()
# movie1.show()
# movie2.show()
# movie3.show()


class Area:
    def __init__(self, length=10, width=10):
        self.__length = length
        self.__width = width

    @property
    def dimensions(self):
        # Getter must return something
        return f"Length: {self.__length}, Width: {self.__width}, Area: {self.__length * self.__width}"

    @dimensions.setter
    def dimensions(self, value):
        # Expect a tuple (length, width)
        length, width = value
        if length > 0 and width > 0:
            self.__length = length
            self.__width = width
        else:
            print("Length and Width must be positive values")

# Example usage
area1 = Area(12, 10)          # initialize with custom values
area1.dimensions = (20, 30)   # setter
print(area1.dimensions)       # getter


# class deque:
#     def __init__(self):
#         self.items = []

#     def clear(self):
#         self.items = []
#     def is_empty(self):
#         return len(self.items) == 0

#     def add_front(self, item):
#         self.items.insert(0, item)

#     def add_rear(self, item):
#         self.items.append(item)

#     def remove_front(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         return "Deque is empty"

#     def remove_rear(self):
#         if not self.is_empty():
#             return self.items.pop()
#         return "Deque is empty"

#     def size(self):
#         return len(self.items)
    
#     def display(self):
#         print(self.items)
#         return self.items

# dq = deque()
# dq.add_rear(1)
# dq.add_rear(2)
# dq.add_front(0)
# dq.display()        
# print(dq.items)
# dq.add_front(12)
# print(dq.items)
# dq.remove_rear()
# dq.display()
# dq.remove_front()
# dq.display()
# dq.clear()
# dq.display()
# print("Deque is empty")


from collections import deque
from turtle import back 
dq = deque()
dq.append(1) 
dq.append(2) 
dq.append(4)
# 10 1 2 3 3
dq.appendleft(10) 
dq.append(15)
# dq.pop()
# dq.popleft()
# dq.append(3)
front = dq[0] if dq else None
dq.clear()
is_empty = len(dq) == 0
print("Deque contents:", list(dq))
print("Front element:", front)
back = dq[-1] if dq else None
print("Back element:", back)


import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the time difference
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        print(f"Result: {result}")
        return result
    return wrapper


@timer
def write_file(filename):
   content = ["gaurav"]
   with open(filename, "a") as textfile:
       for word in content:
           textfile.write(word + "\n")
   return filename


write_file("samples.txt")
# opened_file = open("samples.txt", "r")
# print(opened_file.read())