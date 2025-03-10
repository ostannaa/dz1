from dataclasses import replace
from operator import truediv

string = "hello"
print(type(string))

num1 = 20
print(type(num1))

num2 = 3.14
print(type(num2))

bool_var = True
print(type(bool_var))

lst = ['1' '2' '3']
print (type(lst))

dict = {'name': 'jon' , 'age': '12'}
print(type(dict))

tuple = (1,2,3)
print(type(tuple))

None
print(type(None))

num1 = 1
num2 = 10
print( num1 + num2)

num1 = 1
num2 = 10
print( num1 - num2)

num1 = 1
num2 = 10
print( num1 * num2)

num1 = 1
num2 = 10
print( num1 / num2)

num1 = 1
num2 = 10
print( num1 == num2)

num1 = 1
num2 = 10
print( num1 != num2)

num1 = 1
num2 = 10
print( num1 > num2)

num1 = 1
num2 = 10
print( num1 < num2)

num1 = 1
num2 = 10
num3 = 25
print( num1 == num2 and num3 < num2)

num1 = 1
num2 = 10
num3 = 25
print( num1 != num2 or num3 > num2)

num1 = 1
num2 = 10
num3 = 25
print(not (num1 > num2))

num1 = 12
print (int (num1))

num1 = 12
print (float (num1))

num1 = 12.5
print(int(num1))

num1 = 12.5
print(float(num1))

lst = 1
print (str(lst))

lst = 'hello world'
print (len(lst))

lst = 'hello world'
print(len(lst))

lst = ('hello' 'world')
print(len(lst))
print((lst))

lst = ['hello', 'world']
lst.append('5')
print (lst)

dct = {'hello': 5,
       'world': 6,
       'hi': 10}
key = list(dct.keys())
print("keys:", key)

dct = { 'hi': 10 ,
        'my': 22 ,
        '15': 32}
ke = list(dct.values())
print("keys:", ke)

dct = {'ms': 15 ,
       'ml': 16 ,
       'md': 18}
k = list (dct.items())
print('keys:', k)

num_str = 125
str(num_str)
print(num_str)

lst = 'Hi, my name is Python!'
lst = lst.replace('y','0')
lst = lst.replace('i', '1')
print(lst)


split_test = 'This is split text'
split_test = split_test.split()
print(split_test)

ist = 'string_join'
ln = len(ist)
print(ln)

list_append = [1,2,3]
list_append.append(4)
print(list_append)

list_extend= [4,5,6]
list_extend.extend([7,8,9])
print(list_extend)

list_extend= [4,5,6]
index_of_6 = list_extend.index(6)
print(index_of_6)

list_append = [1,2,3]
length = len(list_append)
print('довжина списку:', length)


dict_test = {'car': 'Toyota',
             'price': 4900,
             'where': 'EU'}
print (dict_test.get('car', 'not found'))

dict_test = {'car': 'Toyota',
             'price': 4900,
             'where': 'EU'}

keys = dict_test.keys()
print(keys)

dict_test = {'car': 'Toyota',
             'price': 4900,
             'where': 'EU'}

keys = dict_test.values()
print(keys)

dict_test = {'car': 'Toyota',
             'price': 4900,
             'where': 'EU'}

keys = dict_test.items()
print(keys)








