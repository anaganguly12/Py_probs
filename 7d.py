email = input("Enter a email address: ")
at = email.index('@')
dot = email.index('.')
final = email[at+1:dot]

print("The company name is: ", final)
