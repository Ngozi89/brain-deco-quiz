print("Welcome to Brain Deco Fun General Knowledge Quiz Game")
# Let player choose if they want to play or quit
player = input("Do you want to play Brain Deco Quiz? ")

# Check If user condition is true. If yes then play else quit
if player.lower() != "yes":
    quit()
else:
    print("Okay, lets' go :)")  

 # Let player enter name 
name = input("Enter your name ")
"Name: "
print("Hi", str(name))
score = 0 
# Set question for user to answer 
answer = input("How many minutes are in a full week? ")
if answer.lower() == "10,080":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is 10,080")    

answer = input("What year was the United Nations established? ")
if answer.lower() == "1945":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is 1945")    

answer = input("What country has the highest life expectancy? ")
if answer.lower() == "hong kong":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Hong Kong")

answer = input("What disease commonly spread on pirate ships? ")
if answer.lower() == "scurvy":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Scurvy")

answer = input("Which langauge has the more native speakers? ")
if answer.lower() == "spanish":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Spanish")

answer = input("Aureolin is a shade of what color ")
if answer.lower() == "yellow":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Yellow")

answer = input("Which planet has the most moons? ")
if answer.lower() == "saturn":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Saturn")

answer = input("What country has won the most World Cups ")
if answer.lower() == "brazil":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Brazil")

answer = input("In what country was Elon Musk born? ")
if answer.lower() == "south africa":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is South Africa")

answer = input("Where is the strongest human muscle located? ")
if answer.lower() == "jaw":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Jaw")

answer = input("How many hearts does an octopus have? ")
if answer.lower() == "3":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is 3")

answer = input("What planet is closest to the sun? ")
if answer.lower() == "mercury":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Mercury")

answer = input("What phone company produced the 3310? ")
if answer.lower() == "nokia":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Nokia")

answer = input("What is the tallest type of tree? ")
if answer.lower() == "redwoods":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Redwoods")

answer = input("What colors is the flag of the United Nations? ")
if answer.lower() == "blue and white":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Blue and White")

answer = input("What country drinks the most coffee? ")
if answer.lower() == "finland":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is Finland")

answer = input("Where did sushi originate? ")
if answer.lower() == "china":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is China")

answer = input("How many dots appear on a pair of dice? ")
if answer.lower() == "42":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is 42")

answer = input("How many bones do we have in an ear? ")
if answer.lower() == "3":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("The answer is 3")

answer = input("What city is known as The Eternal City? ")
if answer.lower() == "rome":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 
    print("The answer is Rome")

print("Thank you for playing Brain Deco Quiz, you got " + str(score) + " questions correct")      