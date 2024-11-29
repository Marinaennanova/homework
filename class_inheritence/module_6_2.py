class Vehicle:
   __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

   def __init__(self,owner:str,__model:str,__engine_power:int,__color:str):
       self.owner = owner # владелец транспорта
       self.__model = __model # модель (марка) транспорта. (мы не можем менять название модели)
       self.__engine_power = __engine_power # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
       self.__color = __color # название цвета. (мы не можем менять цвет автомобиля своими руками)



   def get_model  (self): #- возвращает строку: "Модель: <название модели транспорта>"

       return (f"Модель авто :{self.__model}")

   def get_horsepower (self): #- возвращает строку: "Мощность двигателя: <мощность>"

       return (f"Мощность двигателя:{self.__engine_power}")
   def get_color(self):  #- возвращает строку: "Цвет: <цвет транспорта>"

       return (f"Цвет:{self.__color}")

   def print_info (self):
       print(self.get_model())
       print(self.get_horsepower())
       print(self.get_color())
       print (f'Владелец:{self.owner}')
   def set_color(self,new_color:str):
       if new_color.lower() in  (self.__COLOR_VARIANTS):
           self.__color = new_color
       else:
           print(f"Нельзя сменить цвет на новый  {new_color}")
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass
    # def __init__(self, owner, model,color,engine_power):
    #     super().__init__(owner, model, engine_power, color)

print(dir(Vehicle))
print(dir(Sedan))
if __name__ == "__main__":

  vehicle1 = Sedan('Petrov Sergey', 'Toyota Corola', 'blue', 500)
  vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
  vehicle1.set_color('Pink')
  vehicle1.set_color('Green')
  vehicle1.owner = 'Ivanov Ivan'
# Проверяем что поменялось
  vehicle1.print_info()

