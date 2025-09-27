nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

try:
    print(sum(nums))
except Exception as e:
    print("Cannot print the sum! Your variables are not numbers.", e.__cause__)

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

try:
    print(sum(nums))
except Exception as e:
    print("Cannot print the sum! Your variables are not numbers.", e)


try:
    print(sum())
except: 
    print("Cannot print the sum! Your variables are not numbers.")
finally:
    print("Done! finally blocked runs")


nums = [5, 2, 3, 10]
 
try:
   avg = sum(nums) / len(nums)
   print('The average of the list is: ', avg)
 
except:
   print('Cannot compute average - make sure you enter a list of integers!')
 
finally:
   print('Feel free to rerun the code with another list of integers!')