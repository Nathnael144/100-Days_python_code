#For loop
fruits=["apple","peach","pear"]
for fruit in fruits:
    print(fruit)
    
student=[150,120,20,30,40]
sum=0
for score in student:
    sum+=score
print(sum)

max_score=0

for score in student:
    if score > max_score:
        max_score=score

    
print(max_score)


for i in range (1,10):
    print(i)

s=0

for i in range(1,101):
    
    s+=i
print(s)

#coding exercise

'''FizzBuzz

You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:


    Your program should print each number from 1 to 100 in turn and include number 100.


    But when the number is divisible by 3 then instead of printing the number it should print "Fizz".


    When the number is divisible by 5, then instead of printing the number it should print "Buzz".`


    And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz" '''

for number in range (1,101):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")  
    elif number%5==0:
        print("Buzz")
    else:
        print(number
              
#project
'''    Query successful

Gemini said

Based on the image provided, here is the text transcribed from the code editor and the project description panel:
Left Side: Python Code Editor
Python

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', ...
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level

Right Side: Project Description

Password Generator Project
Description
... and loops to complete the challenge.

Easy Version
Generate the password in sequence. Letters, then symbols, then numbers. If the user wants 4 letters, 2 symbols and 3 numbers then the password might look like this:
*fgdx$924

You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

Hard Version
When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:
x$d24g*f9

And every time you generate a password, the positions of the symbols, numbers, and letters are different. This will make the password more difficult...'''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', ...
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level        
for i in letters:

           
    

    