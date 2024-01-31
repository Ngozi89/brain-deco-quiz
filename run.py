print("Welcome to Brain Deco Quiz App")
# Let player choose if they want to play or quit
player = input("Do you want to play Brain Deco Quiz? ")

# Check If user condition is true. If yes then play else quit
if player.lower() != "yes":
    quit()
else:
    print("Okay, lets' go :)")    

# Set question for user to answer 
answer = input("What country has the highest life expectancy? ")
if answer.lower() == "hong kong":
    print("Correct!")
else:
    print("Incorrect!")    