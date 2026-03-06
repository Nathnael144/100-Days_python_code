#Random number
import random
x=random.randint(a=1, b=10)
print(x)

random_number_0_to_1= random.random()
print(random_number_0_to_1)

random_float= random.uniform(a=1,b=10)
print(random_float)

random_head_tails= random.randint(a=0,b=1)

if random_head_tails==0:
    print("Heads")
else:
    print("Tails")
    
#python list
import random   
name = ["nati","abeni","kebe","fanos","bena"]
x= random.choice(name)
print(x)