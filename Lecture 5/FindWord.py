# Find out the word "DataNew"

data = True
line = 1
word = "dataNew"

with open("./Lecture 5/sample.txt", "r") as f:
    while data:
        data = f.readline();
        
        if (word in data):
            print(f"{word} Found at line {line}")
            break
        
        print(data)
        line += 1