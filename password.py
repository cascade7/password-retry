password = 'a123456'
count=3
while count>=0 :
	count = count - 1
	pwd = input('請輸入密碼: ')
	if pwd == password :
		print('登入成功')
		break
	else:
		print('密碼錯誤 剩下',count,'次機會')
		if count == 0:
			print('登入失敗')
			break