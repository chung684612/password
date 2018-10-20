x = 0
c_password = 'a123456'
while x < 3 :
	password = input('請輸入密碼: ')
	if password == c_password:
		print('登入成功')
		break
	else:
		x += 1
		print('密碼錯誤! 還有', 3 - x, '次機會')