a = input("Введите любое слово: ")


def int_func(a):
    return a.title()


print(int_func(a))

b = input("Введите слова латиницей: ".lower()).split()
c = []
for word in b:
    c.append(int_func(word))
print(c)
