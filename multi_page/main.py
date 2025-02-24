#Gavin Pierce, Multiple Python pages notes

#How do you make multiple files in python?

# make new file ending in .py
# Snake case file nmaes
#discrpitive file names

#How do you get a function from another file

from calc import addition as add, sub, num
    #alisiing is where you improt a funtion and gice it a new keyword

print(add(4,4))
print(sub(16,4))

#How do you get variables from another file?

from calc import num
#better to return from a function

#How do you have a function with multiple returns?

def get_user_info():
    name=input("what is your name\n")
    age=input("how old are you?\n")
    color = input("what is your favorite color\n")
    return name,age,color

name,age,color=get_user_info()

print(age)

#Why would you use multiple pages for a python project? 
    #is is easyer to merge on github
    #Modularity - breaking the programm into smaller more managable pieces. main should only include UI introdution to project.
    #functionaliy
    

