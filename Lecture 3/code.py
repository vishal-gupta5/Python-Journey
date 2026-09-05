# Strings in Python

word = "python"

print(len(word)) # find out the "length" of string
print(word + " Lover") # String concatenate
print(word[2]) # access the value of index 2
print(word[2 : 4]) # slicing the string
print(word[-4 : -2]) # slicing the string in reverse order

a = 10
b = 5
sum = a + b

# Normal formatting
print("sum is: {}".format(sum));

# Index based formatting
print("sum of {1} & {0} is: {2}".format(a, b, sum))

# Value based formatting
print("values of vars {a} & {b}".format(a = 5, b = 20))

# f-strings
print(f"sum of {a} & {b} is: {a + b}")
print(f"Avg of {a} & {b} is: {(a + b) / 2}")