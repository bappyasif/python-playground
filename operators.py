# arithmatic operators
a=3
b=4

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# assignment operators (e.g. =, op=)
print("assignment operators")
print(a, b)
a += b
print(a, b)
a -= b
print(a, b)
a *= b
print(a, b)
a /= b
print(a, b)
a %= b
print(a, b)
a **= b
print(a, b)
a //= b
print(a, b)

# comparison operators
a = 3
b = 4

print("comparison operators")
print(a, b)
print(a == b)
print(a != b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# logical operators
a = 3
b = 4

print("logical operators")
print(a, b)
print(a and b)
print(a or b)
print(not a)
print(not b)
print(a >= b and a <= b)
print(a >= b or a <= b)
print(not (a >= b and a <= b))
print(not (a >= b or a <= b))

def operators(): 
    x = 3
    y = 4
    print(x, y)

    print("arithmatic operator (x=y): ", x+y)
    print("comparison operator (x=y): ", x==y)
    print("logical operator (x==y) OR (x > y): ", x==y or x>y)
    print("logical operator (x<y) AND (x > y): ", x<y and x>y)

operators()