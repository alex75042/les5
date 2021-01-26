#4. Создать (не программно) 
#текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл 
#на чтение и считывающую построчно данные.
#При этом английские числительные должны 
#заменяться на русские. Новый блок строк должен
#записываться в новый текстовый файл

with open('004.txt', encoding='utf-8') as fil_en:
    lines = fil_en.readlines()
    print(lines)


with open('0041.txt', 'w') as fil_ru:

    for line in lines:
        if '1' in line:
            line = line.replace('One', 'один')
            fil_ru.write(line)
        elif '2' in line:
            line = line.replace('Two', 'два')
            fil_ru.write(line)
        elif '3' in line:
            line = line.replace('Three', 'три')
            fil_ru.write(line)
        elif '4' in line:
            line = line.replace('Four', 'четыре')
            fil_ru.write(line)
with open('0041.txt') as fil_ru:
    fil_ru_lines = fil_ru.readlines()
print(fil_ru_lines)