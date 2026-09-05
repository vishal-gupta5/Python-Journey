# List in Python
marks = [90, 56, 93, 95, 67]

print(marks) # Print the list
print(marks[3]) # Access the particular index
print(type(marks)) # Find out the type of list

#! Methods on list
print(marks[3:]) # Slicing on List
marks.append(95) # Append the element at the end
print("After appending the element: ", marks) 

marks.insert(2, 50) # Insert the value at 2 index
print("After inserting the element at index 2", marks) 

marks.sort() # Arrange in increasing order
print("After sorting the list", marks) 

marks.reverse() # Reverse Order
print("After reversing the list", marks) 


#! Linear Search
index = 0
x = 67
for var in marks:
    if (var == x):
        print(f"{var} is at {index}")
        break
    index += 1