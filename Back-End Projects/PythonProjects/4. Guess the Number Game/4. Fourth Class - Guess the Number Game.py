##### LOGIC OPERATORS LESSON
# = assigns a value to a variable
# == checks if to variables or elements are the same
# != different to
#my_bool = 10==25
#print(my_bool)
#my_bool = 5+5==18-8
#print(my_bool)
#my_bool = "blanco"=="Blanco"
#print(my_bool)
#my_bool = "blanco"=="Blanco".lower()
#print(my_bool)
#my_bool = "100" == 100
#print(my_bool)
#my_bool = 100.0 == 100
#print(my_bool)
#my_bool = 100!=100
#print(my_bool)
#my_bool = 100>101
#print(my_bool)
#my_bool = 100<101
#print(my_bool)

##### CONNECTORS + LOGIC OPERATORS
# AND &&
# OR ||
# NOT OR DIFFERENT FROM
#my_bool = 4 < 5 < 6
#print(my_bool)
#my_bool = 4 < 5 and 5 > 6
#print(my_bool)
#my_bool = 4 < 5 and 5 == 2+3
#print(my_bool)
#my_bool = (4 > 5) and (5 == 2+3)
#print(my_bool)
#my_bool = (55==55) and ("dog"=="dog")
#print(my_bool)
#my_bool = (10==10) or (3==3)
#print(my_bool)
#my_bool = (1==10) or (3==3)
#print(my_bool)
#my_bool = (1==10) or (3==30)
#print(my_bool)
#text = "this is a short phrase"
#my_bool = ("phrase" in text) and ("not" in text)
#print(my_bool)
#my_bool = ("phrase" in text) or ("not" in text)
#print(my_bool)
#my_bool = not ("a"=="a")
#print(my_bool)
#my_bool = not ("a"!="a")
#print(my_bool)

##### FLOW CONTROL: CONDITIONAL STATEMENTS (IF, WHERE, CASE)
#if 10 > 9:
 #   print("Successful Result")
#else:
 #   print("False Result")

#x = True
#if x != True:
 #   print("Successful Result")
#else:
 #   print("The variable is True in itself")

#if 5==2:
 #   print("Correct Result")
#else:
 #   print("Incorrect Result")

#pet = "dog"
#if pet == "cat":
 #   print("You pet is a cat")
#else:
 #   print("I don't know what pet you have")

#if (pet == "cat"):
 #   print("You pet is a cat")
#elif (pet == "dog"):
 #   print("Your pet is a dog")
#else:
 #   print("I don't know what pet you have")

#pet = "fish"
#if (pet == "cat"):
 #   print("You pet is a cat")
#elif (pet == "dog"):
 #   print("Your pet is a dog")
#elif (pet == "fish"):
 #   print("Your pet is a fish")
#else:
 #   print("I don't know what pet you have")

#age = 16
#if (age<18):
 #   print("You are a minor")
#else:
 #   print("You are an adult")

#grade = 7
#if age<18:
 #   print("You are a minor")
  #  if grade >= 7:
   #     print("Approved")
    #else:
     #   print("Failed Subject")
#else:
 #   print("Your are an adult")

##### LOOPS LESSON
#name_list = ["Juan", "Ana", "Daniel", "Manuela", "Jack"]
#print(name_list)
#for i in name_list:
 #   print(f"Hi "+ i)

#for name in name_list:
 #   print(name + " do you wanna get a beer?")

#letter_list = ["a","b","c","d"]
#for letter in letter_list:
 #   letter_number = letter_list.index(letter) + 1
  #  print(f"The letter number {letter_number} on the list is: "+ letter)

#sport_list = ["Football","Rugby","Tennis","Basketball","MMA"]
#for sport in sport_list:
 #   if (sport.startswith("R")):
  #      print(f"{sport} starts with an R")
   # else:
    #    print(f"{sport} does not start with an R")

#numbers = [1,2,3,4,5]
#my_value = 0

#for number in numbers:
 #   my_value = my_value + number
  #  print(my_value)

#word = "python"
#for i in word:
 #   print(i.upper())

#for i in [[1,2],[3,4],[5,6]]:
 #   print(i)

#for a,b in [[1,2],[3,4],[5,6]]:
 #   print(a)
  #  print(b)

#dictionary = {"key_1":"a","key_2":"b","key_3":"c"}
#for item in dictionary:
 #   print(item)

#dictionary = {"key_1":"a","key_2":"b","key_3":"c"}
#for item in dictionary.items():
 #   print(item)

#dictionary = {"key_1":"a","key_2":"b","key_3":"c"}
#for item in dictionary.values():
 #   print(item)

#dictionary = {"key_1":"a","key_2":"b","key_3":"c"}
#for a,b in dictionary.items():
 #   print(a +" == " + b)

##### WHILE LOOPS LESSON
#The loops repeats while something is happening
#cash = 5
#while cash > 0:
 #   print(f"I have ${cash} in cash")
  #  cash = cash - 1
#else:
 #   print("I do not have more money")

#cash = 3
#while cash > 0:
 #   print(f"I have ${cash} in cash")
  #  cash -= 1
#else:
 #   print("I do not have more money")

#answer = "yes"

#while answer == "yes":
 #   answer = input("Do you wanna continue? (Yes or No): ").lower()
  #  print("You are a demigod")
#else:
 #   print("The reinforcement stopped by your command")

#PASS Command

#answer = " yes"
#while answer == "yes":
 #   print("Hellow Gorgeous")
  #  pass

#BREAK Command

#name = input("Gimme your name: ").lower()
#for letter in name:
 #   if letter == "n":
  #      break
   # print(letter)

#CONTINUE Command

#name = input("Gimme your name: ").lower()
#for letter in name:
 #   if letter == "n":
  #      continue
   # print(letter)

#number = 10
#while number >= 0:
 #   print(number)
  #  number = number - 1

#number = 50
#while (number >= 0):
 #   if (number % 5 == 0):
  #      print(number)
   # number = number - 1

##### RANGE LESSON
#list = [1,2,3,4]
#for i in list:
 #   print(i)
#Lists are no longer needed
#for i in range(5):
 #   print(i)

#for i in range(1,21):
 #   print(i)

#for i in range(20,31,2):
 #   print(i)

#list = list(range(1,101))
#print(list)
#squares = 0
#for i in range(1,16):
 #   squares = squares + i**2
  #  print(squares)

##### ENUMERATE FUNCTION LESSON
#listX = ["a", "b", "c", "d"]
#ind = 0

#for item in listX:
 #   print(ind,item)
  #  ind += 1


#listX = ["a", "b", "c", "d"]

#for item in enumerate(listX):
 #   print(item)
#Generates multiple tuples

#listX = ["a", "b", "c", "d"]

#for i,item in enumerate(listX):
 #   print(i,item)

#for i,item in enumerate(range(50,56)):
 #   print(i,item)

#listx = ["a", "b", "c", "d"]
#new_tuples = list(enumerate(listx))
#print(new_tuples)
#print(new_tuples[1])
#print(new_tuples[1][1])

#p = "python"
#index_list = list(enumerate(p))
#print(index_list)

##### FUNCTION ZIP LESSON
# Zip creates tuples by joining two lists

#names = ["dan","manu","lau","ana"]
#ages = [24,30,41,63]
#new_tuple = zip(names,ages)
#print(new_tuple)

#names = ["Dan","Manu","Lau","Ana"]
#ages = [24,30,41,63]
#new_tuple = list(zip(names,ages))
#print(new_tuple)

#cities = ["Lima","Madrid","Mexico City","Buenos Aires"]
#combined_tuple = list(zip(names,ages,cities))
#for names,ages,cities in combined_tuple:
 #   print(f"{names} is {ages} years old, and lives in {cities}")

#capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
#paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]


#capitales_y_paises = list(zip(capitales,paises))
#for capitales, paises in capitales_y_paises:
 #   print(f"La capital de {paises} es {capitales}")

#one = ["uno","um", "one"]
#two = ["dos","dois","two"]
#three = ["tres","três","three"]
#four = ["cuatro","quatro","four"]
#five = ["cinco","cinco","five"]
#numeros = list(zip(one,two,three,four,five))
#print(numeros)

#spanish = ["uno","dos","tres","cuatro","cinco"]
#portugues = ["um","dois","três","quatro","cinco"]
#english = ["one","two","three","four","five"]
#numeros = list(zip(spanish,portugues,english))
#print(numeros)

##### MIN AND MAX LESSON
#minimum_amount = min(2,4,-89,-8990,0.09)
#print(minimum_amount)
#maximum_amount = max(1,2,5,796,303930,0.3339)
#print(maximum_amount)
#list_numbers = [58,96,72,64,22]
#print(f"The minimum number on the list is {min(list_numbers)} and the maximum number on the list is {max(list_numbers)}")

#names = ["Juan","Pablo","Alicia","Carlos"]
#print(min(names))
#name = "Carlos"
#print(min(name))
#print(min(name.lower()))

#dictionary = {"C1":45,"C2":11}
#print(min(dictionary))
#print(min(dictionary.values()))
#print(min(dictionary.items()))
#print(min(dictionary.keys()))

##### RANDOM LESSON
#from random import randint
#random_integer = randint(1,50)
#print(random_integer)

#from random import *
#random_number = uniform(1,5)
#print(random_number)
#random_number = round(uniform(1,5),2)
#print(random_number)

#random_number = random()
#print(random_number)

#colors = ["Blue","Red","Green","Black","Yellow","Violet"]
#random_color = choice(colors)
#print(random_color)

#numbers = list(range(1,56))
#print(numbers)
#random_card = shuffle(numbers)
#print(numbers)

##### LIST COMPREHENSION LESSON

#word = "Python"
#list_word = []
#print(list_word)
#for letter in word:
#    list_word.append(letter)
#print(list_word)

#list_word = [letter for letter in word]
#print(list_word)

#list_word = [i for i in "Messi is the best football player"]
#print(list_word)

#number_list = [i for i in range(0,21,2)]
#print(number_list)

#number_list = [i/2 for i in range(0,21,2)]
#print(number_list)

#number_list = [i**2 for i in range(0,21,2)]
#print(number_list)

#number_list = [i for i in range(0,21,2) if i*2 > 10]
#print(number_list)

#number_list = [i for i in range(0,21,2) if i%2 == 0]
#print(number_list)

#number_list = [i for i in range(0,21,2) if i%2 != 0]
#print(number_list)

#number_list = [i if i*2 > 10 else "Number Not Accepted" for i in range(0,21,2)]
#print(number_list)

#feet_measures = [10,20,30,40,50]
#meter_measures = [i*0.3048 for i in feet_measures]
#print(meter_measures)

##### MATCH LESSON
#series = "N-02"

#"""if series == "N-01":
 #   print("Samsung")
#elif series == "N-02":
 #   print("Nokia")
#elif series == "N-03":
 #   print("Black-Berry")
#else:
 #   print("Product does not exist in this store")"""

#match series:
 #   case "N-01":
  #      print("Samsung")
   # case "N-02":
    #    print("Nokia")
    #case "N-03":
     #   print("Black-Berry")

#client = {"name":"Frank","age":45,"job":"Developer"}
#movie = {"tittle":"Matrix","datasheet":{"main_character":"Keanu Reeves","director":"Lana & Lilly Wachowsky"}}
#elements = [client, movie, "book"]

#for i in elements:
 #   match i:
  #      case {"name": name,"age":age,"job":job}:
   #         print(f"{name} is one of our customers: age {age} and his/her job is {job}")
    #    case {"tittle":tittle,"datasheet":{"main_character":main,"director":director}}:
     #       print(f"{tittle} is a movie directed by {director} and its main character is {main}")
      #  case:
       #     print("The system does not support this format")

##### GUESS THE NUMBER GAME PROJECT
# Asks for the name of the player
# Guess a number between 1 - 100
# Got 8 tries to guess the number
# Each time the use makes a guess the game returns:
# 1. > 1 or <100 non valid number out of range
# 2. If the number choosen by the player is greater than the random number tell the player the guess is greater than the number
# 3. If the number choosen by the player is less than the random number tell the player the guess is less than the number
# 4. If the number is correct then tells the player that has won the game and how many attemps it took
print("GUESS THE NUMBER")
print("----------------------------------------------------------------------")
# Inputs and Variables
from random import *
print("CHOOSE YOUR NICKNAME AND DIFFICULTY")
nickname = input("Please enter your name or nickname: ")
difficulty_level = round(int(input("Choose the difficulty you wanna play (1'Super-Easy'- 10'Legendary'): ")))
secret_number = randint(1, 100*difficulty_level)
maximum_attempts = 8 - round((difficulty_level-5))
attempts = 1
print("----------------------------------------------------------------------")
print("NOW MAKE YOUR GUESSES, ¡GOOD LUCK!")
print(f"The secret number is a natural number between 1 and {100*difficulty_level}")
print(f"You have {maximum_attempts} attempts")
while attempts <= maximum_attempts:
    player_guess = round(int(input("¡Make a guess!, what is the secret number? ")))
    if (player_guess == secret_number):
        print(f"¡Congratulations {nickname}! the secret number was in fact {secret_number}")
        print(f"You completed the game in your attempt number {attempts}")
        print("----------------------------------------------------------------------")
        break
    elif (attempts == maximum_attempts):
        print(f"¡Sorry {nickname} you lost the game!, the secret number was {secret_number}")
    elif (player_guess < 1 or player_guess > (100*difficulty_level)):
        print(f"NOT A VALID NUMBER, remember the range is between 1 and {100*difficulty_level}")
    elif (player_guess < secret_number):
        print(f"Your guess is less than the secret number")
    elif (player_guess > secret_number):
        print(f"Your guess is greater than the secret number")
    attempts = attempts + 1
    print("----------------------------------------------------------------------")




