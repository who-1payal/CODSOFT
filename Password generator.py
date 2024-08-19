#Password Generator 

import random

lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
             'u','v','w','x','y','z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
             'U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

print("Welcome to Password Generator!!")

#Prompting user to specify the desired length and complexity of the password
length = int(input("Enter the length of your password:"))
complexity = input("Enter the complexity of the password(low,medium,high):")

if complexity == 'low':
    combined_list = numbers + lowercase
elif complexity == 'medium':
    combined_list = numbers + lowercase + uppercase
elif complexity == 'high':
    combined_list = numbers + lowercase + uppercase + symbols

random.shuffle(combined_list)

#Generating password
password = ""
for i in range(length):
    password += random.choice(combined_list)
    
#Displaying the password
print("Generated password:",password)


