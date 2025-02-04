#What is a dictionary?
def what():
    print("""item with a description. detailed lists. lets you give spicific info about items. key and value key is item and value is the description. heres is and example you can also put a dictionary in a dictionary""")
    car = {
        "make": ["Ford","Chevy", "toyota" "Honda", "tesla", "BMW"],
        "modle": "escape xlt",
        "year": 2008,
        "color": "Red" 
    }

    print(car.get("make"))

    #uses key to find the thing
    print(car["modle"])

    students = {
        "first":{
            1: "Vincent",
            2: "Cecily",
            3: "Sawer",
            4: "alisha"
        },
        "sixth":{
            1: "nicole",
            2: "Luke",
            3: "gavin",
            4: "Jackson"
        }
    }
    print(students["sixth"][2])

    students.pop("first")
    print("students")
    print(car)
    car.popitem()
    print(car)

    print(car)

    car.update({"color": "pirk"})
    print(car)



#What are keys?
def keys():
    print("""
    rather then using an index like in a list you use the keys
    """)


#What are values?
def values():
    print("""

    the items in the list
    
    """)


#How do you write a dictionary?
def how():
    print("""
    here is an example

    car = {
        "make": ["Ford","Chevy", "toyota" "Honda", "tesla", "BMW"],
        "modle": "escape xlt",
        "year": 2008,
        "color": "Red" 
    }

    
    print(car["modle"])
    """)


#What data types can you have in a dictionary?
def data_types():
    print("""
    the dictionarys can have all the list values and also dictionarys
    """)


#How do you print 1 item from a dictionary?
def print_from():
    print("""
    here is an example

          car = {
        "make": ["Ford","Chevy", "toyota" "Honda", "tesla", "BMW"],
        "modle": "escape xlt",
        "year": 2008,
        "color": "Red" 
    }
    
     print(car.get("make"))
    
    """)


#Why would you use a dictionary in a program?
def why():
    print("""
    you would use a dictionary in a program to make the code call an items for a dictionary to make it so that it will have a value to search by and then also to print with
    """)


#What methods can be used with dictionaries?
def methods():
    print("""
    there are several dictionarys methoids such as list, tuples and sets
    """)

def main():
    while 8:
        like_to_do=input("""what would you like to learn?
        1. What is a dictionary?
        2. What are keys?
        3. What are values?
        4. How do you write a dictionary?
        5. What data types can you have in a dictionary?
        6. How do you print 1 item from a dictionary?
        7. Why would you use a dictionary in a program?
        8. What methods can be used with dictionaries?
        9. end
        
        
        """)
        if like_to_do == "1":
            what()
        elif like_to_do == "2":
            keys()
        elif like_to_do == "3":
            values
        elif like_to_do == "4":
            how
        elif like_to_do == "5":
            data_types
        elif like_to_do == "6":
            print_from
        elif like_to_do == "7":
            why
        elif like_to_do == "8":
            methods
        elif like_to_do == "8":
            print("thanks for learning bye.")
            break
        else:
            print("you need a valid variable")

main()