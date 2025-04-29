#personal protfolio Gavin Pierce GPCP2

import morse_code

import movie_recomender

import new_personal_library

import password_generator

import to_do_list

import updated_battle_simmulator

def main():
    while True:
      like_to_do = input("""
      
                  welcome to my personal portfolio. This project is to show some of the things that I have done this year that I am most proud of.
                  what would you like to do?
                  choose one of the following, use the number associated with the thing
                  1. see morse code
                  2. see movie recomender
                  3. see new personal library
                  4. see password generator
                  5. see to do list
                  6. see updated battle simmulator
                  7. exit
                         """)
      if like_to_do == "1":
          morse_code()

      elif like_to_do == "2":
          movie_recomender()

      elif like_to_do == "3":
          new_personal_library()

      elif like_to_do == "4":
          password_generator()

      elif like_to_do == "5":
          to_do_list()

      elif like_to_do == "6":
          updated_battle_simmulator()
      elif like_to_do == "7":
          print("thanks for reveiwing my personal protfolio")
      else:
          print("you need a valid chiose. ")


main()