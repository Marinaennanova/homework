my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
noun = 0
while noun < len(my_list) : # переменная noun отслеживает
    # текущую позицию в списке и в цикле продолжается до тех пор пока
    # переменная не достигнет конца списка

   if int(my_list[noun]) > 0 :
      print(my_list[noun])
   noun = noun + 1
   if int(my_list[noun]) < 0 :
       break
else :
    print(my_list[noun])

