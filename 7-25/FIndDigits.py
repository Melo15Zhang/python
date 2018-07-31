str = ""

with open("String.txt", "r") as f:
    str = f.readline()

# print(str)
newStr = ""
for x in str:
    if x.isdigit():
        newStr += x

print(newStr)