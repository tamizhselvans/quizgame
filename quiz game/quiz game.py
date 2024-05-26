print('welcome to my quiz game ')
#lets know the user wants to play the game or not
start = input('Do you want play? ')

if start.lower() != "yes":
    quit()

print("Yay lets play")
score = 0
#questions and answer path
answer = input("What is CPU? ")
if answer.lower()=="central processing unit":
    print("Correct :)")
    score += 1 #increment the score in above to see the results
else:
    print("Incorrect :(")

answer = input("What is GPU? ")
if answer.lower()=="graphical processing unit":
    print("Correct :)")
    score += 1
else:
    print("Incorrect :(")

answer = input("What is IC? ")
if answer.lower() == "integrated circuit":
    print("Correct :)")
    score += 1
else:
    print("Incorrect :(")
answer = input("What is RAM? ")
if answer.lower() == "random access memory":
    print("Correct :)")
    score += 1
else:
    print("Incorrect :(")

answer = input("What is ROM? ")
if answer.lower() == "read only memory":
    print("Correct :)")
    score += 1
else:
    print("Incorrect :(")
#results of your game
print("you got "+str(score)+" Questions Correct")
print("you got "+str((score/5)*100)+"%")
#just leave this input() i made this line so the python console doesnt quit
input()