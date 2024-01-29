import random
import string

alphabets = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to password generator")

length=int(input("Enter the length of the password:"))

while True:

    n_alphabets=int(input("How many letters you want in your password:\n"))
    n_numbers=int(input("How many numbers you want in your password:\n"))
    n_symbols=int(input("How many symbols you want in your password:\n"))
    
    password=[]
    
    if n_alphabets+n_numbers+n_symbols != length:
           print("The sum of number of alphabets,numbers and symbols should be equal to the length given")
            
    
    else:
                    
    
        for i in range(1,n_alphabets+1):
            char = random.choice(alphabets)
            password += char
    
        for i in range(1,n_numbers+1):
            char = random.choice(numbers)
            password += char
    
        for i in range(1,n_symbols+1):
            char = random.choice(symbols)
            password += char
    break       

random.shuffle(password)
print("Your secured password is: ",end='')
for char in password:
    print(char,end='')