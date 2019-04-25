from sys import exit

def buy_shoes():
	print("看下Nike、Adidas、Newbalance")
	print("好看吗？")
	while True:
		good_looking = input("输入yes或no \n>>>")
		if  good_looking == 'yes':
			price()
		elif good_looking == 'no':
			not_buy()
		else:
			print("别闹，好好输入。")
		
def price():
	while True:
		x = input("价格是多少？超过500块吗？\n>>>")
		if x.isdigit():
			x = int(x)
			if x < 500:
				anta()
			else:
				not_buy()
		else:
			print("你输入的不是数字。")
			
def anta():
	print("欢迎来到'安踏官方旗舰店'")
	while True:
		y = input("安踏多少钱？超过300吗？\n>>>")
		if y.isdigit():
			y = int(y)
			if y > 300:
				print("好贵，不买了。")
			elif y < 300:
				print("真便宜，买安踏吧。")
				print("???怎么又买安踏？")
				not_buy()
		else:
			print("你输入了啥玩意?")

def not_buy():
	print("算了，不买了。")
	exit(0)

buy_shoes()