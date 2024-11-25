class Database:

    def __init__(self):
        self.data = {}

    def add_user(self,username,password):
        self.data[username] = password


class User:

    """
    Класс пользователя содержащий логин и пароль

    """
    def __init__(self,username,password,password_confirm):
        self.username = username
        if password == password_confirm:
           self.password = password

if __name__ == "__main__":
    database = Database()
    while True:
        choice = int(input("Привет,выбирите действие :\n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Введите логин:")
            password = input("Введите пароль:")
            if login in database.data:
               if password == database.data[login]:
                  print(f"Вход выполнен,{login}")
                  break
               else:
                   print("Неверный пароль!")
            else:
                print("Пользователь не найден")
        if choice == 2:
           user = User(input("Введите логин:"),password:=input("Введите пароль:"),
                       password2 := input("Повторите введение пароля:"))
           if password != password2:
               print("Пароли не совпадают попробуй еще раз!")
               continue
           database.add_user(user.username,user.password)
