
#1. Создать программный файл в текстовом формате, 
#записать в него построчно данные, вводимые пользователем. 
#Об окончании ввода данных будет
# свидетельствовать пустая строка.

lines = ["Красный", "Желтый", "Зеленый"]
with open('001.txt', 'w') as fil:
    while True:
        line = input('Вводим текст')
        if line == '':
            break
        fil.write(line + '\n')

with open("001.txt", "r") as fil:
    print(fil.read())

