
def password (n) : # функция которая имеет параметр n который будет принимать значение аргумента
    pole = " " # пустая строка

    for i in range (1,n) :
         for j in range (i+1,n) :
            if n % (i + j) == 0 :
               pole = str(i) + str(j)

    return (pole) # оператор завершающий выполнение функции и возвращает ее результат  вызывающему коду

print (password(int(input("Введите число от 3 до 20 :")))) # вызов функции password и введение числа от 3 до 20
print (password(int(input("Введите число от 3 до 20 :"))))
print (password(int(input("Введите число от 3 до 20 :"))))

