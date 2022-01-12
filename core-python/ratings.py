"""Restaurant rating lister."""
import os, sys, random

# put your code here
def main():
    my_dict = dict()
    print(os.listdir("./Restaurants"))
    file = input("Choose a file to work with\nEnter file name exactly!:\n")

    def read_makeDict(shouldPrint):
        s = open(f'./Restaurants/{file}', "r")
        lines = s.readlines()
        for x in lines:
            y = x.strip().split(":")
            my_dict[y[0]] = y[1]
        if shouldPrint:
            sortAndPrint()

    def sortAndPrint():
        sortedKeys = dict(sorted(my_dict.items(), key = lambda x: x[0].lower()))
        for k, v in sortedKeys.items():
            print(f'{k} is rated at {v}.')
    sortAndPrint()
    
    def userAdd():
        newKey = input("Type a new restaurant to add:\n")
        def ratingCheck():
            newRating = int(input(f"Enter in a rating for '{newKey}'\n"))
            if newRating >= 1 and newRating <= 5:
                my_dict[newKey] = newRating
                sortAndPrint()
            else:
                print("Please provide a rating 1-5")
                ratingCheck()
        ratingCheck()

    def updateRandom():
        read_makeDict(False)
        entry_list = list(my_dict.keys())
        # print(entry_list)
        randChoice = random.choice(entry_list)
        print(f"The random restaurant: '{randChoice}' currently has a rating of: {my_dict.get(randChoice)}")
        newVal = input(f"What should the new rating for {randChoice} be?\n")
        my_dict[randChoice] = newVal
        sortAndPrint()

    def update():
        read_makeDict(True)
        thisChoice = input("Which one do you want to update?\nENTER NAME EXACTLY!:\n")
        def rateCheck():
            updatedRating = int(input(f"What is the new rating for {thisChoice}? Must be 1-5:\n"))
            if updatedRating >= 1 and updatedRating <= 5:
                my_dict[thisChoice] = updatedRating
                sortAndPrint()
            else:
                print("Please enter a rating 1-5")
                rateCheck()
        rateCheck() 

    def giveChoices():
        choice = input("Do you want to 'SEE', 'ADD', 'RANDOM', 'UPDATE', 'LIST' or 'QUIT'? Enter choice here:\n")
        if choice == "SEE":
            read_makeDict(True)
            giveChoices()
        elif choice == "ADD":
            userAdd()
            giveChoices()
        elif choice == "RANDOM":
            updateRandom()
            giveChoices()
        elif choice == "UPDATE":
            update()
            giveChoices()
        elif choice == "QUIT":
            sys.exit("Quitting... Good.py, my friend!")
        elif choice == "LIST":
            print(os.listdir("./Restaurants"))
        else:
            print("Please enter a valid keyword:\n")
            giveChoices()
    giveChoices()
main()