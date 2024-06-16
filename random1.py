import random

r = random.randint(1, 100)

while True:
	guess = input('請輸入數字: ')
	guess = int(guess)
	if guess == r:
		print('恭喜猜對!')
		break
	else:
		if guess > r:
			print('比答案大...')
		else:
			print('比答案小...')