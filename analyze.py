# welcome user
def welcomeuser():
    print("\nwelcome to the text analysis tool, i will mine and analyze a body of text from the file you give me!")
# Get username
def getusername():
      # Get input from user into the terminal
    usernamefrominput = input("\nTo begin, please enter your username:\n")
    return usernamefrominput
# Greet the uer
def greetuser(name):
    print('Hello, ' + name)

welcomeuser()
uername = getusername()
greetuser(uername)
    
