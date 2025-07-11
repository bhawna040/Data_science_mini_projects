#1.	Write a Python program to find the largest of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest number is", max(a, b, c))

#	2.	Create a program that checks whether a number is even or odd.
num = int(input("Enter a number: "))
print(" Number is Even" if num % 2 == 0 else "Odd")

# 3.	Accept a string from the user and reverse it.
text = input("Enter a string: ")
print("Reversed string:", text[::-1])


#	4.	Write a program to count the number of vowels in a string.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)


#	5.	Create a calculator using if-else (add, subtract, multiply, divide).
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    print("Result:", a / b)
else:
    print("Invalid operator")

#6.	Write a program to check if a number is prime.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")

#	7.	Display the multiplication table of a given number.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#	8.	Write a program to print the Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

#	9.	Write a program to find the factorial of a number using a loop.
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)

#10.	Accept a number and check whether it is a palindrome.
num = input("Enter a number: ")
print("Palindrome" if num == num[::-1] else "Not Palindrome")

#11.	Find the sum of digits of a number using a while loop.
num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)

#12.	Create a program to convert Celsius to Fahrenheit.
c = float(input("Enter Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)


#	13.	Write a Python function to find the maximum of two numbers.
def maximum(a, b):
    return a if a > b else b

print(maximum(10, 20))

#	14.	Accept a list of numbers and return the average.
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Average:", sum(nums) / len(nums))


#	15.	Find the second largest number in a list.
nums = list(map(int, input("Enter numbers: ").split()))
nums = list(set(nums))
nums.sort()
print("Second largest:", nums[-2])

#	16.	Accept a sentence and count the number of words.
sentence = input("Enter a sentence: ")
print("Number of words:", len(sentence.split()))

#	17.	Accept a list and remove all duplicates from it.
nums = list(map(int, input("Enter numbers: ").split()))
print("Without duplicates:", list(set(nums)))

#	18.	Write a program to create a dictionary from two lists.
keys = input("Enter keys: ").split()
values = input("Enter values: ").split()
d = dict(zip(keys, values))
print(d)

#	19.	Accept a list and sort it without using sort() function.
nums = list(map(int, input("Enter numbers: ").split()))
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print("Sorted list:", nums)

#	20.	Write a function that checks if a string is a pangram.
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))

print(is_pangram(input("Enter a sentence: ")))

#	21.	Write a function to check if the input is a number or not.
def is_number(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

print(is_number(input("Enter something: ")))

#	22.	Accept a string and check if it is an anagram of another.
a = input("First string: ")
b = input("Second string: ")
print("Anagram" if sorted(a) == sorted(b) else "Not anagram")

#	23.	Accept a number and print its binary, octal, and hexadecimal.
num = int(input("Enter a number: "))
print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))

#	24.	Accept a list and print all elements greater than 50.
nums = list(map(int, input("Enter numbers: ").split()))
print("Numbers > 50:", [n for n in nums if n > 50])

#	25.	Write a function to count uppercase and lowercase letters in a string.
text = input("Enter a string: ")
upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())
print("Uppercase:", upper)
print("Lowercase:", lower)

#	26.	Write a Python program using a lambda function to square all elements in a list.
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print("Squares:", squares)

#	27.	Create a function that returns a list of prime numbers from 1 to 100.
def primes():
    return [n for n in range(2, 101) if all(n % d != 0 for d in range(2, int(n**0.5) + 1))]

print(primes())

#	28.	Write a program to implement a simple calculator using functions.
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(add(a, b))
elif op == '-':
    print(sub(a, b))
elif op == '*':
    print(mul(a, b))
elif op == '/':
    print(div(a, b))
else:
    print("Invalid operator")

#	29.	Implement a recursive function to compute factorial.
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))


#	30.	Create a Python program using OOP for student management (class, object, init).
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

s1 = Student("Alice", 101)
s1.display()

#	31.	Write a program to read a file and count the number of lines and words.
with open("sample.txt", "r") as file:
    lines = file.readlines()
    word_count = sum(len(line.split()) for line in lines)

print("Lines:", len(lines))
print("Words:", word_count)

#	32.	Write a Python decorator to print the execution time of a function.
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Execution time:", time.time() - start)
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()

#	33.	Create a class BankAccount with deposit and withdraw methods.
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

acc = BankAccount("John")
acc.deposit(1000)
acc.withdraw(500)
print("Balance:", acc.balance)

#	34.	Implement a generator to yield even numbers from 1 to n.
def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i

for num in even_numbers(10):
    print(num)

#	35.	Write a function using *args and **kwargs to print any number of arguments.
def display(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

display(1, 2, 3, name="John", age=25)

#	36.	Use list comprehension to create a list of squares of even numbers from 1 to 20.
squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares)

#	37.	Create a function that takes a list and returns only unique elements.
def unique_list(lst):
    return list(set(lst))

print(unique_list([1, 2, 2, 3, 4, 4]))

#	38.	Write a Python program to merge two dictionaries.
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
merged = {**a, **b}
print(merged)

#	39.	Create a class that inherits from another class and overrides a method.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()

#	40.	Write a function to find common elements between two lists.
def common(a, b):
    return list(set(a) & set(b))

print(common([1, 2, 3], [2, 3, 4]))

#	41.	Implement a program to demonstrate try-except-finally for exception handling.
tex=int(input("Enter the number"))
try:
    
    print(tex/0)
except ArithmeticError:
    print("can't divide by zero")
finally:
    print("This is finally block")

#	42.	Write a program to parse and display JSON data from a string.
import json
data = '{"name": "John", "age": 30, "city": "New York}'
parsed_data = json.loads(data)
print(parsed_data)
print("Name",parsed_data['name'])
#	43.	Create a class that demonstrates the use of private and protected members.
class demo:
    def __init__(self):
        self.protected=" I am protected"
        self.private="I am private"
    def show(self):
        print(self.protected)
        print(self.__private)
d=demo()
d.show()
#	44.	Write a Python function to check if a string is a valid email address.
import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0]'
    return bool(re.match(pattern,email))
print(is_valid_email("bhawnasarvang04@gmail.com"))
#	45.	Accept a CSV file and convert it into a list of dictionaries.
import csv
with open("month.csv",newline='') as files:
    reader=csv.DictReader(file)
    data=list(reader)
print(data)
#	46.	Create a simple login system using dictionary and input.
users={"admin":"123","bhawna":"2345"}
username=input("ENter username")
password=input("Enter username")
if users.get(username)==password:
    print("Login successful")
else:
    print("Login failed")
#	47.	Write a function to flatten a nested list using recursion.
def flatten(lst):
    result=[]
    for item in lst:
        if isinstance(item,list):
            result+=flatten(item)
        else:
            result.append(item)
        return result
print(flatten([1, [2, [3, 4], 5], 6]))
#	48.	Demonstrate use of map(), filter(), and reduce() on a list.
from functools import reduce
nums=[1,2,3,4,5]
squared=list(map(lambda x:x**2,nums))
even=list(filter(lambda x:x%2==0,nums))
product=reduce(lambda x,y:x*y,nums)
print("squared",squared)
print("even",even)
print("product",product)

#	49.	Build a small CLI app that takes user input and performs basic operations.
while True:
    Choice=input("Enter command(add,quit)")
    if Choice=="add":
        a=int(input("Enter the number"))
        b=int(input("enter the number"))
        print("Sum is",a+b)
    elif Choice=="quit":
        break
#	50.	Create a mini Python quiz that takes answers from the user and displays score.
score=0
questions={"What is the capital of France?":"Paris","What is the capital of India?":"Delhi","2+2":"4"}
for question,answer in questions.items():
    ans=input(question).strip().lower()
    if ans==a:
        score+=1
print("your score",score ,"/",len(questions))