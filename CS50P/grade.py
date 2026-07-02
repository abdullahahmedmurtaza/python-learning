score = int(input("Enter Your Score : "))
if(score >= 90 and score <= 100):
    print("You got an A")
elif(score >= 80 and score < 90):
    print("You got an B")
elif(score >= 70 and score < 80):
    print("You got an C")
elif(score >= 60 and score < 70):
    print("You got an D")
else: 
    print("You got an F")

# Smaller code with much more tightened up logic

if(90 <= score <= 100):
    print("You got an A")
elif(80 <= score < 90):
    print("You got an B")
elif(70 <= score < 80):
    print("You got an C")
elif(60 <= score < 70):
    print("You got an D")
else: 
    print("You got an F")

# ignoring the upper and lower bounds by checking just one thing
# Much more clean and readable
if(score >= 90):
    print("You got an A")
elif(score >= 80):
    print("You got an B")
elif(score >= 70):
    print("You got an C")
elif(score >= 60):
    print("You got an D")
else: 
    print("You got an F")

    

