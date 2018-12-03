'''
Условие
Политическая жизнь одной страны очень оживленная. В стране действует K политических партий, каждая из которых регулярно объявляет национальную забастовку. Дни, когда хотя бы одна из партий объявляет забастовку, при условии, что это не суббота или воскресенье (когда и так никто не работает), наносят большой ущерб экономике страны.

i-я партия объявляет забастовки строго каждые b_i дней, начиная с дня с номером a_i. То есть i-я партия объявляет забастовки в дни a_i, a_i + b_i, a_i + 2 * b_i и т.д. Если в какой-то день несколько партий объявляет забастовку, то это считается одной общенациональной забастовкой.

В календаре страны N дней, пронумерованных, начиная с единицы. Первый день года является понедельником, шестой и седьмой дни года — выходные, неделя состоит из семи дней.

В первой строке даны числа N и K. Далее идет K строк, описывающие графики проведения забастовок. i-я строка содержит числа a_i и b_i. Вам нужно определить число забастовок, произошедших в этой стране в течении года.
'''

#Мое решение
n,m = input().split()
zab = set()
for j in range(int(m)):
    s,e = input().split()
    for k in range(int(s),int(n)+1,int(e)):
        zab.add(k)
 
zab -= set(range(6, int(n) + 1, 7))
zab -= set(range(7, int(n) + 1, 7))
print(len(zab))

#Правильное решение
N, K = [int(s) for s in input().split()]
work_days = set([day for day in range(1, N + 1) if day % 7 not in (6, 0)])
no_strikes = set(work_days)
for party in range(K):
    a, b = [int(s) for s in input().split()]
    max_strikes = (N - a) // b + 1
    no_strikes -= {a + b*i for i in range(max_strikes)}
print(len(work_days) - len(no_strikes))
