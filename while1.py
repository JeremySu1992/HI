password = 'a123456'
chance = 3
while chance > 0:
	i_pass = input('請輸入密碼: ')
	if i_pass != password:
		chance -= 1		
		if chance > 0:
			print('密碼錯誤! 還有', chance, '次機會')
	else:
		print('登入成功!')
		break
if chance == 0:
	print('登入失敗...')