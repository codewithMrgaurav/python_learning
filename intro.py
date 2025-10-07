# print("hello")

# num = int(input("enter a number:"))
# if num % 2 ==0:
#     print("Even")
# else:
#     print("Odd")


# a = int(input("enter a number:"))
# b= int(input("enter a number:"))
# c=int(input("enter a number:"))

# if a > b and a > c:
#     print("a is greater")
# elif b > c:
#     print("b is greater")
# else:
#     print("c is greater")


from array import array


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

# print(fact(2))

fib_list = []
def fib_numbers(n):
    a , b = 0, 1
    for i  in range(3,n+1):
        fib_list.append(a)
        a, b = b, a + b
    return a ,b

# fib_numbers(10)
# print(fib_list)
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         result = fib(n-1) + fib(n-2)
#         return result

# print(fib(12))


# OOps concepts in python

class Book:
    def __init__(self, title, status, stock):
        self.title = title
        self.__status = status
        self.__stock = stock

    def display(self):
        print(f"Title: {self.title}, Status: {self.__status}, Stock: {self.__stock}")

    def get_stock(self):
        return self.__stock

    def update_stock(self, change):
        self.__stock += change


class Member:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.books_borrowed = 0

    def role_check(self):
        if self.role in ["student", "faculty"]:
            print(f"{self.name} is a valid member")
            return True
        print(f"{self.name} is not a valid member")
        return False

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Books Borrowed: {self.books_borrowed}")

    def borrow_book(self, book: Book):
        if not self.role_check():
            return

        if book.get_stock() <= 0:
            print(f"Sorry, {book.title} is out of stock")
            return

        if self.role == "student" and self.books_borrowed >= 2:
            print(f"{self.name} cannot borrow more than 2 books")
            return
        elif self.role == "faculty" and self.books_borrowed >= 5:
            print(f"{self.name} cannot borrow more than 5 books")
            return

        book.update_stock(-1)
        self.books_borrowed += 1
        print(f"{self.name} has borrowed {book.title}")


# Example Usage

# b1 = Book("Python", "available", 0)
# member1 = Member("Alice", "student")

# member1.borrow_book(b1)
# b1.display()
# member1.display()


def compund_int(principle,rate,time):
    
    net_interest_ratio= pow((1+rate/100),time)
    print("Net Interest Ratio:",net_interest_ratio)
    amount = principle*net_interest_ratio
    ci=amount - principle
    print("Compound Interest:",ci)  
    return ci

# compund_int(2500,20,3)


def armstrong_num(n):
    sum=0
    num= str(n)
    length = len(num)
    i=0
    for i in range(length):
        temp = pow(int(num[i]),length)
        sum+=temp
        i+=1
    if sum == n:
        print(n,"is an Armstrong number")
    else:
        print(n,"is not an Armstrong number")

# armstrong_num(153)


def prime_num(range:list):
    primes = list()
    i=range[0]
    for i in range[1]: 
        total_divisors = 0
        j=2
        for j in range(i):  
            if i % j == 0:
                total_divisors += 1
                break  

        if total_divisors == 0 and i > 1:
            primes.append(i)
            
    return primes

# Test the function with a given range
# prime_list = prime_num([1, 15])
# print(prime_list)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# print(is_prime(29))
# print(is_prime(21))

def fibonacci(n):
    list_fib = []
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        list_fib = [0]
        return list_fib
    elif n == 1:
        list_fib = [0, 1]
        return list_fib
    else:
        list_fib = [0, 1]
        for i in range(2, n):
            [a, b] = [b, a + b]
            list_fib.append(b)
    # print(list_fib)
        return list_fib

# print(fibonacci(10))
# print(sum(fibonacci(10)))

mylist =[5,8,11,9,7,3,1,2,5,13,12,78,9,19,14,6,23,77,44,22,33,34,54,66,98,101,100,103,104,405]

def binary_search(mylist:list,x:int):
   mylist.sort()
   print(mylist)
   low = 0
   high = len(mylist) - 1
   print(len(mylist))
   mid = 0
   while low <= high:
       mid = (low + high) // 2
       if mylist[mid] < x:
           low = mid + 1
       elif mylist[mid] == x:
           return 1
       else:
           high = mid - 1
           mid = (low + high) // 2
   return -1

# res = binary_search(mylist,103)

# if res != -1:
#     print("Element found at index:")
# else:
#     print("Element not found")
    
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None
    
    def push(self, data):
     new_node = Node(data)
     new_node.next = self.top
     self.top = new_node
     print(f"Pushed {data} to stack")
        
    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop")
            return None
        popped_node = self.top
        self.top = self.top.next
        print(f"Popped {popped_node.data} from stack")
        return popped_node.data
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        print(f"Top element is {self.top.data}")
        return self.top.data
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        current = self.top
        print("Stack elements:")
        while current:
            print(current.data ,end=" <- ")
            current = current.next
        print("None")
        
# Example usage
# st = Stack()
# st.push(10)
# st.push(20)
# st.push(30)
# st.display()
# st.peek()
# st.pop()
# st.display()    
# st.pop()
# st.push(40)
# st.display()

