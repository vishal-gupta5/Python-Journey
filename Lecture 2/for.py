# For Loop
string = "hello"

for var in string:
    print(var)
    
    
# Print Sequence 1 to (n)

print("Print Sequence")
n = 10

for i in range(n):
    print(i + 1)
    
    
word = "artificial intelligence"
count = 0

for ch in word:
    if (ch == 'i'):
        count += 1
print("count of i = ", count)
print("Terminate the loop!")