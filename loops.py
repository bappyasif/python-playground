nums = [1,2,3,4]

for num in nums:
    print(num, num+1, num%2==0)

for i in range(2):
    print(i)

teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]

for team in teams:
    for player in team:
        print(player, team[0][0], team[1][0])

i=0

while (i<6):
    print(i)
    i+=1


# for loop
nums = [3, 4, 16]
 
print('This is an example of for loops')

for num in nums:
   print(num ** 2)
 
# while loop
i = 3

print('This is an example of while loops')

while i < 258:
   print(i)
   i = i ** 2
