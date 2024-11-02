immutable_var=([1,2],"apple",9.8,3,4,["nut","rom"])
print(immutable_var)
print(type(immutable_var))
print(immutable_var[5])  # кортеж также как и списки имеет индексацию,но при замене значения индекса в кортеже
# на другой элемент при запуске программа выдаст ошибку.Кортеж неизвеняемый элемент
print(immutable_var)
my_table=list(immutable_var) # преобразование кортежа в список
print(type(my_table))
print(my_table)
my_table[2]=('peach') # замена 2 элемента списка (9.8) на peach
print(my_table)
my_table[0][1]=345 # замена 1 инндекса на новый элемент
print(my_table)
my_table.remove('apple') # удаление из списка элемента
print(my_table)
my_table.remove(["nut","rom"]) # удаление из списка элемента
print(my_table)
my_table.append(["sun,joke,1,2"])# добавление в конец списка элемента
print(my_table)
print("coffee" in my_table)

print(type(immutable_var))
print(type(my_table))
print (len(immutable_var))
print(len(my_table))
print(immutable_var.__sizeof__()) # размер памяти кортежа
print(my_table.__sizeof__())# размер памяти листа