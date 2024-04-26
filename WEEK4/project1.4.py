# Author: Paulina Flores
# Project 1.4: Adding a function and data structures to your scenario

# Objective: So for this posting, take your existing code and add a function and 
# either a list or a dictionary to it to create a new version to post.  
# For example, you might move code you have that prints the result of your decision scenario into 
# a separate function, and for using a data structure, you might put say a list of choices for the user 
# into a Python list and then program printing those out.  

carwashes = ["461 E. Westminster Ave. Orlando, FL 32835", "9619 Wrangler Dr. Orlando, FL 32818", "7372 Manhattan Dr. Orlando, FL 32812"]

def main():
    print("Should I wash my car now?\n") #main 
    print("Please answer in a Y/N format.")

def get_info():
    smudges = input("Does it have smudges? \n")
    if smudges == "N":
        print("Forget about it.")
    elif smudges == "Y":
        time = int(input("What time is it currently? (Hour format: 24hrs, 1-24)\n"))
        rain = input("Is it raining outside? \n")
        mud = input("Is it muddy outside? \n")
        money = input("Do you have enough money right now? \n")
        if time >= 20 and rain == "N" or mud == "Y" and money == "Y":
            print("You should wash your car. Get your stuff together!\n")
            print("Here is a list of carwashes closest to you. \n")
            print(carwashes)
        else:
            print("You should not wash your car yet.")
main()
get_info()
