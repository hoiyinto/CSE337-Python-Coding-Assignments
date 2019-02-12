from q5_p1 import validPassword

valid=False

while valid==False:
	username=input("Please enter a username: ")
	pwd=input("Please enter a password: ")
	valid=validPassword(username,pwd)
	if valid==False:
		print("Invalid password! Please try again!")






