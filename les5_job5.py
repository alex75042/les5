#5. Создать (программно) текстовый файл, 
#записать в него программно набор чисел,
#разделённых пробелами. 
#Программа должна подсчитывать сумму 
#чисел в файле и выводить её на экран

with open('005.txt', 'w') as fil:
    n = input('Целые числа через пробел. вводим ')
    fil.write('числа - ' + n + '\n')
    num = map(int, n.split())
    s_num = sum(num)
    fil.write('сумма чисел: ' + str(s_num))
print('сумма чисел ', n, ' = ', s_num)
