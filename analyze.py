from random_username.generate import generate_username

# welcome user
def welcomeuser():
    print("\nwelcome to the text analysis tool, i will mine and analyze a body of text from the file you give me!")
# Get username
def getusername():
      # Get input from user into the terminal
    usernamefrominput = input("\nTo begin, please enter your username:\n")
    
    if len(usernamefrominput) < 5 or not usernamefrominput.isnotvalididentifier:
        print("your username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9), have no spaces, an cannot start with a number!")
        print("Assigning new username....")
        return generate_username() [0]      
    
    return usernamefrominput   
   
# Greet the user
def greetuser(name):
    print('Hello, ' + name)

welcomeuser()
username = getusername()
greetuser(username)

     
