# recursion is a fucntion that calls itself

def linearAdd(num):
    # base case, where actually recusrion stops, and to avoid infinite recusrsion
    if (num == 1):
        return 1
    else: 
        print(num)
        # line within else is actual recussion call
        return num + linearAdd(num - 1)
    
print(linearAdd(5))


def factorial(num):
   call_stack = []
   if num == 1:
       print('base case reached! Num is 1.')
       return 1
   else:
       call_stack.append({'input': num})
       print('call stack: ', call_stack)
       return num * factorial(num-1)
 
factorial(5)

# why do we use a recursion?
# it produces clear and easy to read code
# it can be used to solve data structures problem
# it splits a complex problem into smaller parts

# examples
def countdown (num):
    stack = []
    if(num == 0):
        print('KABOOM!')
        return 0
    else:
        stack.append(num)
        print(num, stack)
        return countdown(num-1)

print(countdown(5))