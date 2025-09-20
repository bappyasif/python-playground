name = "a b"

print("Hello", name)

print("Heelloo {name}")

print(f"Helloooo {name}")

print(f"Helloooo {name.upper()}")

print(f"Helloooo {name.format()}")

print("Helloooo ".format(name))

print('Very nice to meet you, {}!'.format(name))

print("greetings {}".format(name))

def greet() :
    name = input("What is your name?")
    hometown = input("Where are you from?")
    print(f"Very nice to meet you {name} from {hometown}")

greet()