
def get_multiplied_digits(number):
    str_number = str(number) # представление переменной в строковом виде
    first =int(str_number[0]) # преобразование строки в число взяв только данные нулевого индекса
    if len(str_number)>1: # т.е не один элемент ,а более 1го
       return first*get_multiplied_digits(int(str_number[1:])) # функция вызывает саму себя после чего произойдет поочередное перемножение чисел между собой
    else:
        return first # если длина str_number не больше 1 элемента возвращается first,т.е если один только элемент,считать нечего ,функция останавливается
    

print (get_multiplied_digits(35508)) # в функцию задано число ,вывод в консоль (результат 3*5*5*8, нули пропускается ) =600
