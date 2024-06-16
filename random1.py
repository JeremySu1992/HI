import random

limit = input('請輸入最大值整數範圍: ')
limit = int(limit)

r = random.randint(1, limit)
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