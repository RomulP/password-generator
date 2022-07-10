from random import choice

# сложность пароля в количестве символов
def generator(num):
	password = ""
	for i in range(num):
		x = choice('1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM')
		password += x

	return password

num = int(input('Введите количество знаков в пароле: '))
print(generator(num))