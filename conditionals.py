score = 90

if(score >= 80):
    print("You pass this test")

score = 70

if(score < 80):
    print("You fail this test")

score = 60

if(score >= 80):
    print("You pass this test", score, " out of 80")
else:
    print(f"You fail this test {score}/80")

score = 70

if(score >= 80):
    print("You pass this test in flying colors", score, " out of 80")
elif(score >= 60):
    print(f'You pass this test {score}/80, go see your instructors')
else:
    print(f"You fail this test {score}/80")


score = 82
 
if score >= 92:
   print('Your final grade is an A')
 
elif score >= 85:
   print('Your final grade is a B')
 
elif score >= 70:
   print('Your final grade is a C')
 
else:
   print('Talk with your instructor about your grade!')