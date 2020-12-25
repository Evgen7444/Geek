a = int(input("Введите первое число: "))
b = int(input("Введиет второе число: "))


def div(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "На ноль делить нельзя, мамкин математик!"


print(div(a, b))
