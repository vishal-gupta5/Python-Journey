# Dictionary in Python

info = {
    "name" : "Vishal",
    "cpga" : 8.6,
    "subjects": ["Maths", "Computer Science"],
    3.14 : "PI"
}

print(info) # Print Dictionary

dict_keys = info.keys(); # Return Keys
print(dict_keys)

dict_values = info.values() # Return values
print(dict_values)

print(info.items()) # Print all items

info.update({
    "degree" : "Master of Computer Application"
})

print(info.items())

# print(info["cpga2"]) # Wrong Way

print(info.get("cgpa2")) # None

print("End the program")