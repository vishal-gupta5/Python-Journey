# Tuples in Python
tup = (1, 2, 3, 4, 5)

print(tup)
print(tup[3])
print(type(tup))
print(len(tup))

#! We can't define tup = (1)
t = (1) # Expression
print(type(t))

t = (1,) # tuple
print(type(t))


# Sum of tuple 
sum = 0

for var in tup:
    sum += var
print(sum)