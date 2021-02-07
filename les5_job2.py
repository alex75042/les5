#2. Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить
#подсчёт строк и слов в каждой строке.
#lines = ()
#with open('002.txt') as fil:
 #   lines = fil.readlines()
#print(lines)
#print('Строк в тексте - ', len(lines))
#for num_line, line in enumerate(lines, start=1):
 #   print('В строке ', num_line, ' - cлов ', len(line.split()))

with open('002.txt', encoding='utf-8') as f:

    lines = f.readlines()
    print(lines)
print('Строк в тексте - ', len(lines))
for num, line in enumerate(lines, start=1):
    print('{} строкa ‚ - cлов {} '.format(num, len(line.split())))
