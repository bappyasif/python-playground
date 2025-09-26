# pass, break and continue within loops

# pass
# pass keyword is mostly used as a placeholder in a loop. 
# Nothing gets executed when pass is placed under a condition

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
for name in names:
    if name == 'Manny':
        pass
    elif 'j' in name.lower():
        pass
    # elif 'j' in name:
    #     pass
    else:
        print(name)
    # print(name)


# break
# break keyword is used to break out of a loop, conditional statements.

print('\n \n')
names2 = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

for na in names2:
    if 'h' in na.lower():
        break
    else:
        print(na)


# continue
# continue keyword skips over an iteration when condition is met and moves onto next iteration

print('\n continue')
names3 = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

for name in names3:
    if 'm' in name.lower():
        continue
    else:
        print(name)

    
# examples
print('\n')

names = ['Amanda', 'Mercedes', 'Rachel', 'Elisabeth', 'Tay', 'Xavier', 'Joaquin', 'Sam']
 
for name in names:
  if 'm' in name.lower():
      continue
  elif 'r' in name.lower():
      pass
  elif 'j' in name.lower():
      break
  else:
       print(name)