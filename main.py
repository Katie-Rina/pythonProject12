'''Напишите функцию read_last(lines, file), которая будет открывать
определенный файл file и выводить на печать построчно последние строки
в количестве lines (на всякий случай проверим, что задано положительное целое число).
Протестируем функцию на файле «article.txt» со следующим содержимым:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела'''

# def read_last(lines, file):
#     text = file.read().splitlines()
#     if len(text) < lines:
#         print('-1')          # если введено число большее, чем количество строк в файле
#     else:
#         for i in range(-lines, 0):
#             print(text[i])
#
#
# name = input('Имя файла: ')
# n = float(input('Количество выводимых строк: '))
# while n < 1 or int(n) != n:
#     print('Введите целое положительное число!')
#     n = float(input('Количество выводимых строк: '))
# n = int(n)
# with open(name, 'r', encoding='utf-8') as article:
#     read_last(n, article)


'''Документ «article.txt» содержит следующий текст:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела

Требуется реализовать функцию longest_words(file),
которая записывает в файл result.txt слово, имеющее максимальную длину
(или список слов, если таковых несколько).'''

# def longest_words(file):
#     max = 0
#     text = file.read().splitlines()
#     res = open('res.txt', 'w')
#     for i in range(len(text)):
#         line = text[i].split()
#         for j in range(len(line)):
#             if len(line[j]) > max:
#                 max = len(line[j])
#                 res.close()
#                 res = open('res.txt', 'w')
#                 res.write(line[j])
#                 res.write('\n')
#             elif len(line[j]) == max:
#                 res.write(line[j])
#                 res.write('\n')
#
# name = input('Имя файла: ')
# with open(name, 'r', encoding='utf-8') as article:
#     longest_words(article)
