# 嵌套 if-statements inside if-statements

print(""" You enter a dark room with two doors.
Do you go through door # 1 or door . #2?""")

door = input("> ")

if door == "1":
	print("Three's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")
	
	bear = input("> ")
	
	if bear == "1":
		print("The bear eats your face off. Good job!")
	elif bear == "2":
		print("The bear eats your legs off. Good job!")#想要更多选项，可以加更多 elif:
	else:
		print(f"Well doing {bear} is probably better.")
		print("Bear runs sway.")
		
elif door == "2":
	print("You stare into the endless abyss at Cthulhu's retina.")
	print("1. Blueberries.")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")
	
	insanity = input("> ")
	
	if insanity == "1" or insanity == "2":
		print("Your body survives powered by a mind of jello.")
		print("Good job!")
	else:
		print("The insanity rots your eyes into a pool of muck.")
		print("Good job!")
else:
	print("You stumble around and fall on a knife and die. Good job!")
	
# 想用一串数字可以用 0 < x < 10 或者 1 <= x < 10 ，再或者 x in range(1,10) 右边是开区间，左边是闭区间