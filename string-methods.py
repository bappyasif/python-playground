# strings are deined by single or double quotes
# strings can contain letters, numbers, spaces and special characters

# escaping characters
# we can use escape characters to include special characters in a string
# backslash is used to escape characters
txt = "She said \"Never let go\"."
print(txt) # She said "Never let go".

# in syntax
# in syntax is used to determine if a letter or a substring exists in a string
#  it retruns a boolean value
print("hello" in "hello world")
print("h" not in "hello")

# iterate over a string
# we can use a for loop to iterate over a string
for i in "hello":
    print(i)

# string concatenation
# we can use the + operator to concatenate strings
print("hello" + " " + "world")

# strings are immutable
# we can't change the value of a string
# we can't add or remove characters from a string


# string indexing and slicing
# we can use indexing to access certain characters in a string
# python uses a 0 based indexing
intro = "hello world"
print(intro[0])
print(intro[1])
# we can also slicing a string
print(intro[0:5])
print(intro[6:])
# we can also use negative index to access characters from the end of the string
print(intro[-5:-1])
print(intro[-5:])

# common built in methods

# len()
# returns the length of the string
# it takes a string as an argument and returns its length
# it also counts spaces as characters
print(len(intro))

# str.lower, str.upper(), str.title()
# returns the string in lowercase, uppercase and title case respectively
print(intro.lower())
print(intro.upper())
print(intro.title())

# str.split()
# returns a list of substrings based on a separator
# it takes a string and a separator as arguments
# it splits the string into substrings based on the separator and turns them into a list
print(intro.split(" "))

# str.format()
# returns a formatted string
# it takes a string and a variable number of arguments as arguments
# it replaces the placeholders denoted by {} in the string with the values of the arguments
print("Hello {} {}".format("Bappy", "Sarkar"))

# str.strip()
# returns a copy of the string with leading and trailing whitespace removed
# it takes a string as an argument and returns a copy of the string with leading and trailing whitespace removed
print("   Hello World   ".strip())
print("   Hello World   ".lstrip()) # removes leading whitespace
print("   Hello World   ".rstrip()) # removes trailing whitespace
print("....+Hello World+....".strip(".")) # removes leading and trailing dots
print("....+....Hello World..+....".strip(".+")) # removes leading and trailing dots and plus signs

#str.find()
# returns the index of the first occurrence of a substring in a string
# it takes a string and a substring as arguments and returns the index of the first occurrence of the substring in the string
# it returns -1 if the substring is not found
print(intro.find("o"))

# str.replace()
# returns a copy of the string with all occurrences of a substring replaced with another substring
# it takes a string and two substrings as arguments and returns a copy of the string with all occurrences of the first substring replaced with the second substring
print(intro.replace("o", "OOOooOOO"))

# str.join()
# returns a string that is the concatenation of the strings in a sequence
# it takes a sequence or list of strings as an argument and returns a string that is the concatenation of the strings in the sequence
print(",".join(["a", "b", "c"]))