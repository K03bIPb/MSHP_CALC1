def str_simple():
 f = input()
 if f == '+':
     print('Введите первую строку:')
     s1 = input()
     print('Введите вторую строку:')
     s2 = input()
     print('Сумма двух строк:')
     print(s1+s2)
 elif f == '*':
     print('Введите строку:')
     s = input()
     print('Введите множитель')
     n = int(input())
     print('Ответ:')
     print(n*s)
 elif print('ошибка: введите верное действие') & str_simple():
     pass