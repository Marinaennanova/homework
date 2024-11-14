from module_4.alg import*
a = list(map(int,input("Введите числа через пробел:").split()))
b = list(map(int,input("Введите числа через пробел:").split()))

bubble_sort(a)
select_sort(b)
print(a)
print(b)