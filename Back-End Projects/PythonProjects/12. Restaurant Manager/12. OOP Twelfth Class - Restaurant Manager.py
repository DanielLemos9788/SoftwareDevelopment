#tkinter = Graphic interfaces
from tkinter import *

operator = ""

def click_button(number):
    global operator
    operator = operator + number
    calculator_visualizer.delete(0, END)
    calculator_visualizer.insert(END, operator)

def delete():
    global operator
    operator = ""
    calculator_visualizer.delete(0, END)

def get_result():
    global operator
    operation_result = str(eval(operator))
    calculator_visualizer.delete(0, END)
    calculator_visualizer.insert(0,operation_result)
    operator = ""

def check_check():
    x = 0
    for c in food_entry:
        if food_variables[x].get() == 1:
            food_entry[x].config(state=NORMAL)
            food_entry[x].delete(0, END)
            food_entry[x].focus()
        else:
            food_entry[x].config(state=DISABLED)
            food_text[x].set("0")
        x += 1

    x = 0
    for c in beverage_entry:
        if beverage_variables[x].get() == 1:
            beverage_entry[x].config(state=NORMAL)
            beverage_entry[x].delete(0, END)
            beverage_entry[x].focus()
        else:
            beverage_entry[x].config(state=DISABLED)
            beverage_text[x].set("0")
        x += 1

    x = 0
    for c in dessert_entry:
        if dessert_variables[x].get() == 1:
            dessert_entry[x].config(state=NORMAL)
            dessert_entry[x].delete(0, END)
            dessert_entry[x].focus()
        else:
            dessert_entry[x].config(state=DISABLED)
            dessert_text[x].set("0")
        x += 1



#Initiates tkinter
app = Tk()

#Size of the Screen
app.geometry("1250x480+0+0")

#aVOID maximize
app.resizable(0,0)

#Set Window Title
app.title("Restaurant Manager - Billing System")

#Background Color
app.config(bg="burlywood")

#Superior Panel
superior_panel = Frame(app, bd=2, relief=FLAT)
superior_panel.pack(side=TOP)
title_label = Label(superior_panel, text="Billing System", fg="black", font=("Roboto", 58), bg="burlywood", width=35)
title_label.grid(row=0, column=0)

#Left Panel
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

#Cost Panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg="azure4", padx=70, pady=17)
cost_panel.pack(side=BOTTOM)

#Food Panel
food_panel = LabelFrame(left_panel, text="Food", font=("Roboto", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
food_panel.pack(side=LEFT)

#Beverage Panel
beverage_panel = LabelFrame(left_panel, text="Beverage", font=("Roboto", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
beverage_panel.pack(side=LEFT)

#Dessert Panel
dessert_panel = LabelFrame(left_panel, text="Dessert", font=("Roboto", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
dessert_panel.pack(side=LEFT)

#Right Panel
right_panel = Frame(app, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

#Calculator Panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
calculator_panel.pack()

#Invoice Panel
invoice_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
invoice_panel.pack()

#Buttons Panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
buttons_panel.pack()

#List of Products
food_list = ["Butter Chicken", "Argentinian Beef", "Smoked Turkey", "Kebab", "Lasagna", "Fetta Pasta", "Tomato Soup", "Pulled Pork"]
beverage_list = ["Water", "Coke", "Mango Juice", "French Wine", "BBC Beer", "Coffee", "Passion Fruit Juice", "Aperol Spritz"]
dessert_list = ["Lemon Pie", "French Apple Tart", "Creme Brulee", "Brownies", "Ice Cream", "Mousse", "Milk Shake", "Carrot Cake"]

#Generate Food Items
food_variables = []
food_entry = []
food_text = []
counter = 0
for food in food_list:

    #Create Check Buttons
    food_variables.append("")
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel, text=food.title(), font=("Roboto", 19, "bold"), onvalue=1, offvalue=0, variable=food_variables[counter], command=check_check)
    food.grid(row=counter, column=0, sticky=W)

    #Create Open Entry
    food_entry.append("")
    food_text.append("")
    food_text[counter] = StringVar()
    food_text[counter].set("0")
    food_entry[counter] = Entry(food_panel, font=("Roboto", 18, "bold"), bd=1, width=2, state=DISABLED, textvariable=food_text[counter])
    food_entry[counter].grid(row=counter, column=1)

    counter += 1

#Generate Beverage Items
beverage_variables = []
beverage_entry = []
beverage_text = []
counter = 0
for beverage in beverage_list:

    # Create Check Buttons
    beverage_variables.append("")
    beverage_variables[counter] = IntVar()
    beverage = Checkbutton(beverage_panel, text=beverage.title(), font=("Roboto", 19, "bold"), onvalue=1, offvalue=0, variable=beverage_variables[counter], command=check_check)
    beverage.grid(row=counter, column=0, sticky=W)

    # Create Open Entry
    beverage_entry.append("")
    beverage_text.append("")
    beverage_text[counter] = StringVar()
    beverage_text[counter].set("0")
    beverage_entry[counter] = Entry(beverage_panel, font=("Roboto", 18, "bold"), bd=1, width=2, state=DISABLED, textvariable=beverage_text[counter])
    beverage_entry[counter].grid(row=counter, column=1)

    counter += 1

#Generate Dessert Items
dessert_variables = []
dessert_entry = []
dessert_text = []
counter = 0
for dessert in dessert_list:

    # Create Check Buttons
    dessert_variables.append("")
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel, text=dessert.title(), font=("Roboto", 19, "bold"), onvalue=1, offvalue=0, variable=dessert_variables[counter], command=check_check)
    dessert.grid(row=counter, column=0, sticky=W)

    # Create Open Entry
    dessert_entry.append("")
    dessert_text.append("")
    dessert_text[counter] = StringVar()
    dessert_text[counter].set("0")
    dessert_entry[counter] = Entry(dessert_panel, font=("Roboto", 18, "bold"), bd=1, width=2, state=DISABLED, textvariable=dessert_text[counter])
    dessert_entry[counter].grid(row=counter, column=1)

    counter += 1


#Variables
var_cost_of_food = StringVar()
var_cost_of_beverage = StringVar()
var_cost_of_dessert = StringVar()
var_cost_of_subtotal = StringVar()
var_cost_of_tax = StringVar()
var_cost_of_total = StringVar()


#Cost Labels and Entries
###FOOD
label_cost_food = Label(cost_panel,
                        text="Food Cost",
                        font=("Roboto", 18, "bold"),
                        bg="azure4",
                        fg="white")
label_cost_food.grid(row=0, column=0)

text_cost_food = Entry(cost_panel,
                       font=("Roboto", 18, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_cost_of_food)
text_cost_food.grid(row=0, column=1, padx=41)

###BEVERAGE
label_cost_beverage = Label(cost_panel,
                        text="Beverage Cost",
                        font=("Roboto", 18, "bold"),
                        bg="azure4",
                        fg="white")
label_cost_beverage.grid(row=1, column=0)

text_cost_beverage = Entry(cost_panel,
                       font=("Roboto", 18, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_cost_of_beverage)
text_cost_beverage.grid(row=1, column=1, padx=41)

###DESSERT
label_cost_dessert = Label(cost_panel,
                        text="Dessert Cost",
                        font=("Roboto", 18, "bold"),
                        bg="azure4",
                        fg="white")
label_cost_dessert.grid(row=2, column=0)

text_cost_dessert = Entry(cost_panel,
                       font=("Roboto", 18, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_cost_of_dessert)
text_cost_dessert.grid(row=2, column=1, padx=41)

###SUBTOTAL
label_cost_subtotal = Label(cost_panel,
                        text="Subtotal Cost",
                        font=("Roboto", 18, "bold"),
                        bg="azure4",
                        fg="white")
label_cost_subtotal.grid(row=0, column=2)

text_cost_subtotal = Entry(cost_panel,
                       font=("Roboto", 18, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_cost_of_subtotal)
text_cost_subtotal.grid(row=0, column=3, padx=41)

###TAX
label_cost_tax = Label(cost_panel,
                        text="Tax Cost",
                        font=("Roboto", 18, "bold"),
                        bg="azure4",
                        fg="white")
label_cost_tax.grid(row=1, column=2)

text_cost_tax = Entry(cost_panel,
                       font=("Roboto", 18, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_cost_of_tax)
text_cost_tax.grid(row=1, column=3, padx=41)

###TOTAL
label_cost_total = Label(cost_panel,
                        text="Tax Cost",
                        font=("Roboto", 18, "bold"),
                        bg="azure4",
                        fg="white")
label_cost_total.grid(row=2, column=2)

text_cost_total = Entry(cost_panel,
                       font=("Roboto", 18, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_cost_of_total)
text_cost_total.grid(row=2, column=3, padx=41)

#Buttons
buttons = ["Total", "Invoice", "Save", "Reset"]
columns = 0
for button in buttons:
    button = Button(buttons_panel,
                    text=button.title(),
                    font=("Roboto",18,"bold"),
                    fg="grey",
                    bg="azure4",
                    bd=1,
                    width=5)
    button.grid(row=0, column=columns)
    columns += 1

#Invoice Area
invoice_text = Text(invoice_panel,
                    font=("Roboto",18,"bold"),
                    bd=1,
                    width=42,
                    height=10)
invoice_text.grid(row=0, column=0)

#Calculator
calculator_visualizer = Entry(calculator_panel,
                              font=("Roboto",18,"bold"),
                              width=35,
                              bd=1)
calculator_visualizer.grid(row=0, column=0, columnspan=6)

calculator_buttton_list = ["7","8","9","+","4","5","6","-","1","2","3","x","=","Clean","0","/"]
saved_buttons_list = []

row_x = 1
column_x = 0
for button in calculator_buttton_list:
    button = Button(calculator_panel,
                    text=button.title(),
                    font=("Roboto",16,"bold"),
                    fg="grey",
                    bg="azure4",
                    bd=1,
                    width=6)
    saved_buttons_list.append(button)

    button.grid(row=row_x, column=column_x)

    if column_x == 3:
        row_x += 1

    column_x += 1

    if column_x == 4:
        column_x =0

saved_buttons_list[0].config(command=lambda : click_button("7"))
saved_buttons_list[1].config(command=lambda : click_button("8"))
saved_buttons_list[2].config(command=lambda : click_button("9"))
saved_buttons_list[3].config(command=lambda : click_button("+"))
saved_buttons_list[4].config(command=lambda : click_button("4"))
saved_buttons_list[5].config(command=lambda : click_button("5"))
saved_buttons_list[6].config(command=lambda : click_button("6"))
saved_buttons_list[7].config(command=lambda : click_button("-"))
saved_buttons_list[8].config(command=lambda : click_button("1"))
saved_buttons_list[9].config(command=lambda : click_button("2"))
saved_buttons_list[10].config(command=lambda : click_button("3"))
saved_buttons_list[11].config(command=lambda : click_button("*"))
saved_buttons_list[12].config(command=get_result)
saved_buttons_list[13].config(command=delete)
saved_buttons_list[14].config(command=lambda : click_button("0"))
saved_buttons_list[15].config(command=lambda : click_button("/"))


#Avoids Closing the Screen
app.mainloop()


