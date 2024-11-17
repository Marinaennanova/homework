# формируем класс с названием House
class House:
# В представленном коде наблюдается self, который является указателем на сам объект.
# Метод '__init__' (конструктор или инициализатор) куда добавляется характеристики атрибутов.
    def __init__(self,name,numbers_of_floor):
# характеристики атрибутов name,numbers_of_floor.
        self.name = name
        self.numbers_of_floor = numbers_of_floor
# формируем функцию для указанных атрибутов с из характеристиками
    def go_to(self):
# вводим номер этажа в заданном жилищном комплексе
            new_floor = int(input(f"Введите номер этажа {self.name}:"))
# перебираем проверяем наличие указанного номера этажа
            for i in range(1,new_floor+1):
# устанавливваем условие сравнения от первого элемента до последнего включительно и выводим в консоль
                 if 1 <= new_floor <= self.numbers_of_floor:
                    print(i)
# если условие False то в консоль выводится ответ и программа остатнавливается
                 else:
                     print("Такого этажа не существует.")
                     break
# обращение к атрибуту класса House
h1 = House ("ЖК Горький",18)
h2 = House ("Домик в деревне",2)
h3 = House ("Гусарская балада",3)
print(h1.name,h1.numbers_of_floor)
print(h2.name,h2.numbers_of_floor)
print(h3.name,h3.numbers_of_floor)
# запуск функции с заданными характеристикасми атрибутов и вывод их в консоль
h1.go_to()
h2.go_to()
h3.go_to()
#  в итоге на выходе если в заднанном жилищном комплексе 18 этажей,а мы задали 20 ,то консоль выдаст,что "такого
#  этажа нет",если же введется меньшее количество или равное кол-во этажей,то консоль выведет порядок от 1 до
# введеного числа.