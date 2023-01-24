##### STRING VARIABLE LESSONS
#name = "Daniel"
#print(name)
#name = "Laura"
#print(name)
#age1 = 30
#age2 = 20
#print(age1 + age2)
#name = input("Gimme your First Name: ")
#print("Your first name is "+name)
#wordI = "Hello"
#wordII = "Python"
#phrase = wordI +" "+ wordII
#print(phrase)
#age1 = 30
#age2 = 20
#combined_age = age1 + age2
#print(combined_age)

##### INTEGER AND FLOAT NUMBER LESSONS
#my_number = 5
#print(my_number)
#print(type(my_number))
#my_number = 6 + 14
#print(my_number)
#print(my_number + my_number)
#my_number = 5.87
#print(my_number)
#print(type(my_number))
#my_number = my_number**2
#print(my_number)
#print(type(my_number))
#my_number = 10 + 101.97
#print(my_number)

#father_age = input("Gimme your Father's Age: ")
#own_age = input("Gimme your Age: ")
#combined_age = father_age + own_age
#print("Your combined age is "+combined_age+" years old")

##### VARIABLE CONVERTION
#num_1 = 20
#num_2 = 40.5
#num_1 = num_1 + num_2
#print(num_1)
#print(type(num_1))

#num_1 = 5.8
#print(num_1)
#print(type(num_1))
##Eliminates the decimal numbers by force == Round-down or reduction
#num_2 = int(num_1)
#print(num_2)
#print(type(num_2))

#own_age = input("Gimme your Age: ")
#own_age = int(own_age)
#new_age = own_age + 1
#print("Next year your age is gonna be: "+str(new_age)+" years old")

##### FORMAT FUNCTION LESSON
#x = 10
#y = 5
#z = x + y
#print("My numbers are = {1} y {0}, and the sum is {2}".format(x,y,z))
#print("My numbers are = {0} y {1}".format(x,y))
#geeks = 75
#portal = 3440
#print(f"The users of the portal are {portal} and the slef-declared geek users are {geeks}")

#color = "red"
#plate_number = 645501
#print(f"Is your car the {color} down there with plates {plate_number}??")
#x = 5
#y = 2
#print(f"{x} plus {y} is equal to {x+y}")
#print(f"{x} minus {y} is equal to {x-y}")
#print(f"{x} times {y} is equal to {x*y}")
#print(f"{x} to the power of {y} is equal to {x**y}")
#print(f"{x} divided by {y} is equal to {x/y}")
#print(f"{x} residual of {y} is equal to {x%y}")
### ROUNDOWN
#z = 7
#print(f"{z} divided and rounded down by {y} is equal to {z//y}")
### RESIDUAL
#print(f"{z} residual of {y} is equal to {z%y}")
#print(f"{x} to the power of {5} is equal to {x**5}")
#print(f"The square root of {x} is equal to {x**0.5}")

###### FLOAT AND ROUNDING LESSON
#print(90/7)
#print(round(90/7,2))
#result = 90/7
#round_result = round(result,1)
#print(round_result)
#print(type(round_result))
#print(round(round_result))
#print(type(round_result))
#round_result = round(round_result)
#print(type(round_result))

###### CALCULATOR PROJECT
## Gets the information of the salesman
## Then returns the commission gained by the worker
print("SALES COMMISSIONS CALCULATOR \nThe commission percentage is set as 13%")
## Variables and information
commission_amount = 0.13
name_salesman = input("Insert your First and Last Names: ")
worker_id = input("Insert you Worker ID with no Spaces:  ")
total_monthly_sales = float(input("What were your Monthly Total Sales?: "))
## Shows the result and calculates the commission
print(f"ID={worker_id}, {name_salesman} your commissions this month are ${round(total_monthly_sales*commission_amount,2)} USD \nPlease claim your commission amount with a screenshot of this result and send an email to HR \nThe full commission amount will be reflected on your next salary")
