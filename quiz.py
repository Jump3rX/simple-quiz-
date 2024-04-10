print("Welcome to Quizzy!")
playing = input("Do you want to play? y/n>> ").lower()

if playing != "y":
    quit()
print("Okay,lets play! :)")
score = 0
answer = input("What does cpu stand for?>> ").lower()
if answer == "central processing unit":
    score +=1
    print("Correct!")
else:
    print("Incorrect!")


answer = input("What does GPU stand for?>> ").lower()
if answer == "graphics processing unit":
    score +=1
    print("Correct!")
else:
    print("Incorrect!")



answer = input("What does RAM stand for?>> ").lower()
if answer == "random access memory":
    score +=1
    print("Correct!")
else:
    print("Incorrect!")


answer = input("What does PSU stand for?>> ").lower()
if answer == "power supply unit":
    score +=1
    print("Correct!")
else:
    print("Incorrect!")

print("You got " + str(score) + " points!")
print("You got "+ str((score/4)*100)+"%")