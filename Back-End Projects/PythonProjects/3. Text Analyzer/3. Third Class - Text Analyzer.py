###### INDEX FUNCTION
#my_text = "This is the first trial"
#result = my_text[0]
#print(f"{my_text} + {result}")
#result = my_text[9]
#print(result)
#result = my_text.index("trial")
#print(result)
#result = my_text.index("i")
#print(result)
#result = my_text.index("i",5)
#print(result)
#result = my_text.index("i",6,15)
#print(result)
#result = my_text.rindex("a")
#print(result)

##### MANIPULATE STRINGS == SLICING
#text = "ABCDEFGHIJKLM"
#print(text)
#fragment = text[2]
#print(fragment)
#fragment = text[:5]
#print(fragment)
#fragment = text[2:5]
#print(fragment)
#fragment = text[2:10:2]
#print(fragment)
#fragment = text[::2]
#print(fragment)
#fragment = text[::-2]
#print(fragment)

###### Upper, Lower, Split, Join, Find, Replace Functions
#text = "Leo Messi is the Best Futbol Player in all History"
#result = text
#print(result)
#print(result.upper())
#print(result.lower())
#print(result[17:].upper())
#print(result.split())
#print(result.split("t"))
#a = "Learning"
#b = "Python"
#c = "is"
#d = "Marvelous"
#e = " "
#print(e.join([a,b,c,d]))
#e = "-"
#print(e.join([a,b,c,d]))
### FIND METHOD
#print(text)
#print(result.find("s"))
#When it looks for something that does not exits in the code the result will be -1
#print(result.find("z"))
### REPLACE METHOD
#print(result.replace("Messi","Andreas"))
#print(result.replace("Messi","Andreas"))
#print(result.replace("i","X"))

##### STRINGS ARE: INMUTABLE, ARE ABLE TO CONCATENATE, MULTIPLY STRINGS, MULTILINES OR PARAGRAPH, LENGTH
#name = "Carina"
#print(name)
#name = "Karina"
#print(name)
#n = "Karim"
#m = "Benzema"
#print(n + m)
#print(n * 8)
#print((n + m) * 8)

#poem = """For eternity on the throne
#He made of stone
#She out of bones
#Spirits connected all the way
#But yet in live slipped away"""
#print(poem)
### TRUE OR FALSE IS A STRING IS INSIDE ANOTHER STRING
#print("water" in poem)
#print("water" not in poem)
### LENGTH OF A STRING
#print(len(poem))

##### LISTS
#my_list = ["a","b","c","d"]
#second_list = ["hi",5,12.5]
#result = len(my_list)
#print(type(my_list))
#print(type(second_list))
#print(result)
#result = my_list[0]
#print(result)
#result = my_list[0:3]
#print(result)
#own_list = ["e","f","g"]
### CONCATENATE
#print(my_list+own_list)
#my_list[0] = "alpha"
#print(my_list)
#my_list.append("i")
#print(my_list)
#my_list.pop()
#print(my_list)
#deleted = my_list.pop(0)
#print(deleted)
###SORT LISTS
#list = ["g","o","b","m","c"]
#print(list)
#list.sort()
### SORT DOES NOT CREATE A NEW LIST JUST SORTS THE LIST
#print(list)
#list.reverse()
#print(list)
#list.reverse()
#print(list)

##### DICTIONARIES
### Concept + Key == Unique keys, values may be repeated
#my_dic = {"a":"1","b":"2","c":"3"}
#dictionary = {"c1":"value_1","c2":"value_2"}
#print(type(dictionary))
#print(dictionary)
#result = dictionary["c1"]
#print(result)
#client = {"first_name":"Jack","last_name":"Smith","weight":85,"height":176}
#information = (client["first_name"])
#print(information)
#information = (client["height"])
#print(information)
###DICTIONARIES INSIDE DICTIONARIES
#dictionary = {"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":200}}
#print(dictionary["c2"])
#print(dictionary["c3"])
#new_variable = dictionary["c3"]
#print(new_variable)
#print(new_variable["s2"])
#print(dictionary["c2"][1])
#print(dictionary["c3"]["s1"])
#dictionary = {"c1":["a","b","c"],"c2":["d","e","f"]}
#print(dictionary)
#section_one = dictionary["c1"]
#print(section_one)
#section_two = dictionary["c2"]
#print(section_two)
#connected = section_one + section_two
#connected.sort()
#print(connected)
#print(dictionary["c2"][1].upper())
###ADD ELEMENT TO A DICTIONARY
#dictionary = {1:"a",2:"b"}
#print(dictionary)
#dictionary[3] = "c"
#print(dictionary)
#dictionary[2] = "alpha"
#print(dictionary)
#print(dictionary.keys())
#print(dictionary.values())
#print(dictionary.items())

##### TUPLES LESSON: less memory on python, inmutable
#tuple = (1,2,3,4)
#print(tuple)
#print(tuple[0])
#tuple = (1,2,(10,20),4)
#print(tuple)
#print(tuple[2][1])
#tuple = list(tuple)
#print(tuple)
#t = (1,2,3)
#print(t)
#x,y,z = t
#print(x,y,z)
### MUST HAVE THE SAME NUMBER OF ELEMENTS AS THE LIST, TUPLE OR DICTIONARY
#t = (1,2,3,4)
#print(t)
#print(len(t))
#print(t.count(2))
#print(t.index(2))

##### SETS LESSON: UNIQUE ELEMENTS, NOT SORTED, INMUTABLE
#my_set = set([1,2,3,4,5])
#print(type(my_set))
#print(my_set)
#another_set = {1,2,3}
#print(type(another_set))
#print(another_set)
### I CANNOT INCLUDE LISTS OR DICTIONARIES, BUT I CAN INCLUDE TUPLES
#new_set = set([1,2,3,4,(1,2,3),5,6])
#print(new_set)
#print(len(new_set))
#print(2 in new_set)
###UNION OF SETS
#s1 = {1,2,3}
#print(s1)
#s2 = {3,4,5}
#print(s2)
#s3 = s1.union(s2)
#print(s3)
#s3 = s1.intersection(s2)
#print(s3)
#s1.add(4)
#print(s1)
#s1.remove(3)
#print(s1)
#s1.discard(6)
#print(s1)
#s1.pop()
### SINCE THERE IS NO REAL ORDER ON SETS, POP ELIMINATES A RANDOM ELEMENT OF THE SET
#print(s1)
#s1.clear()
#print(s1)

##### BOOLEANS LESSON
#var_one = True
#var_two = False
#print(type(var_one))
#print(var_one)
#number = 5 > 2+3
#print(type(number))
#print(number)
#n = 5 == 2+3
#print(type(n))
#print(n)
#n_1 = 5 != 2+3
#print(type(n_1))
#print(n_1)
#num = bool(5>6)
#print(type(num))
#print(num)
### TO GENERATE AUTOMATIC FALSE VALUES
#N = bool()
#print(type(N))
#print(N)

#list = [1,2,3,4]
#control = 5 in list
#print(type(control))
#print(control)



##### TEXT ANALYZER PROJECT
#Insert a Text
#Insert 3 desire letters
#Return 5 results:
#1 How many times each letter appears
#2 How many words are in the text
#3 First and Last letters of the text
#4 Invert the Text
#5 Look for the word Python inside the Text (true or false must be the returned answer)
print("RANDOM TEXT ANALYZER")
print("----------------------------------------------------------------------")
#Inputs and Variables
#Text: Hellow Damn World, Leo Messi is the best futbol player in the world.
random_text = input("Please Insert the Text You Want to Have Analyzed:")
first_letter = input("Choose the First Letter or Word you Wanna Count:").upper()
second_letter = input("Choose the Second Letter or Word you Wanna Count:").upper()
third_letter = input("Choose the Third Letter or Word you Wanna Count:").upper()
random_text_upper = random_text.upper()
# 1. Find how many times each letter or character choosen appears inside the text
print("----------------------------------------------------------------------")
print("COUNT OF LETTERS")
print(f"Your first letter or word appears:{random_text_upper.count(first_letter)} times")
print(f"Your second letter or word appears:{random_text_upper.count(second_letter)} times")
print(f"Your third letter or word appears:{random_text_upper.count(third_letter)} times")
print("----------------------------------------------------------------------")
# 2. Counts the number of words in the text
print("COUNT OF WORDS")
random_text_list = (random_text.split())
print(f"The number of words inside the text is: {len(random_text_list)}")
print("----------------------------------------------------------------------")
# 3. Shows the first and las letters of the text including punctuation
print("FIRST AND LAST WORDS")
print(f"The first word in the text is: {random_text_list[0]}")
print(f"The last word in the text is: {random_text_list[len(random_text_list)-1]}")
print("----------------------------------------------------------------------")
# 4. Inverts the text, starting from the last word to the first one
print("TEXT INVERSION")
space = " "
print(f"The inversion of the text is: \n{space.join(random_text_list[::-1])}")
print("----------------------------------------------------------------------")
# 5. Look for the word Python inside the text
print("PYTHON WORD IN TEXT")
python = "PYTHON"
python_result = random_text_upper.find(python) != -1
dictionary = {True:"has",False:"does not have"}
print(f"The text {dictionary[python_result]} the word Python inside")
print("----------------------------------------------------------------------")

