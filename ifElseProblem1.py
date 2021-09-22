#Write a program to prompt for a score between 0.0 and 1.0. 
#If the score is out of range, print an error. 
#If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade >= 0.9 A || >= 0.8 B || >= 0.7 C || >= 0.6 D || < 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. 
#For the test, enter a score of 0.85.

score = input('Enter Score: ')

if (float(score) >= 0.9): #1st: Condition, False 1st: Condition
    print("A")
elif (float(score) >= 0.8): #2nd: Condition, True 
    print("B") # print("B") is returned and the if else statement terminates
elif (float(score) >= 0.7): #3rd: Condition, this does not execute because the 2nd condition was true
    print("C")
elif (float(score) >= 0.6): #4th: Condition, this does not execute because the 2nd condition was true
    print("D") 
elif (float(score) < 0.6): #5th: Condition, this does not execute because the 2nd condition was true
    print("F")
else:
    print("Value entered is not within the correct range.")
