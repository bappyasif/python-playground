name = "bappy"

name = "a b"

temp = 96.69

sum = 4 + 5

casted = str(sum)

print(f"hello {name} {temp} {sum} {casted}", type(casted) == str, type(sum) == int, type(temp) == float, type(name) == str, type(casted), type(sum), type(temp), type(name))

def variables() :
    int_val = 4
    print(int_val, type(int_val))

    print()

    float_val = float(int_val)
    print(float_val, type(float_val))

variables()