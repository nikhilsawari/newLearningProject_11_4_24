print("Hello world")
print(2*222)

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
