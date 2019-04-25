#ex19 

def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")
	
print("We can just give the function numbers directly: ")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers (amount_of_cheese,amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 四种values的给法:
'''We can give it straight numbers. 
We can give it variables. 
We can give it math. 
We can even combine math and variables.'''

# 注：避免variable的名字和function中的variable名称相同