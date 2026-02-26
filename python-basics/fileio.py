#name: Elvis Mutuma
# Date : 23/02/2026
# Program to perform file operations

#create new file
new_file = open("stdent_data.txt","r+")

#write to new file
new_file.write("{Student Name : Bob Afwata, ID : 29783789, email : bobafwata@gmail.com}")
new_file.close()


#read from the file
new_file = open("stdent_data.txt","r+")
data = new_file.read()

print(data)

new_file.close()

#delete file
# us os module
import os
os.remove("remove.txt")


