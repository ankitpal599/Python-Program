file = open("data.txt","w")
file.write("Hello World!\n")
file.write("I am Ankit Pal.")
file.close()

file = open("data.txt","r")
data = file.read()
print(data)
file.close()

file = open("data.txt","a")
file.write("\nI am currently pursuing BE.")
file.close()

file = open("data.txt","r")
for line in file:
    print(line)
file.close()

with open("data.txt","w") as file:
    file.write("I belong to Ayodhya")

with open("data.txt","r") as file:
    data = file.read()
    print(data)
