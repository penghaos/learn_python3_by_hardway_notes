
from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")
	
	
	while True:
		choice = input("Please enter a number which is more than 0 and less than 50 \n >>> ")
		if choice.isdigit(): #检验是否所有字符都为数字
		#学习【异常处理】有关内容
		#if isinstance(int(choice),int):	#检验choice是不是整数，错误
			how_much = int(choice)
		 
			if how_much < 50 and how_much > 0:
				print("Nice, you're not greedy, you win!")
				exit(0)
			elif how_much > 50:
				dead("You greedy bastard!")
			else:
				dead("Man, learn to type a number.")
				
		else:
			print("Man, I said you enter a number.")
		
def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False
	
	while True:
		choice = input("Please enter 'take money' or 'taunt bear'  \n >>> ")
		
		if choice == "take money":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" :
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bear_moved = True
			
			while bear_moved:
				choice_second = input("Please enter 'taunt bear' or 'open door' \n >>>")
			# input 要放在while语句中，否则会无限循环
				if choice_second == "taunt bear":
					dead("The bear gets pissed off and chews your leg off.")
				elif choice_second == "open door":
					gold_room()
				else:
					print("Enter right name.")
		else:
			print("I got no idea what that means.")
			
def cthulhu_room():
		print("Here you see the great evil Cthulhu.")
		print("He, it, whatever stares at you and you go insane.")
		print("Do you flee for your life or eat your head?")
		
		choice = input("Enter 'flee' or 'head' \n >>> ")
		
		if "flee" in choice:
			start()
		elif "head" in choice:
			dead("Well that was tasty!")
		else:
			cthulhu_room()
			
def dead(why):
	print(why,"Good job!")
	exit(0)
	
def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")
	
	begin = True #我加的
	while begin: #我加的
		
		choice = input("choose 'left' or 'right' \n >>> ")
		
		if choice == "left":
			bear_room()
		elif choice == "right":
			cthulhu_room()
		else:
			#dead("You stumble around the room until you starve.")
			print("please enter a right string.")
start()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	