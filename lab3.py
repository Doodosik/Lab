import math

Title = 'БАГ-20-02, Миловзоров А.В., Вариант 5'
an = input('Введите начальное значение a: ').split('/')
ak = input('Введите конечное значение a: ').split('/')
da = input('Введите шаг Δa: ').split('/')


def correct(i):
    p = 0
    while p < len(i):
        b = list(i[p])
        if 'π' in b and len(b) > 1:
            b.remove('π')
            if ''.join(b) == '-':
                k = '-1'
            else:
                k = ''.join(b)
            i[p] = float(k) * math.pi
        elif 'π' in b and len(b) == 1:
            i[i.index('π')] = math.pi
        else:
            p += 1
            continue
        p += 1
    if len(i) == 2:
        return float(i[0]) / float(i[1])
    elif i[0] == '' or len(i) > 2:
        return 'Ошибка!'
    else:
        return float(i[0])


an = correct(an)
ak = correct(ak)
da = correct(da)

# Расчёты с помощью арифметического цикла ("Для")
print('       Расчёты арифметического цикла       ')
print('*******************************************')
print('*      a      *      x      *      g      *')
print('*******************************************')

for n in range(1, int((ak - an) / da) + 2, 1):
    a = an + da * (n - 1)
    x = math.exp(a) + math.exp(-a)
    g = 0.5 * x - 2 * math.cos(x + math.pi / 4)
    print('*  ' + str(round(a, 4)) + ' ' * (10 - len(str(round(a, 4)))) + ' *   ' + str(round(x, 4)) + ' ' * (
            10 - len(str(round(x, 4)))) + '*   ' + str(round(g, 4)) + ' ' * (10 - len(str(round(g, 4)))) + '*')
    n += 1
print('*******************************************')

# Расчёты с помощью цикла "Пока"
print('            Расчёты цикла "Пока"           ')
print('*******************************************')
print('*      a      *      x      *      g      *')
print('*******************************************')

a = an
while a <= ak:
    x = math.exp(a) + math.exp(-a)
    g = 0.5 * x - 2 * math.cos(x + math.pi / 4)
    print('*  ' + str(round(a, 4)) + ' ' * (10 - len(str(round(a, 4)))) + ' *   ' + str(round(x, 4)) + ' ' * (
            10 - len(str(round(x, 4)))) + '*   ' + str(round(g, 4)) + ' ' * (10 - len(str(round(g, 4)))) + '*')
    a += da
print('*******************************************')
print(Title)
