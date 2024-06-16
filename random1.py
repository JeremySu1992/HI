import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1
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
	print('這是第', count, '次猜數字')
print('在第', count, '次猜對')