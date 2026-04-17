# 4.3 Counting to twenty
for num in range (1,21):
  print (num)

# 4.4 One Million
for a in range (1,31):
  print (a) 

# 4.5 Summing a million
numbers = list(range (1,31))

print (sum(numbers))
print(max(numbers))
print(min(numbers))

# 4.6 Odd numbers
odd_numbers = list(range (1,31,2))
print(odd_numbers)

# 4.7 Multiples of three
threes = list (range(3,31,3))
for b in threes:
  print(b) 

#4.8 Cubes
cubes= []
for t in range (1,11):
  cube= t**3
  cubes.append(cube)

#4.9 Cube comprehension
cubes_comprehension = [value**3 for value in range(1, 11)]
print(cubes_comprehension)

