###### INTEGRATED MODEULES
# COLLECTIONS
# OS
# SHUTIL
#DATETIME
# MATH
# TIMEIT
# REGULAR EXPRESIONS

##### COLLECTIONS MODULE LESSON
"""
from collections import Counter

numbers = [1,2,3,4,5,6,7,8,9,10,4,4,4,4,2,2,2,3,3,3,3]
print(Counter(numbers))
print(Counter("mississippi"))
print(Counter("Al pan pan y al vino vino"))

series = Counter([1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,4])
print(series.most_common())
print(series.most_common(1))
print(series.most_common(2))
print(list(series))
"""

"""from collections import defaultdict"""
"""my_dic = {"one":"green","two":"blue","three":"red"}
print(my_dic)
print(my_dic["two"])"""
"""my_dic = defaultdict(lambda: "nothing")
my_dic["one"] = "green"
print((my_dic["two"]))
print(my_dic)
print(my_dic["one"])"""



"""from collections import namedtuple
my_tuple = (500,18,65)
print(my_tuple)
print(my_tuple[1])
person = namedtuple("Person",["name","height","weight"])
ariel = person("Ariel", 1.76, 79)
print(ariel.height)
print(ariel[2])"""

"""from collections import defaultdict
my_dic = defaultdict(lambda: "Nothing")
my_dic["age"] = 44
print(my_dic)
print(my_dic[1])"""

"""from collections import deque
queue_list = deque(["name", "age", "DOB"])
print(queue_list)
cities_queue = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(cities_queue)"""

##### OS & SHUTIL MODULES LESSON
"""import os
import shutil
print(os.getcwd())
file = open("curse_trial.txt","w")
file.write("Trial Nx Text")
file.close()
print(os.listdir())

#shutil.move("curse_trial.txt","C:\\Users\\DanielLemos\\Desktop")
#os.unlink() = DELETES A FILE
#os.rmdir() = DELETES AN EMPTY FOLDER
#os.rmtree() = DELETES EVERYTHING INSIDE A DIRECTORY

import send2trash
file = open("curse_trial_II.txt","w")
file.write("Trial Nx Text")
file.close()
send2trash.send2trash("curse_trial_II.txt")
send2trash.send2trash("curse_trial.txt")

print(os.walk(os.getcwd()))
directory = os.getcwd()
for folder,subfolder,file, in os.walk(directory):
    print(f"In the directory: {directory}")
    print(f"The subfolders are:")
    for sub in subfolder:
        print(f"\t{sub}")
    print("The files are:")
    for fil in file:
        print(f"\t{fil}")
    print("\n")"""

##### DATETIME MODULE LESSON
"""import datetime

my_hour = datetime.time(17, 35)
print(my_hour)
print(type(my_hour))
print(my_hour.hour)

my_day = datetime.date(2025, 10, 17)
print(my_day)
print(my_day.year)
print(my_day.ctime())
print(my_day.today())"""

"""from datetime import datetime

my_date = datetime(2025, 5, 15, 22, 10, 15, 2500)
print(my_date)
my_date = my_date.replace(month = 11)
print(my_date)

from datetime import date
birth = date(1995, 3, 5)
death = date(2095, 6, 19)

life = death - birth

print(life)
print(life.days)

awake = datetime(2022,10,5,7,30)
sleep = datetime(2022,10,5,23,45)

wake = sleep - awake
print(wake)
print(wake.seconds)"""

"""from datetime import *
my_date = datetime(1999,2,3)
print(my_date)
my_date = date(1999,2,3)
print(my_date)

today_date = my_date.today()
print(today_date)

new_date = time(20,43,55)
print(new_date)
minutes = new_date.minute
print(minutes)"""

##### TIME MEASURMENT MODULE LESSON
# time
# timeit
"""def for_trial(number):
    listx = []
    for n in range(1,number+1):
        listx.append(n)
    return listx

def while_trial(number):
    listx = []
    i = 1
    while i <= number:
        listx.append(i)
        i += 1
    return listx

print(for_trial(15))
print(while_trial(15))

import time

start = time.time()
for_trial(1000000)
end = time.time()
print(end - start)

start = time.time()
while_trial(1000000)
end = time.time()
print(end - start)

import timeit

statement = """
#for_trial(10)
"""
set_up = """
"""def for_trial(number):
    listx = []
    for n in range(1,number+1):
        listx.append(n)
    return listx"""
"""

duration_one = timeit.timeit(statement, set_up, number = 100000000)
print(duration_one)

statement_two = """
#while_trial(10)
"""
set_up_two = """
"""def while_trial(number):
    listx = []
    i = 1
    while i <= number:
        listx.append(i)
        i += 1
    return listx"""
"""

duration_two = timeit.timeit(statement_two, set_up_two, number = 100000000)
print(duration_two)"""

##### MATH MODULE LESSON
"""import math
result = math.floor(89.665)
print(result)
result = math.ceil(89.665)
print(result)
result = math.pi
print(result)
result = math.log(100, 5)
print(result)
result = math.log(25, 5)
print(result)
result = math.tan(2563)
print(result)
result = math.cos(90)
print(result)
result = math.sin(90)
print(result)"""
#Numpy
#Pandas

"""import math
result = math.factorial(7)
print(result)"""

###### REGULAR EXPRESSIONS MODULE LESSON
#/d = numeric
#/w = any string
#/s = whitespaces
#/D = NOT number
#/W = NOT strings
#/s = NOT whitespace

#Quantifiers
#+ = one or more times
#{n} = repeats n times
#{n,m} = repeats from n to m times
#{n,} = characters can go from n to infinity
#* = Zero or more times
#? = One or Zero (singular or plural)

"""text_x = "If you need help, please call (658)-598-9977 the number is available 24/7 through the online help channel"
word = "help" in text_x
print(word)

import re
pattern = "nothing"
search_v = re.search(pattern,text_x)
print(search_v)

pattern = "help"
search_v = re.search(pattern,text_x)
print(search_v)
print(search_v.start())
print(search_v.end())

pattern = "help"
search_v = re.findall(pattern,text_x)
print(search_v)
print(len(search_v))

for n in re.finditer(pattern,text_x):
    print(n.span())

textx = "Call 564-525-6588 right now"
pattern = r"\d\d\d-\d\d\d-\d\d\d\d"
result = re.search(pattern, textx)
print(result)
print(result.group())

pattern = r"\d{3}-\d{3}-\d{4}"
result = re.search(pattern, textx)
print(result)

pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
result = re.search(pattern, textx)
print(result.group(2))
print(result.group(3))
print(result.group(1))

#password = input("Password: ")
#pattern = r"\D{1}\w{7}"
#check_password = re.search(pattern, password)
#print(check_password)

textx = "We do not have service on monday"
search = re.search(r"monday|tuesday",textx)
print(search)

search = re.search(r"vice",textx)
print(search)

search = re.search(r".vice",textx)
print(search)

search = re.search(r"...vice",textx)
print(search)

search = re.search(r"...vice...",textx)
print(search)

search = re.search(r"^\D",textx)
print(search)

search = re.search(r"\D$",textx)
print(search)

search = re.findall(r"[^\s]",textx)
print(search)

search = re.findall(r"[^\s]+",textx)
print(search)
### SEARCHES ALL WORDS INSIDE A TEXT

print(" ".join(search))"""

"""import re
def verify_email(email):
    pattern_a ="@"
    pattern_b =".com"
    result_a = re.search(pattern_a,email)
    result_b = re.search(pattern_b,email)
    if (result_a == None or result_b == None):
        print("This is NOT a valid email address")
    else:
        print("Ok")

verify_email("hsjdhdj@hgh.com")
verify_email("fjwijfeij@wefmofem.br")
verify_email("sfdefJj1122@wearemo.com.br")"""

"""import re
def verify_greeting(phrase):
    x = re.search(r"^Hi|Hellow",phrase)
    if (x == None):
        print("You have NOT say Hi yet")
    else:
        print("Ok")


trial_phrase = "Messi is the goat in football history"
x = re.search(r"^\D",trial_phrase)
print(x)
x= re.search(r"^Hi|Hellow",trial_phrase)
print(x)
verify_greeting(trial_phrase)
trial_phrase = "Hi, Messi is the goat in football history"
verify_greeting(trial_phrase)"""

"""import re
def verify_postal_code(postal_code):
    regulatory_pattern = r"\w{2}\d{4}"
    x = re.search(regulatory_pattern,postal_code)
    if x:
        print("Ok")
    else:
        print("The postal code is INVALID")


verify_postal_code("AA1234")
verify_postal_code("AAA8982")
verify_postal_code("Z/1278")"""

##### COMPRESS AND DECOMPRESS FILES (ZIP)
#import zipfile
"""my_zip = zipfile.ZipFile("compressed_file.zip", "w")
my_zip.write("mi_texto_A.txt")
my_zip.write("mi_texto_B.txt")
my_zip.close()"""
"""open_zip = zipfile.ZipFile("compressed_file.zip","r")
open_zip.extractall()"""
#import shutil
"""original_folder = "C:\\Users\\DanielLemos\\PycharmProjects\\pythonProject\\9. Serial Number Searcher\\Superior_Folder"
destiny_folder = "Compressed_Superior"
shutil.make_archive(destiny_folder,"zip",original_folder)"""
#shutil.unpack_archive("Compressed_Superior.zip","Decompressed_Superior","zip")


##### SERIAL NUMBER SEARCHER PROJECT

#import shutil
#shutil.unpack_archive("Proyecto+Dia+9.zip","Project_9_Instructions","zip")
#Pattern == [N]+[3 text characters] + [-] + [5 numbers]

#Classes, Variables and Main Functions
from pathlib import *
from datetime import *
from math import *
import time
import os
import re

directory_folder = Path(os.getcwd(),"Mi_Gran_Directorio")
pattern_SNS = r"N\w\w\w-\d\d\d\d\d"
lorem_pattern = "lorem"
creation_date = date(2023,1,12)
creation_date_formatted = creation_date.strftime("%Y %m %d")
current_date = date.today()
current_date_formatted = current_date.strftime("%Y %m %d")

def serial_number_searcher(directory,pattern):
    text_list = []
    pattern_list = []
    for txt in Path(directory).glob("**/*.txt"):
        opened_txt = open(txt,"r")
        actual_text = opened_txt.read()
        x = re.search(pattern,actual_text)
        if (x == None):
            continue
        else:
            text_list.append(txt.stem)
            pattern_list.append(x.group())
    return text_list, pattern_list

#Main Process
print("-" * 140)
start = time.time()
print("PATTERN SEARCHER PROJECT")
print(f"Search Date: {current_date_formatted}")
print(f"{(current_date-creation_date).days} days have passed since the creation of this project")
print("\n")

list_one,list_two = serial_number_searcher(directory_folder,pattern_SNS)
pattern_and_file_dictionary = dict(zip(list_one,list_two))
print("\tFILES      \tPATTERNS")
print("\t--------- \t--------")
for keys,values in pattern_and_file_dictionary.items():
    print(f"\t{keys}  \t{values}")

print("\n")
print(f"The Pattern was Found: {len(list_two)} Times")
end = time.time()
print(f"Search Duration Time: {ceil(end-start)} Second(s)")
print("-" * 140)



















