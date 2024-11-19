
class House:

    def __init__(self,name,numbers_of_floor):

        self.name = name
        self.numbers_of_floor = numbers_of_floor

    def __len__(self):
        return self.numbers_of_floor

    def __str__(self):
        return (f"Название жилого комплекса : {self.name},количество этажей в комплексе  {self.numbers_of_floor}")

h1 = House ("ЖК Горький",18)
h2 = House ("Домик в деревне",2)
h3 = House ("Гусарская балада",3)
print(h1)
print(h2)
print(h3)
print(len(h1))
print(len(h2))
print(len(h3))
