read_f = open("Ex02.txt")
content = read_f.read()
print(content)

read_f = open("Ex02.txt")
content = read_f.readlines()
print(f'Количество строк в файле - {len(content)}')

read_f = open("Ex02.txt")
content = read_f.readlines()
for i in range(len(content)):
    print(f'кличество символов {i + 1}-ой строки {len(content[i])}')

read_f = open('Ex02.txt')
content = read_f.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')

read_f.close()
