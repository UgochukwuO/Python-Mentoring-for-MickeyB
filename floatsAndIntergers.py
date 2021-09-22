# difference between float and int 
# A Floating point number is simply a number with a decimal point. ex 2.343, 4322.04, 3.14 
# A Integer is simply whole number. ex. 5, 2, 343454535354, 

# If you do a mathematical operation (+, -, *, /) with an integer and a float, the resulting value will be a floating point number. int(5) + 4.5 = 9.5


#find the radius of a circle

pi = 3.14 # float / floating point number
r = 3 # integer

radiusOfACirlce = pi*r**2 # The resulting value will be a float. Output = 28.26


print(radiusOfACirlce)



#what is a scenario in life that you would only use whole numbers?

#hmm your age?

# okay lets write a program that adds together to peoples ages

age1 = 26
age2 = 23

sumOfAge = age1 + age2

print("The sum of " + str(age1) + " and " + str(age2) + " is = " + str(sumOfAge))


#this is an example where you only want to be using integers. 

#if we run that it wont create a problem for us because we are adding 
#integers and string? 

#good catch, yes it will. but we can use fuction to convert integers to strings as well. one moment...

#no problem, would that function be str()?!!!! 

#YES
