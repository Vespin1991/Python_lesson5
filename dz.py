# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 1 способ решения
# text = 'мы пошлиабв пришли дляабв из магазина банкаабв'
# text_new = text.split(" ")
# print(text_new)
# spisok = []
# for i in text_new:
#     if "абв" not in i:
#         spisok.append(i)
# print(*spisok)

# 2 способ решения
# text = 'мы пошлиабв пришли дляабв из магазина банкаабв'
# text_new = text.split(" ")
# print(text_new)
# spisok = [i for i in text_new if "абв" not in i]
# print(*spisok)

# 3 способ решения
# text = 'мы пошлиабв пришли дляабв из магазина банкаабв'
# text_new = text.split(" ")
# print(text_new)
# spisok = list(filter(lambda slovo: "абв" not in slovo, text_new))
# print(*spisok)


# 2.Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# from random import randint
# a = randint(0, 9)
# b = randint(0, 9)
# print(f"Вывод первого случайного целого числа {a}")
# print(f"Вывод второго случайного целого числа {b}")
# if a > b:
#     print('        ХОДИТ ПЕРВЫЙ ИГРОК')
# else:
#     print('        ХОДИТ ВТОРОЙ ИГРОК')
# x = 193
# x_new = 0
# sum1 = 0
# sum2 = 0
# if a > b:
#     while x != 0:
#         if x > 30:
#             print('    1 игрок введите число от 1 до 28 :')
#             q = int(input())
#             x_new = x - q
#             x = x_new
#             sum1 = sum1 + q
#             print(f'у вас {sum1} конфет')
#             print(f'осталось {x} конфет')
#         else:
#             print('              1 игрок win')
#             print(f'первому игроку нужно было взять {sum1} конфет ')
#             break
#         if x > 30:
#             print('    2 игрок введите число от 1 до 28 :')
#             w = int(input())
#             x_new = x - w
#             x = x_new
#             sum2 = sum2 + w
#             print(f'у вас {sum2} конфет')
#             print(f'осталось {x} конфет')
#         else:
#             print('              2 игрок win')
#             break
# else:
#     while x != 0:
#         if x > 30:
#             print('    2 игрок введите число от 1 до 28 :')
#             q = int(input())
#             x_new = x - q
#             x = x_new
#             sum1 = sum1 + q
#             print(f'у вас {sum1} конфет')
#             print(f'осталось {x} конфет')
#         else:
#             print('              2 игрок win')
#             break
#         if x > 30:
#             print('    1 игрок введите число от 1 до 28 :')
#             w = int(input())
#             x_new = x - w
#             x = x_new
#             sum2 = sum2 + w
#             print(f'у вас {sum2} конфет')
#             print(f'осталось {x} конфет')
#         else:
#             print('              1 игрок win')
#             print(f'первому игроку нужно было взять {sum2} конфет ')
#             break

# Создайте программу для игры в ""Крестики-нолики"".

# lst_0 = ['-', '-', '-']
# lst_1 = ['-', '-', '-']
# lst_2 = ['-', '-', '-']
# spl_0 =str(lst_0).split(',')
# spl_1 =str(lst_1).split(',')
# spl_2 =str(lst_2).split(',')
# p = [1,2,3]
# ri = [4,5,6]
# mer = [7,8,9]
# print('   Добро пожаловать в игру крестики и нолики. Первыми ходят крестики')
# print('Нужно указать позицию от 1 до 9, куда нужно поставить крестик либо нолик')
# print(p)
# print(ri)
# print(mer)
# g = 0 
# while g < 10:
#     if g < 4:
#         a = int(input('1 игрок введите позицию крестика : '))
#         if a == 1:
#             spl_0[0] = '[x  '
#         elif a == 2:
#             spl_0[1] = '  x '
#         elif a == 3:
#             spl_0[2] = '   x]'
#         elif a == 4:
#             spl_1[0] = '[x  '
#         elif a == 5:
#             spl_1[1] = '  x '
#         elif a == 6:
#             spl_1[2] = '   x]'
#         elif a == 7:
#             spl_2[0] = '[x  '
#         elif a == 8:
#             spl_2[1] = '  x '
#         elif a == 9:
#             spl_2[2] = '   x]'
#         print(*spl_0)
#         print(*spl_1)
#         print(*spl_2)
#         if (('[x  ' in spl_0 and '  x ' in spl_0 and '   x]' in spl_0)
#         or  ('[x  ' in spl_1 and '  x ' in spl_1 and '   x]' in spl_1)
#         or  ('[x  ' in spl_2 and '  x ' in spl_2 and '   x]' in spl_2)
#         or  ('[x  ' in spl_0 and '  x ' in spl_1  and '   x]' in spl_2)
#         or  ('   x]' in spl_0 and '  x ' in spl_1  and '[x  ' in spl_2)
#         or  ('[x  ' in spl_0 and '[x  ' in spl_1 and '[x  ' in spl_2)
#         or  ('  x ' in spl_0 and '  x ' in spl_1 and '  x ' in spl_2)
#         or  ('   x]' in spl_0 and '   x]' in spl_1 and '   x]' in spl_2)
#         ):
#             print('ПОБЕДА ЗА КРЕСТИКАМИ')  
#             break
#         a = int(input('2 игрок введите позицию нолика : '))
#         if a == 1:
#             spl_0[0] = '[o  '
#         elif a == 2:
#             spl_0[1] = '  o '
#         elif a == 3:
#             spl_0[2] = '   o]'
#         elif a == 4:
#             spl_1[0] = '[o  '
#         elif a == 5:
#             spl_1[1] = '  o '
#         elif a == 6:
#             spl_1[2] = '   o]'
#         elif a == 7:
#             spl_2[0] = '[o  '
#         elif a == 8:
#             spl_2[1] = '  o '
#         elif a == 9:
#             spl_2[2] = '   o]'
#         print(*spl_0)
#         print(*spl_1)
#         print(*spl_2)
#         if (
#             ('[o  ' in spl_0 and '  o ' in spl_0 and '   o]' in spl_0)
#         or  ('[o  ' in spl_1 and '  o ' in spl_1 and '   o]' in spl_1)
#         or  ('[o  ' in spl_2 and '  o ' in spl_2 and '   o]' in spl_2)
#         or  ('[o  ' in spl_0 and '  o ' in spl_1  and '   o]' in spl_2)
#         or  ('   o]' in spl_0 and '  o ' in spl_1  and '[o  ' in spl_2)
#         or  ('[o  ' in spl_0 and '[o  ' in spl_1 and '[o  ' in spl_2)
#         or  ('  o ' in spl_0 and '  o ' in spl_1 and '  o ' in spl_2)
#         or  ('   o]' in spl_0 and '   o]' in spl_1 and '   o]' in spl_2)
#         ):
#             print('ПОБЕДА ЗА НОЛИКАМИ')
#             break
#         g = g + 1
#     else:
#         a = int(input('1 игрок введите позицию крестика : '))
#         if a == 1:
#             spl_0[0] = '[x  '
#         elif a == 2:
#             spl_0[1] = '  x '
#         elif a == 3:
#             spl_0[2] = '   x]'
#         elif a == 4:
#             spl_1[0] = '[x  '
#         elif a == 5:
#             spl_1[1] = '  x '
#         elif a == 6:
#             spl_1[2] = '   x]'
#         elif a == 7:
#             spl_2[0] = '[x  '
#         elif a == 8:
#             spl_2[1] = '  x '
#         elif a == 9:
#             spl_2[2] = '   x]'
#         print(*spl_0)
#         print(*spl_1)
#         print(*spl_2)
#         if (('[x  ' in spl_0 and '  x ' in spl_0 and '   x]' in spl_0)
#         or  ('[x  ' in spl_1 and '  x ' in spl_1 and '   x]' in spl_1)
#         or  ('[x  ' in spl_2 and '  x ' in spl_2 and '   x]' in spl_2)
#         or  ('[x  ' in spl_0 and '  x ' in spl_1  and '   x]' in spl_2)
#         or  ('   x]' in spl_0 and '  x ' in spl_1  and '[x  ' in spl_2)
#         or  ('[x  ' in spl_0 and '[x  ' in spl_1 and '[x  ' in spl_2)
#         or  ('  x ' in spl_0 and '  x ' in spl_1 and '  x ' in spl_2)
#         or  ('   x]' in spl_0 and '   x]' in spl_1 and '   x]' in spl_2)
#         ):
#             print('ПОБЕДА ЗА КРЕСТИКАМИ')  
#             break
#         else:
#             print('К СОЖАЛЕНИЮ НИКТО НЕ ВЫИГРАЛ. ПОПРОБУЙТЕ СНОВА')
#             break


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
print('Введите ,что хотите сделать : 1 - сжатие , 2 - восстановление')
a = int(input())
if a == 1:
    print('Введите набор букв, цифр или символов в формате "aaaqqqEEEE333####" ')
    qw = input() 
    i = 0
    summ = 1
    new = []
    while i <= len(qw):
        if len(qw) == summ:
            new.append(summ)
            new.append(qw[i])
            break
        if qw[i] == qw[i+1]:
            summ = summ + 1
        else:
            new.append(summ)
            new.append(qw[i])
            qw = qw[summ:len(qw)+1]
            i = -1
            summ = 1
        i = i + 1
    print(*new)
else:
    print('Введите сжатый файл в формате "1p2^3j4Q" ')
    qw = input()
    i = 0
    sp = []
    while i < len(qw):
        rep = qw[i+1][:i+1]
        sp.append(rep*int(qw[i]))
        i = i + 2
    print(*sp)
# если ввести двузначное число и более ,то не сработает(код не доработан,понимаю это)




        



