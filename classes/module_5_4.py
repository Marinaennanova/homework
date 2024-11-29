class House:
    # создание атрибута
    houses_history = []

    # применение метода __new__
    def __new__(cls, *args):
    # добавление в атрибут "houses_history" названий ЖК представленных в задаче по одному при каждом запуске функции
    # что соответствует нулевому индексу (ЖК Горький -индекс 0, 18-индекс 1)
        cls.houses_history.append(args[0])
    #вoзврат  метода __new__из наследуемого класса в дочерний
        return object.__new__(cls)
    def __init__(self, name, numbers_of_floor):
            self.name = name
            self.numbers_of_floor = numbers_of_floor


    def __del__(self):
        print(f'Жилой комплекс : {self.name} - это здание снесено,но останется в истории ')

print("\n")
h1 = House ( ' "ЖК Горький" ',18)
print(House.houses_history)
h2 = House ('"Домик в деревне"',2)
print(House.houses_history)
h3 = House ('"Гусарская балада"',3)
print(House.houses_history)
print("\n")
# удаление атрибута заданного класса
del h2
del h3
del h1

print("________________________________________________________________________\n")
print("Жилые комплексы оставшиеся в истории")
print(House.houses_history)