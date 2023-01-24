##### INSTALL NEW LIBRARIES
# pip install + "name of de module"
# You can create packages on pycharm directly

##### ERRORS LESSON
#Error management:
#Try -> try do the next thing to see if something happens
#Except -> if something happens, do not stop the code, excecute the next code
#Finaly -> whatever happens inside the codes or errors, execute the next code at the end

#def sum():
 #   print(10 + 10)
  #  print("Thank you for adding the two numbers")

#sum()

"""def sum_parameters():
    n1 = int(input("First number: "))
    n2 = int(input("Second number: "))
    print(n2+n1)
    print("Thank you for adding the two numbers")

try:
    sum_parameters()
    # Code that you wanna try
except ValueError:
    print("System Response: One of the variables was NOT a number")
    # Code to execute if there is an error
except TypeError:
    print("System Response: You are trying to add different type of variables")
finally:
    print("System Closed")
    # Code that is gonna be executed anyways
"""
"""
def ask_number():
    while True:
        try:
            number = int(input("Gimme a number: "))
        except:
            print("That was NOT a number")
        else:
            print(f"You entered the number = {number}")
            break
    print("Thanks")

ask_number()
"""
"""
def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFountError:
        "El archivo no fue encontrado"
    except:
        "Error desconocido"
    else:
        "Abriendo exitosamente"
    finally:
        "Finalizando ejecución"
"""

##### TEST YOUR CODE TO LOOK FOR MISTAKES
#pip install pylint
"""
number_one = 500
print(Number_one)
"""

##### HOW TO USE UNITTEST (INTEGRATED LIBRARY)
"""
def capital_letter(text):
    return text.upper()
"""

##### DECORATORS
"""
def capital_letter(text):
    print(text.upper())

def lower_case_letter(text):
    print(text.lower())
"""
"""
def get_function(function):
    return function

get_function(capital_letter("Testing the code"))
"""
"""
def change_letter(type):
    def capital_letter(text):
        print(text.upper())

    def lower_case_letter(text):
        print(text.lower())

    if type == "upper":
        return capital_letter
    elif type == "lower":
        return lower_case_letter

operation = change_letter("upper")
operation("Words have meaning")
"""
"""
def greeting_decorator(function):
    def another_function(word):
        print("Hi")
        function(word)
        print("Thanks")
    return another_function

@greeting_decorator
def upper_case_letter(text):
    print(text.upper())

@greeting_decorator
def lower_case_letter(text):
    print(text.lower())

upper_case_letter("demigod")
lower_case_letter("BEST ANIME IS MIRAI NIKKI")
"""
"""
def greeting_decorator(function):
    def another_function(word):
        print("Hi")
        function(word)
        print("Thanks")
    return another_function


def upper_case_letter(text):
    print(text.upper())


def lower_case_letter(text):
    print(text.lower())

decorated_upper = greeting_decorator(upper_case_letter)
upper_case_letter("runsho")
decorated_upper("runsho")
"""

##### GENERATORS
#Generates the variables as they are needed
#Saves space in memory
#instead of return uses yield
"""
def my_function():
    return 4

def my_generator():
    yield 4

print(my_function())
print(my_generator())

g = my_generator()
print(next(g))
"""
"""
def my_function():
    listx = []
    for i in range(1,5):
        listx.append(i * 10)
    return listx

def my_generator():
    for i in range(1,5):
        yield i * 10

print(my_function())
g = my_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
"""
"""
def my_generator():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = my_generator()
print(next(g))
print(next(g))
print("Hellow World")
print(next(g))
"""
"""
def my_generator():
    x = 0
    while x >= 0:
        x += 1
        yield x

g = my_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
"""
"""
def my_generator():
    x = 0
    while x >= 0:
        x += 1 * 7
        yield x

g = my_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
"""
"""
def losing_lifes():
    x = 3
    yield (f"You have {x} lifes left")
    x -= 1
    yield (f"You have {x} lifes left")
    x -= 1
    yield (f"You have {x} lifes left")
    x -= 1
    yield ("Game Over")

remaining_lifes = losing_lifes()
print(next(remaining_lifes))
print(next(remaining_lifes))
print(next(remaining_lifes))
print(next(remaining_lifes))
"""

##### STORE TURNS ASSIGNMENT PROJECT
# PHARMACY
# 3 SECTIONS OR AREAS : PHARMACY, COSMETICS AND GROCERIES
# TURNS = P-1, PH-23, G-5
# Turn is assigned depending on the section selected by the client
# Decorators for each turn text

#Classes, Variables and Main Functions
reset_turns_key = 1356288880002423917122199000
p_turn = 0
c_turn = 0
g_turn = 0

def continue_process():
    print("-" * 140)
    stop_security_key = "ANSIDNCOWMCOIEIMCIW7239E829389238JWINEIFNKEWNF823E0239E2398"
    continue_key = input("Do you wanna get a new turn?: ")
    while continue_key == stop_security_key:
        break

def turn_assignment_menu(reset_option, p_turn, c_turn, g_turn):
    next_option = 0
    while next_option != reset_option:
        try:
            print("-" * 140)
            next_option = int(
                input("""SKY PHARMACY SECTIONS
                [1] Pharmacy
                [2] Cosmetics
                [3] Groceries
                Choose the number of the section you wanna enter: """))
            print("-" * 140)
            if (next_option == 1):
                p_turn += 1
                print(f"Your turn is: P-{p_turn}, wait until you are called")
                continue_process()
            elif (next_option == 2):
                c_turn += 1
                print(f"Your turn is: C-{c_turn}, wait until you are called")
                continue_process()
            elif (next_option == 3):
                g_turn += 1
                print(f"Your turn is: G-{g_turn}, wait until you are called")
                continue_process()
            elif (next_option == reset_option):
                print(f"Today we assigned {p_turn + c_turn + g_turn} turns across all sections of Sky Pharmacy")
                break
            else:
                print("¡The option you chose was not a VALID number!")
                print("Please enter a number between 1, 2 or 3 to get your turn")
        except:
            print("-" * 140)
            print("¡The option you entered was NOT a number!")
            print("Please enter a number between 1, 2 or 3 to get your turn")
            next_option = 100

#Store Turns Process
turn_assignment_menu(reset_turns_key,p_turn,c_turn,g_turn)




