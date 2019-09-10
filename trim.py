def trim(s):
	i = 0
	j = len(s)-1
	if len(s) == 0:
		return ''
	
	while s[i]==' 'and i < len(s)-1 :
		i+=1
	
	while s[j]==' ' and j>=1:
		j-=1
		
	if i == j:
		return ''
	return s[i:j+1]
	
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')