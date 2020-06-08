# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [ index.name for index in humans if index.name[:1] == 'D']
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [index.name for index in humans if index.name[-1:] == 'e']
#for index in humans:
#    if index.name[-1:] == 'e':
#        b.append(index.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [index.name for index in humans if index.name[:1] == 'C'  or index.name[:1] == 'D' or index.name[:1] ==  'E' or index.name[:1] == 'F' or index.name[:1] ==  'G']
#for index in humans:
#    if index.name[:1] == 'C'  or index.name[:1] == 'D' or index.name[:1] ==  'E' or index.name[:1] == 'F' or index.name[:1] ==  'G':
#        c.append(index.name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [int(index.age+10) for index in humans]
#for index in humans:
#    d.append(int(index.age+10))
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f'{index.name}-{index.age}' for index in humans]
#for index in humans:
#    e.append(f'{index.name}-{index.age}')
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(index.name, index.age) for index in humans if index.age >= 27 and index.age <= 32]
#for index in humans:
#    if index.age >= 27 and index.age <= 32:
#        f.append((index.name, index.age))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(index.name.upper(), index.age+5) for index in humans]
#for index in humans:
#    g.append(Human(index.name.upper(), index.age+5))
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(index.age) for index in humans]
#for index in humans:
#    h.append(math.sqrt(index.age))
print(h)
