#迭代
def findMinAndMax(L):
	if L==[]:
		return (None, None)
	tempMin = tempMax = L[0]
	for i in L:
		if i>tempMax:
			tempMax = i
		if i<tempMin:
			tempMin = i
	
	return (tempMin, tempMax)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')