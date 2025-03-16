list = [1 , 2 , 2, 3]
list.append(10)
list.append(20)
list.remove (20)
print(list)

list_1 = [1 , 2 , 3]
summa = sum(list_1)
print (summa)

list_2 = [1 , 2 , 3]
result = [num * 2 for num in list_2]
print(result)

list_4 = ('apple' , 'banana' , 'orange')
elements1 = list_4[0]
elements2 = list_4[1]
elements3 = list_4[2]
print(elements1)
print(elements2)
print(elements3)

list_5 = ['31' , '22' , 'ap']
list_6 = ['jj' , 'j' , 'pp']
listadd = list_5 + list_6
print(listadd)

slovnik = {'name': 'sakalova' , 'age': '26', 'sport': 'dance'  }
valu= slovnik.values()
print(valu)

books = {'book1': '2000', 'book2': '2002'}
books.update({'book3': '2000'})
print(books)

country = {'Ukraine' : 'Kiev', 'Italy' : 'Rome'}
city = country.pop('Ukraine', 'Kiev')
print(city)


