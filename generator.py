#生成器
g =  (x*x for x in range(1,10))
print(g)
#打印generator的每一个元素
def fib(max):
	n,a,b = 0,0,1
	while n<max:
		yield b #返回值
		a,b = b, a+b
		n += 1
	return 'done'

f = fib(6)
print(f)
#变成generator的函数，
#在每次调用next()的时候执行，
#遇到yield语句返回，
#再次执行时从上次返回的yield语句处继续执行。

for n in fib(6):
	print(n)
	
g = fib(6)
while True:
	try:
		x = next(g)
		print('g',x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
# -*- coding: utf-8 -*-
def triangles():
    Last = [1]
    yield Last         #返回第一行
    while 1:
        L = [1]        #每行开头的1
        for x in range(1,len(Last)):
                L.append(Last[x-1]+Last[x])
                       #中间满足:L[x]=Last[x-1]+Last[x]
        L.append(1)    #每行最后的1
        Last = L[:]    #新生成的行在下次迭代时作为上一行
        yield L        #返回新生成的行

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')