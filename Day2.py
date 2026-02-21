#Data Type 

print("Hello"[2])
print(123)
print(True)
print(len("hello"))
print(type("hello"))
print(int("123"))

#x=input ("my name ")
#print("The number of letter in my name is :" + str(len(x)))

print (6/3)
print(5//2)
print(2**3)

# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
# Convert this sentence into code on line 6.

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi =(weight/(height**2))

print(bmi)
print(round(bmi))
print(round(bmi,2))

#f - string
score=1
height=2.1
Winner=True

print(f"your score is = {score}, your height is {height}. you are winning: {Winner}")

#project
print("Welcome to the tip calculator!")
bill=input("What was the total bill?")
tip= input("How much tip would you like to give? 10, 12 or 15?")
people= input("How many people to split the bill?")

total= (float(bill)*(float(tip)/100) +float(bill))/int(people)
print(f"Each person should pay ${total}")





