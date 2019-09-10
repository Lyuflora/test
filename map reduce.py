#高阶函数
# map
#将传入的函数依次作用到序列的每个元素，
#并把结果作为新的Iterator返回
def f(x):
	return x*x
	
r = map(f,[1,3,5,7,9])
print(list(r))

#reduce
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#这个函数必须接收两个参数，
#reduce把结果继续和序列的下一个元素做累积计算

#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#别人的
def normalize(name):

    result = evname[0:].upper()+evname[1:len(name)].lower()

    return result