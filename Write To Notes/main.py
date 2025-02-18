# Gavin Pierce Write To Notes
#
#
#
#How do you find a file in a folder? 
#
#
#
#In a python project how do you open a file?
#
#
#
#What is the difference between writing, appending, and creation modes?
#
#
#

#"""
#
#r= to read the file
#w= write on the file
#w+ = read and write
#a apennd (adds doesnt delete)
#(replaces old file)
#x= create a file
#a+ = append and read

#"""
#
#
#with open("writeing/test.csv", "a") as file:
#    file.write("i have changed this file forever")
#    print(file.read())

import csv
data = [
    {"usernam": "larose","color": "green"},
    {"usernam": "maxwell","color": "blue"}
]

with open("notes/user_names.csv", "w+", newline="") as file:
    fieldnames = ["username" , "color"]
    writer=csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)



#with open("notes/user_names.csv", "w", newline="") as file:
#    writer = csv.writer(file)
#    
#    writer.writerow([["silly_username", "black"],["odd_one", "pink"], ["user_is","orange"]])

#with open("notes/user_names.csv", "w", newline="") as file:
#    writer = csv.writer(file)
#    reader = csv.reader(file)
#    next(reader)
#    for row in reader:
#        print(f"user name: {row[0]} color: {row[1]}")