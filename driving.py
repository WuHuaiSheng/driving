country = input('請問你是哪國人(台灣或美國): ')
if country == '台灣':
	age = input('請輸入年齡: ')
	age = int(age)
	if age >= 18:
		print('台灣人已達可以考駕照年齡')
	else:
		print('還不能考駕照')
elif country == '美國':
	age = input('請輸入年齡: ')
	age = int(age)
	if age >= 16:
		print('美國人已達可以考駕照年齡')
	else:
		print('還不能考駕照')
elif country != '台灣' and country != '美國':
	print('只能輸入台灣/美國')
