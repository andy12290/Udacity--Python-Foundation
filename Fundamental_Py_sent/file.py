# write into the text file
text = "save this file \n New line"

saveFile = open('example.txt', 'w')

# write in file
saveFile.write(text)
saveFile.close()

# README FILE
readme = open('example.txt', 'r').read()
print(readme)

# this is how we are going to solve the first example
change = int(input("Enter input:"))
quarter = int(change/25)
dime = int(change/10)
cents = (change-dime*10)
print(quarter)
print(dime)
print(cents)




