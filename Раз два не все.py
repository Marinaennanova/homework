
data_structure = [[1,2,3],{"a":4,"b":5},(6,{"cube":7,"drum" :8}),"Hellow",((),[{(2,"Urban",("Urban2",35))}])]

def culc_stucture(data_structure):
        summa = 0
        if isinstance(data_structure,(int,float)): # данный метод проверяет принадлежность обьекта
# к определенному классу или типу,принимает два аргумента
           return data_structure
        elif isinstance(data_structure,str): # проверка на наличие строк
           return len(data_structure)# если строки есть ,возвратить длину этой строки
        elif isinstance(data_structure,(list,tuple,set)): # проверка на наличие списка,кортежа и множества
           for i in data_structure:
             summa+=culc_stucture(i) # осуществляем перебор по елементам и их суммируем если есть числа
        elif isinstance(data_structure,dict): # проверка на наличие словаря
           for key,value in data_structure.items(): # возвращаем пару ключ+значение перебрав заданный список
             summa += culc_stucture(key) # переборка по ключу если это числа
             summa += culc_stucture(value)# переборка по значению ключа и их суммирование если это числа
        return summa
result = culc_stucture(data_structure)
print(result)
