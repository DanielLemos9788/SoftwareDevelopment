###### INPUT AND OUTPUT LESSON
# Read, Write, Edit Files
#my_file = open("trial_1.txt")
#print(my_file)
#print(my_file.read())
#first_line = my_file.readline()
#print(first_line)

#first_line = my_file.readline()
#print(first_line.rstrip())

#first_line = my_file.readline()
#print(first_line.upper())

#for l in my_file:
 #   print("Here it says:" + l)

#all_lines = my_file.readlines()
#print(all_lines)
#READLINES TRANFORM THE TEXT INTO A LIST
#all_lines = all_lines.pop()
#print(all_lines)

#my_file.close()

##### CREATE, WRITE AND MODIFY TEXT
#a = write mode at the end
#w = write mode clearing everything

#file = open("trial_1.txt","r")
#file.write("I'm the new text") --> NOT WRITABLE
#file.close()

#file_I = open("trial_1.txt","w")
#file_I.write("I'm the new text")
#file_I.close()

#file_I = open("trial_1.txt","w")
#file_I.write("Hellow ")
#file_I.write("World ")
#file_I.close()

#file_I = open("trial_1.txt","w")
#file_I.write("""HELLOW
#WORLD
#HERE
#I'AM""")
#file_I.close()

#file_I = open("trial_1.txt","w")
#file_I.writelines(["Hellow","World","Here","I'm"])
#file_I.close()

#file_I = open("trial_1.txt","w")
#word_list = ["Hellow","World","Here","I'm"]

#for n in word_list:
 #   file_I.write(n + "\n")

#file_I.close()

#file_I = open("trial_1.txt","a")
#file_I.write("Welcome to Elden Ring")
#file_I.close()

###### PATH & OS METHODS
import os
#get current working directory
#pathway = os.getcwd()
#print(pathway)

#change directory
#pathway = os.chdir("C:\\Users\\DanielLemos\\OneDrive - Mo Tecnologias\\Escritorio\\Alternative Path")
#print(pathway)

#file = open("Second_Trial.txt")
#print(file.read())

#pathway_X = os.makedirs("C:\\Users\\DanielLemos\\OneDrive - Mo Tecnologias\\Escritorio\\Alternative Path\\Another Alternative")

#new_path = "C:\\Users\\DanielLemos\\PycharmProjects\\pythonProject\\Trial_1.txt"
#element = os.path.basename(new_path)
#e = os.path.dirname(new_path)
#print(element)
#print(e)
#ee = os.path.split(new_path)
#print(ee)

#os.rmdir("C:\\Users\\DanielLemos\\OneDrive - Mo Tecnologias\\Escritorio\\Alternative Path\\Another Alternative")
#another_file = open("C:\\Users\\DanielLemos\\OneDrive - Mo Tecnologias\\Escritorio\\Alternative Path\\Second_Trial.txt")
#print(another_file.read())

#from pathlib import Path
#folder = Path("C:/Users/DanielLemos/OneDrive - Mo Tecnologias/Escritorio/Alternative Path")
#file = folder / "Second_Trial.txt"
#my_file = open(file)
#print(my_file.read())

##### PATHLIB LESSON
#from pathlib import Path, PureWindowsPath
#folder = Path("C:/Users/DanielLemos/PycharmProjects/pythonProject/Trial_1.txt")
#print(folder.read_text())
#print(folder.name)
#print(folder.suffix)
#print(folder.stem)

#if not folder.exists():
 #   print("This file does not exist")
#else:
 #   print("Good, the file exists")


#windows_path = PureWindowsPath(folder)
#print(windows_path)

###### PATH SECOND LESSON
from pathlib import Path
#base = Path.home()
#guide = Path("Barcelona", "Sacred_Family.txt")
#print(base)
#print(guide)
#guide_x = Path(base, guide)
#print(guide_x)
#guide_xx = Path(base, "Europe", "Spain", guide)
#print(guide_xx)
#second_guide = guide_xx.with_name("La_Pedrera.txtx")
#print(second_guide)
#print(guide_xx.parent)
#print(guide_xx.parent.parent.parent)

#guide = Path("C:/Users/DanielLemos/OneDrive - Mo Tecnologias/Escritorio/Europe")
#guide_x = Path(Path.home(),"Europe")
#print(guide_x)
### Brings all the txt files visibles in the folder
#for txt in Path(guide).glob("*.txt"):
 #   print(txt)

### Brings all the txt inside the folder even if they are inside other folders inside the main folder
#for txt in Path(guide_x).glob("**/*.txt"):
 #   print(txt)

#guide = Path("Europe","Spain","Barcelona","Sagrada_Familia.txt")
#print(guide)
#in_europe = guide.relative_to(Path("Europe"))
#in_spain = guide.relative_to(Path("Europe","Spain"))
#print(in_europe)
#print(in_spain)

#guide = Path("C:/Users/DanielLemos/OneDrive - Mo Tecnologias/Escritorio/Europe")
### Brings all the txt files visibles in the folder
#for txt in Path(guide).glob("*.txt"):
 #   print(txt.relative_to(Path("C:\\","Users","DanielLemos","OneDrive - Mo Tecnologias","Escritorio")))

#from pathlib import Path
#ruta = Path(Path.home(),"Curso Python","Día 6","practicas_path.py")

##### CLEAN THE CONSOLE

#name = input("Enter your Name: ")
#age = input("Enter your age: ")
#print(f"Your name is {name} and your age is {age}")

#from os import system
#name = input("Enter your Name: ")
#age = input("Enter your age: ")
### FOR OTHER OPERATIN SYSTEMS LIKE LINUX OR MAC USE CLEAR ON THE SYSTEM COMMAND
#system("cls")
#def clear(lines=25): print('\n' * lines)
#clear()
#print(f"Your name is {name} and your age is {age}")

#def abrir_leer(file):
 #   file_to_read = open(file)
  #  return file_to_read.read()

#def sobrescribir(file):
 #   file_to_change = open(file,"w")
  #  return file_to_change.write("contenido eliminado")

#def registro_error(file):
 #   file_to_change = open(file,"a")
  #  return file_to_change.write("se ha registrado un error de ejecución")


#from pathlib import Path
#ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
#print(ruta)
#carpeta = ruta.parents[3]
#print(carpeta)


##### RECIPE BOOK PROJECT
# Folder directory with cookbook and options: Done on Local
# Welcome to user + de directory of the book + total of recipes
# The user will have 6 options:
# 1. Read Recipe
# 2. Create New Recipe
# 3. Create New Category
# 4. Delete Recipe
# 5. Delete Category
# 6. Close Program
# De loop does not stop until the user closes the program
### The folder of the book is in the same directory as the python file
# Inputs and Variables
from pathlib import *
import os
import shutil
recipe_folder = Path(os.getcwd(),"Recipe Book")
stop_option = 6

### COUNTS ALL THE RECIPES ON THE BOOK/FOLDER
def count_recipes(recipe_folder):
    all_recipes_list = []
    for txt in Path(recipe_folder).glob("**/*.txt"):
        all_recipes_list.append(txt.stem)
    print(all_recipes_list)
    return len(all_recipes_list)

### GETS CATEGORY
def get_category():
    list_present_categories = next(os.walk(recipe_folder))[1]
    print("The current category options are:")
    print(list_present_categories)
    category = input("Choose one category: ")
    while category not in list_present_categories:
        print("¡Write a valid category, exactly as shown above!")
        category = input("Choose one category: ")
    category_path = Path(recipe_folder, category)
    return category_path,category

### CREATES A NEW CATEGORY/FOLDER
def create_new_category():
    list_present_categories = next(os.walk(recipe_folder))[1]
    print("The current categories are:")
    print(list_present_categories)
    category_name = input("Choose the new category name: ")
    while category_name in list_present_categories:
        print("¡Please enter a NEW category!")
        category_name = input("Choose the new category name: ")

    new_category_path = Path(recipe_folder, category_name)
    new_category = os.mkdir(new_category_path)
    return new_category

### DELETES A CATEGORY CHOSEN BY THE USER
def delete_category():
    list_present_categories = next(os.walk(recipe_folder))[1]
    print("The current categories are:")
    print(list_present_categories)
    category_name = input("Choose the category you wanna delete: ")
    while category_name not in list_present_categories:
        print("¡Please enter a VALID category!")
        category_name = input("Choose the category you wanna delete: ")

    delete_category_path = Path(recipe_folder, category_name)
    shutil.rmtree(delete_category_path,ignore_errors=True)
    print(f"The category {category_name} was deleted from the book")

### GETS RECIPE OR TXT FILES
def get_recipe(category_path,category):
    list_recipes = []
    for txt in Path(category_path).glob("*.txt"):
        list_recipes.append(txt.stem)
    print(f"The current recipe options in {category} are:")
    print(list_recipes)
    recipe = input("Choose one recipe to open: ")
    while recipe not in list_recipes:
        print("¡Write a valid recipe, exactly as shown above!")
        recipe = input("Choose one recipe to open: ")
    recipe_path = Path(category_path, recipe + ".txt")
    return recipe_path,recipe

### READS THE RECIPE FILE
def read_recipe(recipe_path,recipe):
    to_read = open(recipe_path,"r")
    print(f"The recipe of {recipe} is:")
    print(to_read.read())
    to_read.close()

### CREATES A NEW RECIPE FILE
def create_new_recipe():
    category_path,category = get_category()
    list_recipes = []
    for txt in Path(category_path).glob("*.txt"):
        list_recipes.append(txt.stem)
    print(f"The current recipes in {category} are:")
    print(list_recipes)
    recipe_name = input("Give the new recipe a name: ")
    while recipe_name in list_recipes:
        print("¡Please enter a NEW recipe!")
        recipe_name = input("Give the new recipe a name: ")

    new_recipe_path = Path(category_path,recipe_name+".txt")
    new_recipe = open(new_recipe_path,"w")
    content_new_recipe = input("Please write the content of the recipe: \n")
    new_recipe.write(content_new_recipe)
    new_recipe.close()

### DELETES A RECIPE FILE CHOOSEN BY THE USER
def delete_recipe():
    category_path,category = get_category()
    list_recipes = []
    for txt in Path(category_path).glob("*.txt"):
        list_recipes.append(txt.stem)
    print(f"The current recipes in {category} are:")
    print(list_recipes)
    recipe_name = input("Choose the recipe you wanna delete: ")
    while recipe_name not in list_recipes:
        print("¡Please enter a VALID recipe!")
        recipe_name = input("Choose the recipe you wanna delete: ")

    delete_recipe_path = Path(category_path,recipe_name+".txt")
    os.remove(delete_recipe_path)
    print(f"The recipe {recipe_name} was deleted from the book")

### CLEARS THE PAGE BY PRINTING X NUMBER OF EMPTY SPACES
def clear_page(lines=100):
    print("\n" * lines)

### TAKES THE USER BACK TO THE MAIN MENU AT ANY POINT
def go_back_main_menu():
    pass
    

### Main Menu Complete Process
print("WELCOME TO THE RECIPE BOOK PROJECT")
print(f"The Recipe Book is located at: {recipe_folder}")
print(f"At the moment the book has {count_recipes(recipe_folder)} recipes")
print("----------------------------------------------------------------------")
next_option = int(input("""MAIN MENU
[1] Read a Recipe
[2] Create Category
[3] Create Recipe
[4] Delete Category
[5] Delete Recipe
[6] Exit

Choose the number of the process you wanna do next: """))
#clear_page()
print("----------------------------------------------------------------------")

while stop_option != next_option:
    if(next_option == 1):
        category_path,category = get_category()
        recipe_path,recipe = get_recipe(category_path,category)
        print("\n")
        read_recipe(recipe_path,recipe)
    elif(next_option == 2):
        create_new_category()
    elif(next_option == 3):
        create_new_recipe()
    elif(next_option == 4):
        delete_category()
    elif(next_option == 5):
        delete_recipe()
    #clear_page()
    print("----------------------------------------------------------------------")
    next_option = int(input("""MAIN MENU
    [1] Read a Recipe
    [2] Create Category
    [3] Create Recipe
    [4] Delete Category
    [5] Delete Recipe
    [6] Exit

    Choose the number of the process you wanna do next: """))
    print("----------------------------------------------------------------------")

print("You exit the Recipe Book")

