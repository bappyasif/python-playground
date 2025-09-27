# create function

def add_three(num1, num2, num3):
    sumThree = num1 + num2 + num3
    return sumThree

print(add_three(1, 2, 3))

# parameters, when used in function definitions
def greetings(language):
    if(language == 'spanish'):
        greet='Hola'
    
    elif(language == 'french'):
        greet = 'Bonjour'

    elif(language == 'english'):
        greet = 'Hello'
    
    elif (language == 'dutch'):
        greet = 'Hallo'

    return greet

# arguments, when used in function calls
print(greetings('english'))
print(greetings('french'))
print(greetings('spanish'))
print(greetings('dutch'))

