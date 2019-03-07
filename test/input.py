#/usr/bin/env python3

high = int(input('您的声高：\n'))
weigh = int(input('您的体重：\n'))


bmi = weigh / high*high

if bmi < 18.5:
	print('过轻')
elif bmi < 25:
	print('正常')
elif bmi <29:
	print('过重')
elif bmi <32:
	print('肥胖')
else :
	print('严重肥胖')

 	
