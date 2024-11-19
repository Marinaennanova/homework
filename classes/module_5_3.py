class House:

    def __init__(self,name,numbers_of_floor):

        self.name = name
        self.numbers_of_floor = numbers_of_floor
#реализация специального метода __len__()', который будет возвращать кол-во этажей в комплексе.
    def __len__(self):
        return self.numbers_of_floor

# реализация специального метода __str__()', который будет возвращать название комплекса.
    def __str__(self):
        return (f"Название жилого комплекса : {self.name},количество этажей в комплексе  {self.numbers_of_floor}")

    def __eq__(self, other):
        return self.numbers_of_floor == other.numbers_of_floor

    def __lt__(self, other):
        return self.numbers_of_floor < other.numbers_of_floor

    def __le__(self, other):
        return self.numbers_of_floor < other.numbers_of_floor

    def __gt__(self, other):
        return self.numbers_of_floor > other.numbers_of_floor

    def __ge__(self, other):
        return self.numbers_of_floor >= other.numbers_of_floor

    def __ne__(self, other):
        return self.numbers_of_floor != other.numbers_of_floor

    def __add__(self, other):
        return self.numbers_of_floor + other.numbers_of_floor

    def __radd__(self, value):
        if isinstance(self,int):
           return self

    def __iadd__(self, value):
        if isinstance(self, int):
           return self

h1 = House ("ЖК Горький",18)
h2 = House ("Домик в деревне",2)
h3 = House ("Гусарская балада",2)
print(h1)
print(h2)
print(h3)
print(len(h1))
print(len(h2))
print(len(h3))
print(h1==h2)    #__eq__метод
print(h2==h3)    #__eq__метод
print(h1<h2)     # __lt__метод
print(h2<h3)     # __lt__метод
print(h1<h2)     #__le__
print(h2<h3)     #__le__
print(h1>h2)     #__gt__
print(h2>h3)     #__gt__
print(h1>=h2)    #__ge__
print(h2>=h3)    #__ge__
print(h1!=h2)    #__ne__
print(h2!=h3)    #__ne__
print(h1+h2)     #__add__
print(h1+h1)     #__radd__
print(h2+h3)     #__iadd__

