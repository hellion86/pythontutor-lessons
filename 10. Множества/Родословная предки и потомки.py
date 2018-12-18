'''
Условие
Даны два элемента в дереве. Определите, является ли один из них потомком другого.

Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K. В каждой из следующих K строк, содержатся имена двух элементов дерева.

Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2, если второй является предком первого или 0, если ни один из них не является предком другого.
'''

#Мое решение

#Правильное решение
def poisk(search1,search2):
	s = search2
	while search2 in d:
		search2 = d[search2]
		if search2  == search1:
			return 1
	while search1 in d:
		search1 = d[search1]
		if s == search1:
			return 2
	return 0

d = {}
for i in range(int(input())-1):
    pot,rod = input().split()
    if rod not in d:
        d[rod] = None
    d[pot] = rod

for i in range(int(input())):
    p,r = input().split()
    print(poisk(p,r),end = ' ')


#Решение разработчиков
def is_ancestor(man, older_man):
    if man == older_man:
        return True
    while man in p_tree:
        man = p_tree[man]
        if man == older_man:
            return True
    return False
    
p_tree = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

for i in range(int(input())):
    first, second = input().split()
    if is_ancestor(second, first):
        print(1, end=' ')
    elif is_ancestor(first, second):
        print(2, end=' ')
    else:
        print(0, end=' ')
