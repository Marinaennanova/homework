

def single_root_words(root_words,*other_words): # создание функции с обязательным аргументом и неограниченную последовательность
    same_words = []
         for i in other_words: # переборка элементов переменной с неграниченной последовательностью
              if root_words.lower() in i.lower() or i.lower() in root_words.lower():
                  same_words.append(i) # добавить пременную в созданный пустой список

         print(root_words,other_words) # печать нового списка

         return same_words

res=single_root_words("мир","мирный","солнечный","мировой","мирок")
res2=single_root_words("Сахар","Сахарный","Засахаренный","Хлеб","Сахарок")
print(res)
print(res2)