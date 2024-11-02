

calls = 0
def count_calls () : # подсчет вызывов остальных функций
    global calls#глобальная переменная заведена в тело функции для подсчета в будущем  количества всех вызванных функций
    calls+=1 # подсчет

def string_info (string) : # принимает аргумент строку и возвращает кортеж из длины этой строки
#  в верхнем и нижнем регистре
    count_calls() # вызов функции счетчика
    string = "Мама мыла раму "
    my_tuple = tuple(string.upper()) # преобразование в кортеж в верхнем регистре
    my_tuple_2 = tuple(string.lower())  # преобразование в кортеж в нижнем регистре
    print(my_tuple)
    print(my_tuple_2)
    return len(my_tuple),len(my_tuple_2)
string_info ("Мама мыла раму ")
def is_contains (s="Порошок",l="вода") : # принимает два аргумента
    count_calls() # вызов функции счетчика
    print(s,l)
    if "Порошок" in s:
           print(True)
    if "вода" is not l:
        print(False)

is_contains ()
string_info ("Мама мыла раму ")
is_contains ()
print(calls) # выводит на экран кол-во вызвоных функций