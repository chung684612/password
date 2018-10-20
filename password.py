x = 3
c_password = 'a123456'
while x > 0 :
	x -= 1
	password = input('請輸入密碼: ')
	if password == c_password:
		print('登入成功')
		break
	else:
		if x > 0:
			print('密碼錯誤! 還有', x, '次機會')
		else:
			print('登入失敗')