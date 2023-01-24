###### HOW TO READ METHODS, FUNCTIONS AND DOCUMENTATION
#dictionary = {"key1":100,"key2":500}
#print(dictionary)
#popped_dic = dictionary.popitem()
#print(popped_dic)
#second_popped_dic = dictionary.popitem()
#print(second_popped_dic)
#print(dictionary)

#variable = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
#print(variable)
#changed_variable = variable.lstrip(",:%_#")
#print(changed_variable)

#fruits = ["mango", "banana", "cherry", "passion fruit", "watermelon"]
#print(fruits)
#fruits.insert(3,"orange")
#print(fruits)

#marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
#marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
#conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
#print(conjuntos_aislados)

##### FUNCTIONS LESSON
#def print_string(x):
 #   print("Your string is " + x)

#print_string("Ronaldinho")

#def greeting(x):
 #   print(f"Hi {x}")

#greeting("Leo Messi")
#greeting("Charles")

##### FUNCTIONS LESSON 2
#def multiply(x,y):
 #   return x*y

#print(multiply(5,25))

#word = "python"
#print(word)
#word = word[::-1]
#def inversion(x):
 #   return x[::-1].upper()

#print(inversion(word)

###### FUNCTIONS + LOOPS LESSON
#def check_3_digit(x):
 #   return x in range(100,1000)

#result = check_3_digit(678)
#print(result)

#result = check_3_digit(78)
#print(result)

#sum = 590 + 270
#result = check_3_digit(sum)
#print(result)

#def check_3_digit_on_list(listx):
 #   for n in listx:
  #      if n in range(100,1000):
   #         return True
    #    else:
     #       pass

#result = check_3_digit_on_list([55,99,6000])
#print(result)
#print(type(result))
#result = check_3_digit_on_list([555,99,6000])
#print(result)
#result = check_3_digit_on_list([55,99,600])
#print(result)

#def check_3_digit_on_list_II(listx):
 #   for n in listx:
  #      if n in range(100,1000):
   #         return True
    #    else:
     #       pass
    #return False

#result = check_3_digit_on_list_II([55,99,60])
#print(result)

#def check_3_digit_on_list_III(listx):
 #   listxx_3 = []
  #  for n in listx:
   #     if n in range(100,1000):
    #        listxx_3.append(n)
     #   else:
      #      pass
    #return listxx_3

#result = check_3_digit_on_list_III([555,99,600])
#print(result)

#def all_positive(listx):
 #   validation = 0
  #  for n in listx:
   #     if (n >= 0):
    #        validation = validation
     #   elif (n < 0):
      #      validation = validation + 1
    #if (validation == 0):
     #   return True
    ##   return False

#n_list = [50,4,6,0.5,-2]
#print(n_list)
#print(all_positive(n_list))
#n_list = [50,4,6,0.5,0]
#print(n_list)
#print(all_positive(n_list))

#def sum_less_than_x(listx,x):
 #   sum = 0
  #  for i in listx:
   #     if i in range (1,x):
    #        sum = sum + i
     #   else:
      #      pass
    #return sum

#n_list = [55,2500,45000,300,25,50]
#print(n_list)
#print(sum_less_than_x(n_list,1000))

#def sum_in_range_xy(listx,lower,upper):
 #   sum = 0
  #  for i in listx:
   #     if i in range (lower,upper):
    #        sum = sum + i
     #   else:
      #      pass
    #return sum

#n_list = [55,2500,45000,300,25,50]
#print(n_list)
#print(sum_in_range_xy(n_list,500,100000))

#def count_even_numbers(listx):
 #   aggregated_count = 0
  #  for n in listx:
   #     if (n%2 == 0):
    #        aggregated_count = aggregated_count + 1
     #   else:
      #      pass
    #return aggregated_count

#n_list = list(range(0,101))
#print(n_list)
#print(count_even_numbers(n_list))

#### FUNCTIONS + LOOPS LESSON 2
#coffee_prices = [("Latte",1.5),("Americano",1.2),("Moka",4)]
#for n in coffee_prices:
 #   print(n)

#for n,price in coffee_prices:
 #   print(n)

#for n,price in coffee_prices:
 #   print(price*4)

#def most_expensive_coffee(listx):
 #   coffe = ""
  #  price = 0
   # for c,p in listx:
    #    if p > price:
     #       price = p
      #      coffe = c
       # else:
        #    pass
    #return (coffe,price)

#coffee,price = most_expensive_coffee(coffee_prices)
#print(f"The mos expensive coffee is {coffee} at a price of ${price}")

##### MINIGAME WITH MULTIPLE FUNCTIONS
#from random import *
# Initial List
#picks = ["-","--","---","----"]
# Shuffle the List values
#def shuffle_x(listx):
 #   shuffle(listx)
  #  return listx
# Ask for the attempts
#def try_your_luck():
 #   attempt = ""
  #  while attempt not in ["1","2","3","4"]:
   #     attempt = input("Choose a number between 1 and 4: ")
    #return int(attempt)
# Check Attempt
#def check_attempt(listx,attempt):
 #   if listx[attempt - 1] == "-":
  #      print("¡You gotta wash the dishes!")
   # else:
    #    print("¡How lucky, you are free to go!")
    #print(f"Your pick was {listx[attempt-1]}")

#print("LUCKY PICK")
##print(picks)
#print("¡Choose a pick to avoid washing the dishes today!")
#print("The picks showed were shuffled")
#shuffled_picks = shuffle_x(picks)
#selected_pick = try_your_luck()
#check_attempt(shuffled_picks,selected_pick)

#from random import *
#def roll_dice(times):
 #   throws_vector = []
  #  i = 1
   # sum_throws = 0
    #while i <= times:
     #   x = randint(1,6)
      #  sum_throws = sum_throws + x
       # throws_vector.append(x)
        #i += 1
    #print(f"Roll the dice: {throws_vector}")
    #if (sum_throws <= (times*6)*0.5):
     #   print(f"¡Too bad! the sum of your dice rolls is {sum_throws}")
    #elif (sum_throws <= (times*6)*0.8):
     #   print(f"¡You got a decent result! the sum of your dice rolls is {sum_throws}")
    #elif (sum_throws > (times*6)*0.8):
     #   print(f"¡You got good Luck! the sum of your dice rolls is {sum_throws}")

#print(randint(1,6))
#print(roll_dice(20))
#n_list=[1,2,6,8,4,6,7,15,20,19,22,15,22]
#print(n_list)
#print(sorted(n_list))
#print(max(n_list))
#n_list.remove(max(n_list))
#print(n_list)
#x = list(set(n_list))
#print(x)
#def list_reduction(listx):
 #   sorted(listx)
  #  final_list = list(set(listx))
   # final_list.remove(max(final_list))
    #return final_list

#n_list = list_reduction(n_list)
#print(n_list)

#def average(final_list):
 #   list_sum = 0
  #  for n in final_list:
   #     list_sum = list_sum + n
    #avg_list = round((list_sum / len(final_list)),2)
    #return avg_list

#n_list = average(n_list)
#print(n_list)
#n_list =[1,2,3,4,5,6,7,8,9,10]
#print(n_list)

#from random import *
#def throw_coin():
 #   throw = choice(["Heads","Tails"])
  #  return throw

#def try_your_luck(throw,listx):
 #   if throw == "Heads":
  #      listx.clear()
   #     print(f"The list will be destroyed: {listx}")
    #elif throw == "Tails":
     #   print(f"The list of numbers will be preserved: {listx}")

#t = throw_coin()
#print(t)
#try_your_luck(t,n_list)

##### UNDIFINED ARGUMENTS LESSON
# *ARGS = ARGUMENTS
# *KWARGS = KEY WORD ARGUMENTS

#def sum(a,b):
 #   return a + b

#print(sum(5,6))

#def sum_I(*args):
 #   total_sum = 0
  #  for arg in args:
   #     total_sum += arg
    #return total_sum

#print(sum_I(5,6,16,100))

#def sum_II(*airplanes):
 #   return sum(*airplanes)

#print(sum_II(1001,1001))

#def sum_of_squares(*args):
 #   total_sum = 0
  #  for arg in args:
   #     total_sum = total_sum + (arg**2)
    #return total_sum
#print(sum_of_squares(1,2,3))

#def sum_of_absolute_value(*args):
 #   total_sum = 0
  #  for arg in args:
   #     total_sum = total_sum + ((arg**2)**0.5)
    #return total_sum
#print(sum_of_squares(1,-2,3))

#def names_plus_sum_of_numbers(*args):
 #   total_sum = 0
  #  name = ""
   # for arg in args:
    #    if (type(arg) == str):
     #       name = arg
      #  elif (type(arg) == int):
       #     total_sum += arg
    #print(f"{name}, the sum of your numbers is {total_sum}")

#names_plus_sum_of_numbers(4,5,6,7,8,"Daniel")

##### KEY WORD ARGUMENTS LESSON
#**kwargs
#def sum(**kwargs):
 #   print(type(kwargs))

#sum(x=3,y=5,z=2)

#def sum_I(**kwargs):
 #   for key,value in kwargs.items():
  #      print(f"The value of the key {key} = {value}")

#sum_I(x=3,y=5,z=2)

#def sum_II(**kwargs):
 #   total_sum = 0
  #  for key,value in kwargs.items():
   #     print(f"The value of the key {key} = {value}")
    #    total_sum += value
    #return total_sum

#print(sum_II(x=3,y=5,z=2))

#def new_sum (x,y,*args,**kwargs):
 #   print(f"The first numeric value is {x}")
  #  print(f"The second numeric value is {y}")

   # for arg in args:
    #    print(f"argument = {arg}")

    #for key,value in kwargs.items():
     #   print(f"{key} = {value} ")

#new_sum(1,2,6,7,8,9,n=100,v=200,z=300)
#args = [100,200,300,400]
#kwargs = {"n":"One","v":"Two","w":"Three"}
#new_sum(15,50,*args,**kwargs)

#def list_of_attributes(**kwargs):
 #   return list(kwargs.keys())


#k = {"n":"One","v":"Two","w":"Three"}
#print(list(k.keys()))
#print(list_of_attributes(**k))

#def describe_person(n,**kwargs):
    #name = n
    #print(f"The characteristics of {name} are:")
    #for keys,values in kwargs.items():
     #   print(f"{keys} = {values}")

#describe_person("Maria",Eyes_color="Blue", Hair_color="Red" )

##### FIVE PROBLEMS
### EXCERCISE 1
#def return_distinct_numbers(x,y,z):
 #   if (x+y+z > 15):
  #      return max(x,y,z)
   # elif (x+y+z < 10):
    #    return min(x,y,z)
    #elif (x+y+x >= 10 and x+y+x <= 15):
     #   return x+y+z-max(x,y,z)-min(x,y,z)
#print(return_distinct_numbers(1,2,3))
#print(return_distinct_numbers(15,20,30))
#print(return_distinct_numbers(5,4,3))

###EXCERCISE 2
#def sorted_letters_from_word(word):
 #   return sorted(set(list(word)))

#print(sorted_letters_from_word("Paradise"))

###EXCERCISE 3
#def consecutive_zeros(*args):
 #   last_number = -1
  #  for arg in args:
   #     if (last_number == arg and last_number == 0):
    #        return True
     #   else:
      #      last_number = arg
    #return False
#print(consecutive_zeros(0,1,2,3,4,5))
#print(consecutive_zeros(0,1,0,0,3,4,5))

###EXCERCISE 4
#def count_prime_numbers(min_range,max_range):
 #   prime_list = list(range(min_range,max_range+1))
  #  count_list = []
   # for n in prime_list:
    #    i = 1
     #   divisors_list = []
      #  while i <= n:
       #     divisors_list.append(n%i)
        #    i = i + 1
        #if (divisors_list.count(0)==2):
         #   count_list.append(n)

    #print(f"{divisors_list}")
    #print(f"{prime_list}")
    #print(f"The prime numbers are: {count_list}")
    #print(f"The amount of prime numbers between 0 and {max_range} is {len(count_list)}")

#count_prime_numbers(0,150)

#def count_prime_numbers(num):
 #   prime_list = [2]
  #  i = 3
   # if num < 2:
    #    return 0
    #while i <= num:
     #   for n in range(3,i,2):
      #      if i % n == 0:
       #         i += 2
        #        break
        #else:
         #   prime_list.append(i)
          #  i += 2

    #print(prime_list)
    #return len(prime_list)

#print(count_prime_numbers(100))

##### HANGMAN GAME PROJECT
# Creates a secret word
# Each turn the player chooses a letter
# Positive outcome: shows the positions of the letter
# Negative outcome: shows the previous letters and the hangman with more parts + losses a life
# Inputs and Variables
from random import *
list_of_hangman_words = ["DISDAIN","UTTERLY","DOLPHIN","EMIR","TAILORED"]
secret_word = choice(list_of_hangman_words)
secret_word_list = list(secret_word)

incorrect_letters = []
player_lifes = 8
turn = 1

hangman_list = []
for n in secret_word_list:
    hangman_list.append("_")

valid_characters_list = []
for i in list(range(ord("A"),ord("Z")+1)):
    valid_characters_list.append(chr(i))


print("LET'S PLAY THE HANGMAN GAME")
print(f"The word has {len(list(secret_word))} letters")
print(hangman_list)
print(f"You got {player_lifes} lifes, ¡Good Luck!")

print("----------------------------------------------------------------------")

#Start of the Game: Receives Letters as input
def verify_letter(letter):
    """
    :param letter:
    :return: Changes the character in an empty list for a letter as many times as the letter appears
    """
    i = 0
    while i <= len(secret_word)-1:
        if letter == secret_word_list[i]:
            hangman_list[i] = secret_word_list[i]
        i += 1
    return hangman_list

while turn <= player_lifes:
    guess_letter = input("Enter a letter you think is part of the word: ").upper()
    if (guess_letter not in valid_characters_list):
        print("Please enter a valid character (A-Z)")
    else:
        if (guess_letter in secret_word):
            hangman_list = verify_letter(guess_letter)
            print(f"{hangman_list}")
            print("¡The letter was part of the word!")

            if (hangman_list == secret_word_list):
                print("""
                **   0   **
                   --|--
                    / \ 
                """)
                print(f"¡Congratulations, You Saved the Hangman!")
                break
            print("----------------------------------------------------------------------")
        elif (guess_letter not in secret_word):
            print(f"{hangman_list}")
            print("¡The letter is NOT in the word!")
            incorrect_letters.append(guess_letter)
            print(f"Incorrect Letters: {incorrect_letters}")
            print(f"You got {player_lifes - turn} life(s) left")
            print("----------------------------------------------------------------------")
            turn += 1

if (hangman_list != secret_word_list):
    print("""
    |-----|
    |     0
    |   --|--
    |    / \ 
    |________
    """)
    print(f"¡The Hangman Died!, the word was {secret_word}")

















