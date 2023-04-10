#Password Checker Practice

#Task: Print the username and have the password blocked and show how many characters it is

#len = length of string! Don't forget

username = input('what is your username? ')  
password = input('what is your password? ')  

passwordLength = len(password)
hiddenPassword = "*" * passwordLength

print("---------------------")

print(f'Hello {username}, your password {hiddenPassword} is {passwordLength} letters long')