# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

num = 12
print("num is "+str(num))
print(1+2)
name= "Nikhil"
surname = "Awari"
address = "New dehli"
age = 22

print(name)
print(name[3])
print(name+" "+surname)
print(name * 3)
print(name[1:3])
print(name[0])
print(name[-3])
print("New" in address)
print(name.upper())
print(name.lower())
print(type(name))
print("My name is - %s and address is - %s also mmy age is - %s" % (name, address, age))
print("My name is - {} and address is - {} also mmy age is - {}".format(name, address, age))
print(2**3)

print('List----------------------')
my_list = ['a','b']
print(my_list)
print(len(my_list))
my_list2 = ['one', 'two', 'three']
my_list2.append("four")
print(my_list2)
my_list3 = ['one', 'car', 3, '#']
print(my_list3)
my_list.append(my_list2)
print(my_list)
my_list.extend(['how','I','met'])
print(my_list)
my_list3.insert(1,'one')
print(my_list3)
l = list(range(10))
print(l)
l[2:9:2]
print(l[2:9:2])
print(l[::2])
print(l[:2:2])

print('Dictionary----------------------')
my_dict = {"key1":"value1","key2":"value2"}
print(my_dict)


print(my_dict['key2'])
my_dict['key2']=123
print(my_dict)
d = {}
# Create a new key through assignment
d['animal'] = 'Dog'
print(d)

new_list = [1,2,3,4,5,6,7,8]
for numbers in new_list:
    if numbers < 5:
        print(numbers,end=' ')

while numbers in new_list:
    if numbers < 5:
        print(new_list)

Method -
def fib(n):    # write Fibonacci series less than n
...     """Print a Fibonacci series less than n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...


Object creation in python -
1.
__init__ inbuilt function in all class for initialization
Self is like this. in java
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

2.
p1 = MyClass()
print(p1.x)
