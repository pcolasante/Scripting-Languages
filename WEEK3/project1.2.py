#Author: Paulina Flores

#Projects 1.2 and 1.3: Post your scenarios and python implementations here

#Purpose: The goal of this exercise is to give you some experience thinking about and implementing if, elif and else, 
#along with a handful of relational operators such as == and logical operators such as and and or.

#Objective: Create a Python program that makes the decision(s) 
#described in the scenario you claimed. 
#Code if, elif and else statements, with and, or, >, <, ==, and so on as needed to implement your 
#interpretation of the scenario you claimed. If you can work in a List or a Dictionary, so much the better.

#Scenario: If my car has smudges and it's after 8 p.m and it's not raining outside or it's very muddy outside 
#and I have enough money, then I will wash my car. 

print("Should I wash my car now?\n")  # main
smudges = input("Does it have smudges? (Y or N)\n")
if smudges == "N":
    print("Forget about it.")
elif smudges == "Y":
    time = int(input("What time is it currently? (Hour format: 24hrs, 1-24)\n"))
    rain = input("Is it raining outside? (Y or N)\n")
    mud = input("Is it muddy outside? (Y or N)\n")
    money = input("Do you have enough money right now? (Y or N)\n")

if time >= 20 and rain == "N" or mud == "Y" and money == "Y":
    print("You should wash your car. Get your stuff together!\n")
else:
    print("You should not wash your car yet.\n")
    if time < 20:
        print("It's too early, you could wait until later. \n")
    if rain == "Y":
        print("You should stay inside, and get a warm drink. \n")
    if money == "N":
        print("Hmm. You should save money first. \n")


print('Bye!')
