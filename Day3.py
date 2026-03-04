print("Welcome to ticket office")

height=int(input("What is your height in cm?"))

if height>80:
    print("your can buy the ticket")
else:
    print("chenge the position to buy the ticket")
    

#modulo operator
x= int(input ("check the number is even or odd "))

if x%2==0:
    print("Even number")
else:
    print("Odd number")
    
print("BMI calculator")

weight= float(input("What is your weight? "))
height= float(input("What is your height? "))    

BMI= weight/(height**2)
if BMI<18.5:
    print("under weight")
elif 18.5<= BMI<25:
    print("normal weight")
elif BMI>=25:
    print("over weight")
else:
    print("The input is wrong")
    
    
    
#  project   
    
    
'''Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25

Add beef for small pizza (Y or N): +$2

Add beef for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Interaction

Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: N

Your final bill is: $28.'''

print("Welcome to Pizza delivery")
S= 15
M= 20
L= 25
size=input("what size of pizza do you want? S, M or L")
beff= input("do you want beff on your pizza? Y or N")
extra_chess= input("do you want extera chess? Y or N")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("The input is wrong")
if beff=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_chess=="Y":
    bill+=1
print(f"Your final bill is: ${bill}")

    
 







    