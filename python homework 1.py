# a умножить на b равно c; c является решением линейного уравнения ax + b = 0
print('Условие первое: произведение A и B равно C.')
print('Условие второе: C является решением линейного уравнения AX + B = 0.')
a = int(input('Введите A: '))
b = int(input('Введите B: '))
c = int(input('Введите C: '))
if a*b == c and a*c+b == 0:
    print('Оба условия выполняются.')
elif a*b == c:
    print('Выполняется только первое условие.')
elif a*c+b == 0:
    print('Выполняется только второе условие.') 
else:
    print('Ни одно из условий не выполняется.')
