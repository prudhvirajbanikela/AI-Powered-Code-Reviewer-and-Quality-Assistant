# file = open("data.txt","w")
# file.write("hello, world!\n")
# file.write("welcome tp python programming.\n")

# file.close()



# file = open("data.txt","r")
# content = file.read()
# print(content)
# file.close()



file = open("data.txt","a")
file.write("This is an appended to the file.\n")
file.close()
