a=[[2,3,3,2],[2,5,5,3]]
print(a[0])
d=(sum(a[0])/len(a[0]))
f=(sum(a[1])/len(a[1]))
s=(d,f)
g={"мама","папа"}
spisok=zip(g,s)
print(dict(spisok))

#Дано:
grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={"Johnny","Bilbo","Steve","Khendrik","Aaron"}
#решение
print(grades)
print(students)
print(type(grades))
print(type(students))
print(len(grades))
grades_0=(sum(grades[0])/len(grades[0])) # вычисление среднего арифметического значения в списке по обращенному индексу
grades_1=(sum(grades[1])/len(grades[1]))
grades_2=(sum(grades[2])/len(grades[2]))
grades_3=(sum(grades[3])/len(grades[3]))
grades_4=(sum(grades[4])/len(grades[4]))
my_list=(grades_0,grades_1,grades_2,grades_3,grades_4) #присвоение нескольких переменных к одному списку
print(my_list)
spisok=zip(students,my_list) # обьединение списка с множеством через функцию zip(создает итератор ,который
# обьединяет элементы между собой
print(dict(spisok)) # метод dict который перестроил новый список в словарь так как у нас имеется ключ и его значение