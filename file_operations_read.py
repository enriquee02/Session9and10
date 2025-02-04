fp = open("text.txt") #open for reading

print(fp.read()) #print method gets the entire file content
fp.close() #this is good practice if you want to do other operations with the file

#same thing using context manager
# this is more pythonic
with open("text.txt", "r") as f:
    print(f.read())

#another way to take the file is to read them line by linen

with open("text.txt", "r") as f:
    for line in f: #f is iterable and we get each individual line
        print(line)

with open("text.txt", "r") as f:
    for line in f: #f is iterable and we get each individual line
        print(line, end="")
        print(line.rstrip())
