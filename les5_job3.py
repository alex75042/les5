#3. Создать текстовый файл (не программно). 
#Построчно записать фамилии сотрудников и
#величину их окладов (не менее 10 строк). 
#Определить, кто из сотрудников имеет оклад менее
#20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода
# сотрудников.

#Пример файла:

#Иванов 23543.12
#Петров 13749.32


with open('003.txt', encoding='utf-8') as fil:
    lines = fil.readlines()
    print(lines)

income = []
income_min = []
a = '\n'
for line in lines:
    name, incom = line.split(': ')
    print(incom)
    #incom  = incom.replase('\n', '')
    #for i in range(len(incom)):
      #  if


    income .append(incom)
print(income)
for el in income:
    print(el)
    #el = el.replase('\n', '')
    income_f = sum([int(el[:el.find('\n')]) for el in income if '\n' in el])
    if int(el) < 20000:
        income_min.append(line)
       # print(line, end='')
print('', income_min)
#print('', sum(income) / len(income), '\n')