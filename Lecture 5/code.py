# f = open("./Lecture 5/sample.txt", "r")
# f = open("./Lecture 5/sample.txt", "w")
# f = open("./Lecture 5/sample.txt", "a")
f = open("./Lecture 5/sample2.txt", "x")

# data = f.read()
# print(data)


# data2 = f.readline()
# print(data2)

f.write("text to overwrite \n the complete data")

f.write("New text is being appended \n to the file")

f.close()