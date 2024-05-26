print('welcome to my quiz game ')
#lets know the user wants to play the game or not
start = input('Do you want play? ')

if start.lower() != "yes":
    quit()

print("Yay lets play")
score = 0
answer = input("What is CPU? ")
if answer.lower()=="central processing unit":
    print("Correct :)")
    score += 1
else:
    print("Incorrect :(")
print("you got "+str(score)+" Questions Correct")
print("you got "+str((score/1)*100)+"%")
