summa = 0
count = 0
persons = []
with open("Ex03.txt") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split('-')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Заработали менее 20000: {persons}")
print(f"Средняя заработная плата: {result}")
