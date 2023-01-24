##### OBJECT CREATION
#Inheritance
#Polymorphism
#Encapsulation
#Abstraction
#Association
#Aggregation
#Composition

## Attributes > Class creation

##### OBJECT & CLASS CREATION LESSON
#class Bird:
 #   pass

#my_bird = Bird()
#another_bird = Bird()

#print(my_bird)
#print(type(my_bird))
#print(another_bird)

##### ATTRIBUTES LESSON
# You can have attributes that are connected to the class
# You can have attributes that are connected to the instance

#class Bird:

 #   def __init__(self,color):
  #      self.color = color

#my_bird = Bird("Black")
#print(my_bird)
#word = "Hi"
#print(my_bird.color)

#class SecondBird:

 #   def __init__(self,my_color):
  #      self.color = my_color

#my_bird = SecondBird("Blue")
#print(my_bird.color)

#class Book:
 #   def __init__(self, parameter):
  #      self.attribute = parameter

#my_book = Book("Crime and Punishment")
#print(my_book.attribute)

#class XBird:
 #   wings = True
  #  def __init__(self,color,species):
   #     self.color = color
    #    self.species = species


#my_bird = XBird("Yellow","Mockingbird")
#print(my_bird.species)
#print(f"My bird is {my_bird.color} {my_bird.species}")
#print(my_bird.wings)

#class House:
 #   def __init__(self,color,floors):
  #      self.color = color
   #     self.floors = int(floors)

#white_house = House("White",6)
#print(white_house)
#print(f"I got a {white_house.color} House with {white_house.floors} floors")


#class Cube:
 #   sides = 6
  #  def __init__(self,color):
   #     self.color = color

#red_cube = Cube("Red")
#print(f"I got a {red_cube.color} cube with {red_cube.sides} sides")

#class Character:
 #   real = False
  #  def __init__(self,species, magic, age):
   #     self.species = species
    #    self.magic = magic
     #   self.age = int(age)

#harry_potter = Character("Mage",True,17)
#print(f"Harry Potter is a {harry_potter.species} with magic == {harry_potter.magic}, and is {harry_potter.age} years old")


###### METHODS LESSONS
#class Bird:
 #   wings = True
#
 #   def __init__(self,color,species):
  #      self.color = color
   #     self.species = species

    #def whistles(self):
     #   print("whistle: chirp chirp")

    #def fly(self, meters):
     #   print(f"El bird is flying at {meters} meters")

#tweety = Bird("yellow","canary")
#print(tweety)
#tweety.fly(50)
#tweety.whistles()
#print(tweety.wings)

#class Dog:
 #   def __init__(self,times):
  #      self.times = int(times)

   # def bark(self):
    #    print("¡Guau!" * self.times)

#d = Dog(4)
#print(d)
#d.bark()

#class Mage:
 #   def __init__(self,name):
  #      self.name = name
   # def cast_spell(self,times):
    #    print("¡Abracadabra!"*times)

#m_1 = Mage("Merlin")
#m_1.cast_spell(4)

#class Alarm:
 #   def __init__(self,time_setup):
  #      self.time = time_setup
   # def move_alarm(self,minutes):
    #    print(f"The alarm will be moved {minutes} minutes")

#alarm_movement = Alarm("4:00 a.m.")
#alarm_movement.move_alarm(4)

##### THÉ OF METHODS CLASS
# Instance methods
#def my_method(self):
 #   XXX
# @classmethods
#@classmethod
#def my_method(cls):
 #   XXX
# @staticmethods
#---> CANNOT USE THE ATTIRBUTES OF THE CLASS
#@staticmethod
#def my_method():
 #   XXX
#---> CANNOT USE THE ATTIRBUTES OF NEITHER THE CLASS NOR THE METHOD

#INSTANCE METHODS AFFECT THE SELF... can access and modify the attributes of the instance

#class Bird:

 #   wings = True

  #  def __init__(self,color,species):
   #     self.color = color
    #    self.species = species

    #def whistles(self):
     #   print("¡Chirp Chirp!")

   # def fly(self, meters):
    #    print(f"El bird is flying at {meters} meters")
     #   self.whistles()

    #def chage_to_black(self):
     #   self.color = "Black"
      #  print(f"Now the bird is {self.color}")

#tweety = Bird("Yellow","canary")
#print(tweety.color)
#tweety.chage_to_black()

#CAN ACCESS OTHER METHODS

#tweety.fly(10)

#CAN MODIFFY THE STATUS OF THE CLASS
#tweety.wings = False
#print(tweety.wings)

#CLASS METHODS
#class Bird:

 #   wings = True

  #  def __init__(self,color,species):
   #     self.color = color
    #    self.species = species

    #def whistles(self):
     #   print("¡Chirp Chirp!")

#    def fly(self, meters):
 #       print(f"El bird is flying at {meters} meters")
  #      self.whistles()

   # def chage_to_black(self):
    #    self.color = "Black"
     #   print(f"Now the bird is {self.color}")

    #@classmethod
    #def lay_eggs(cls,egg_amount):
     #   print(f"Laid {egg_amount} eggs")
        # CANNOT BE DONE = print(f"The color is {self.color}")
      #  cls.wings = False
       # print(f"Now the wings attirbute is {Bird.wings}")

#Bird.lay_eggs(10)

#CLASSMETHODS DO NOT NEED AN INSTANCE DEFINED JUST A CLASS
#CLASSMETHODS CAN CHANGE CLASS ATTIRBUTES

#STATIC METHOD
#class Bird:

 #   wings = True

  #  def __init__(self,color,species):
   #     self.color = color
    #    self.species = species

    #def whistles(self):
     #   print("¡Chirp Chirp!")

    #def fly(self, meters):
     #   print(f"El bird is flying at {meters} meters")
      #  self.whistles()

    #def chage_to_black(self):
     #   self.color = "Black"
      #  print(f"Now the bird is {self.color}")

    #@classmethod
    #def lay_eggs(cls,egg_amount):
     #   print(f"Laid {egg_amount} eggs")
        # CANNOT BE DONE = print(f"The color is {self.color}")
      #  cls.wings = False
       # print(f"Now the wings attirbute is {Bird.wings}")

    #@staticmethod
    #def look():
     #   print("The bird is looking at you")

#CANNOT CHANGE OR USE INSTANCE ATTRIBUTES
#CANNOT CHANGE OR USE CLASS ATTRIBUTES

#Bird.look()


#class Pet:
 #   @staticmethod
  #  def breath():
   #     print("Inhale and Exhale")
#Pet.breath()

#class Player:
 #   alive = False
  #  @classmethod
   # def revive(cls):
    #    cls.alive = True
     #   print(f"The player is currently alive? {cls.alive} ")

#Player.revive()

#class Player:
 #   def number_of_rows(self,amount):
  #      self.amount = amount
   #     return amount

    #def throw_arrow(self):
     #   self.amount = self.amount - 1
      #  print(f"There are {self.amount} arrows left")

#number_one = Player()
#print(number_one.number_of_rows(10))
#number_one.throw_arrow()

##### INHERITANCE LESSON
#class Animal:
 #   def __init__(self,age,color):
  #      self.age = int(age)
   #     self.color = color
    #def be_born(self):
     #   print("This animal was born")


#class Bird(Animal):
 #   pass

#print(Bird.__bases__)
#print(Animal.__subclasses__())

##tweety = Bird(5,"yellow")
#tweety.be_born()
#print(tweety.color)
#print(tweety.age)

#class Person:
 #   def __init__(self,name,age):
  #      self.name = name
   #     self.age = age

#class Student(Person):
 #   pass

#class Pet:
 #   def __init__(self,age,name,number_of_legs):
  #      self.age = age
   #     self.name = name
    #    self.number_of_legs = number_of_legs

#class Dog(Pet):
 #   pass


#class Vehicle:
 #   @classmethod
  #  def accelerate(cls):
   #     pass
    #@classmethod
    #def brake(cls):
     #   pass

#class Car(Vehicle):
 #   pass

 ###### INHERITANCE EXTENSION LESSON
# Children class can have inherited methods, modified methods and new methods
# Multiple Inheritance

#class Animal:

 #   def __init__(self,age,color):
  #      self.age = int(age)
   #     self.color = color

    #def be_born(self):
     #   print("This animal was born")

    #def talk(self):
     #   print("The animal made a sound")



#class Bird(Animal):
 #   def __init__(self,age,color,fly_height):
  #      self.age = int(age)
   #     self.color = color
    #    self.fly_height = fly_height
    #def talk(self):
     #   print("Tweet")

    #def fly(self,meters):
     #   print(f"The bird flies {meters} meters")

#tweety = Bird(3,"yellow",50)
#tweety.be_born()
#tweety.talk() # OVERRIDES THE METHOD
#tweety.fly(21)

#runsho = Animal(10,"white and brown")

### BETTER METHOD TO GET THE INIT VALUES OF THE PARENT CLASS

#class Animal:

 #   def __init__(self,age,color):
  #      self.age = int(age)
   #     self.color = color

    #def be_born(self):
     #   print("This animal was born")

    #def talk(self):
     #   print("The animal made a sound")



#class Bird(Animal):
 #   def __init__(self,age,color,fly_height):
  #      super().__init__(age,color)
   #     self.fly_height = fly_height
    #def talk(self):
     #   print("Tweet")

    #def fly(self,meters):
     #   print(f"The bird flies {meters} meters")

#class Father:
 #   def talk(self):
  #      print("I'm the King in The North")

#class Mother:
 #   def laugh(self):
  #      print("JA JA JA")

   # def talk(self):
    #    print("How you doing?")

#class Children(Father,Mother):
 #   pass

#class Grandchildren(Children):
 #   pass

#jon = Grandchildren()
#jon.talk()
#jon.laugh()

# IF THERE IS A METHOD WITH THE SAME NAME AND PROPERTIES IN THE DIFFERENT PARENT CLASSES, THE CHILDREN CLASS WITH INHERIT THE METHOD OF THE CLASS THAT WAS FIRST INHERITED

#print(Grandchildren.__mro__)

#class Vertebrado:
 #   vertebrado = True

#class Ave(Vertebrado):
 #   tiene_pico = True
  #  def poner_huevos(self):
   #     print("Poniendo huevos")

#class Reptil(Vertebrado):
 #   venenoso = True

#class Pez(Vertebrado):
 #   def nadar(self):
  #      print("Nadando")
   # def poner_huevos(self):
    #    print("Poniendo huevos")

#class Mamifero(Vertebrado):
 #   def caminar(self):
  #      print("Caminando")
   # def amamantar(self):
    #    print("Amamantando crías")

#class Ornitorrinco(Mamifero,Ave,
  #                 Pez,Reptil):
 #   pass

#class Padre():
 #   color_ojos = "marrón"
  #  tipo_pelo = "rulos"
   # altura = "media"
    #voz = "grave"
    #deporte_preferido = "tenis"

    #def reir(self):
     #   return "Jajaja"

    #def hobby(self):
     #   return "Pinto madera en mi tiempo libre"

    #def caminar(self):
     #   return "Caminando con pasos largos y rápidos"


#class Hijo(Padre):
 #   def hobby(self):
  #      return "Juego videojuegos en mi tiempo libre"


###### POLIMORPHISM LESSON

#class Cow:
 #   def __init__(self,name):
  #      self.name = name

   # def talk(self):
    #    print(self.name + " says MUUUU")

#class Sheep:
 #   def __init__(self,name):
  #      self.name = name

   # def talk(self):
    #    print(self.name + " says BEEEE")

#c_1 = Cow("Aurora")
#s_1 = Sheep("Cloud")
#c_1.talk()
#s_1.talk()

#class Cow:
 #   def __init__(self,name):
  #      self.name = name

   # def talk(self):
    #    print(self.name + " says MUUUU")

#class Sheep:
 #   def __init__(self,name):
  #      self.name = name

   # def talk(self):
    #    print(self.name + " says BEEEE")

#c_1 = Cow("Aurora")
#s_1 = Sheep("Cloud")

#animals = [c_1,s_1]

#for n in animals:
    #n.talk()

#def animal_talks(animal):
 #   animal.talk()

#animal_talks(c_1)
#animal_talks(s_1)


#palabra = "polimorfismo"
#lista = ["Clases", "POO", "Polimorfismo"]
#tupla = (1, 2, 3, 80)

#for n in palabra,lista,tupla:
    #print(len(n))

#class Mago():
 #   def atacar(self):
  #      print("Ataque mágico")

#class Arquero():
 #   def atacar(self):
  #      print("Lanzamiento de flecha")

#class Samurai():
 #   def atacar(self):
  #      print("Ataque con katana")

#mage_1 = Mago()
#archer_1 = Arquero()
#samurai_1 = Samurai()

#player_list = [archer_1,mage_1,samurai_1]

#for n in player_list:
 #   n.atacar()

#class Mago():
 #   def defender(self):
  #      print("Escudo mágico")

#class Arquero():
 #   def defender(self):
  #      print("Esconderse")

#class Samurai():
 #   def defender(self):
  #      print("Bloqueo")

#def player_defends(player):
 #   player.defender()

#sam = Samurai()
#player_defends(sam)

##### HIDDEN & SPECIAL METHODS LESSON
#my_list = [1,1,1,1,1,1,1,1]
#print(len(my_list))

#class Object:
 #   pass

#my_object = Object()
#print(my_object)

#class CD:
 #   def __init__(self,author,tittle,songs):
  #      self.author = author
   #     self.tittle = tittle
    #    self.songs = songs

    #def __str__(self):
     #   return f"Album: {self.tittle} from {self.author}"

    #def __len__(self):
     #   return self.songs

    #def __del__(self):
     #   print(f"The CD <{self.tittle}> has been deleted")

#my_cd = CD("Pink Floyd","The Wall",24)
#print(str(my_cd))
#print(my_cd)
#print(len(my_cd))
#del my_cd


##### BANK ACCOUNT PROJECT
#Create a person: Class Person: attributes = name + last name
#Create a client: Class Client: attribute = Person.inheritance + account_number + Balance
#methods for client:-print basic information -Deposit to bank account -Withdrawal from ban account
#Ask the client to deposit, withdrawal or exit
#Function # 1: create client -> gives back a client created by class
#Function # 2: Main Menu

#Classes, Variables and Main Functions
stop_option = 4

class Client:
    def __init__(self,account_number,balance,first_name,last_name):
        self.account_number = account_number
        self.balance = int(balance)
        self.account_owner = first_name +" "+ last_name

    def client_basic_info(self):
        print(f"""CARNEROS ROYAL BANK ACCOUNT INFORMATION
        - Account Number: {self.account_number}
        - Current Balance: ${self.balance} USD
        - Account Owner: {self.account_owner} 
        """)

    def deposit(self,deposit_amount):
        self.balance = self.balance + deposit_amount

    def withdrawal(self,withdrawal_amount):
        if (withdrawal_amount > self.balance):
            return "Error 201: Insufficient Funds"
        else:
            self.balance = self.balance - withdrawal_amount

def continue_process():
    stop_security_key = "ANSIDNCOWMCOIEIMCIW7239E829389238JWINEIFNKEWNF823E0239E2398"
    continue_key = input("Please enter any character go back to the Carneros Royal Bank Account Menu: ")
    while continue_key == stop_security_key:
        break

def create_client():
    entry_first_name = input("What is the first name of the client?: ")
    entry_last_name = input(f"What is the last name of the client?: ")
    entry_account_number = input("Create an account number for the client: ")
    set_balance = input(f"Please set the current balance of the bank account {entry_account_number}: ")
    new_CRB_client = Client(entry_account_number,set_balance,entry_first_name,entry_last_name)
    return new_CRB_client

def bank_account_menu(client_X,stop_option):
    next_option = 0
    while stop_option != next_option:
        print("-" * 140)
        next_option = int(input(""" CARNEROS ROYAL BANK ACCOUNT MENU
            [1] Client Basic Information
            [2] Deposit Money
            [3] Withdrawal Money
            [4] Exit
         
            Choose the number of the process you wanna do next: """))
        print("-" * 140)
        if (next_option == 1):
            client_X.client_basic_info()
            continue_process()
        elif (next_option == 2):
            amount_to_deposit = int(input("Enter the amount that you wanna deposit on your bank account: "))
            client_X.deposit(amount_to_deposit)
            print(f"¡Your deposit was successful!")
            print(f"Your updated balance is: ${client_X.balance} USD")
            continue_process()
        elif (next_option == 3):
            amount_to_withdrawal = int(input("Enter the amount that you wanna withdrawal from your bank account: "))
            x = client_X.withdrawal(amount_to_withdrawal)
            while x == "Error 201: Insufficient Funds":
                print(f"Please enter a VALID amount, your current balance is ${client_X.balance} USD")
                amount_to_withdrawal = int(input("Enter the amount that you wanna withdrawal from your bank account: "))
                x = client_X.withdrawal(amount_to_withdrawal)
            print(f"¡Your withdrawal was successful!")
            print(f"Your updated balance is: ${client_X.balance} USD")
            continue_process()
    print(f"¡Take care {client_X.account_owner}, have a great day!")

#Bank Account Creation & Menu Complete Process
print("WELCOME TO CARNEROS ROYAL BANK")
print("-"*140)
print("¡Let's Create a New Client!")
bank_account_menu(create_client(),stop_option)
















