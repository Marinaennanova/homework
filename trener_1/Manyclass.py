class Human:
    def __init__(self,name,group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):

        print(f"Hello,меня зовут {self.name} ")


class StudentGroup:
    def __init__(self,group):
        self.group = group

    def about(self):
        print(f"{self.name}  учится в группе {self.group}")


class Student(Human,StudentGroup):
    def __init__(self,name,place,group):
        super().__init__(name,group)
        self.place = place
        super().info()


# human = Human("Дениска")
# print(human.name)
student = Student("Максимка"," я из МАГУ","Питон 1")
student.about()
print(Student.mro()) # метод для просмотра цепочки наследования классов