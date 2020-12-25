#можно с помощью инпута запрашивать данные
# name = str(input("Введите ваше имя: "))
# surname = str(input("Введите вашу фамилию: "))
# day = int(input("Введите год своего рождения"))
# city = str(input("Введите город проживания: "))
# post = (input("Введите ваш адрес электронной почты: "))
# number = int(input("Введите ваш номер телефона"))
#
#
# def profile(name, surname, day, city, post, number):
#     print(name, surname, day, city, post, number)
#
#
# profile(name, surname, day, city, post, number)

#а это, как написано в задании
def profile(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)


profile(name='Евген', surname='Купченко', year=1985, city='Москва', email='email', phone='123456')
