from tkinter import *
from PIL import ImageTk, Image

# create the main window, object named root
root = Tk()

# giving title to the main window
root.title("Energy Output of Solar Cells & Powering a Home")
# root.geometry(width x height)
root.geometry('1000x750')

# introductory information
lbl = Label(root, text="Hi! In this module you will looking at the energy output of solar cells.")
lbl.grid(column=0, row=1, sticky=W, columnspan=6)
lbl2 = Label(root, text="A standard rooftop solar panel has an energy output of approximately 250 watts per hour.")
lbl2.grid(column=0, row=2, sticky=W, columnspan=6)

# picture
image = Image.open("house.png.png")
image = image.resize((350, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
canvas = Canvas(root, width=300, heigh=300)
canvas.image = img
canvas.grid(column=9, row=1, rowspan=10)
canvas.create_image(1, 1, anchor=NW, image=img)

# more introductory information
lbl3 = Label(root, text="On your house you can install a maximum of 8 solar panels.")
lbl3.grid(column=0, row=3, sticky=W, columnspan=6)
lbl4 = Label(root, text=" ")
lbl4.grid(column=0, row=4, sticky=W, columnspan=6)
lbl5 = Label(root, text="In your home, you need to power 5 light bulbs and the refrigerator.")
lbl5.grid(column=0, row=5, sticky=W, columnspan=6)
lbl6 = Label(root, text="The light bulbs use 60 watts per hour and the refrigerator uses 130 watts per hour.")
lbl6.grid(column=0, row=6, sticky=W, columnspan=6)

lbl7 = Label(root, text="You also have a cell phone that uses 5.45 watts per hour to charge")
lbl7.grid(column=0, row=7, sticky=W, columnspan=6)
lbl8 = Label(root, text="and a laptop that takes 197 watts per hour to charge.")
lbl8.grid(column=0, row=8, sticky=W, columnspan=6)

lbl9 = Label(root, text="Finally, you get about 6.5 peak sunlight hours a day. This means that the wattage of your solar cells")
lbl9.grid(column=0, row=9, sticky=W, columnspan=6)
lbl10 = Label(root, text="gets multiplied by the number of peak sunlight hours to get the total watts you can use a day.")
lbl10.grid(column=0, row=10, sticky=W, columnspan=6)

lbl11 = Label(root, text="If you have 1 solar panel, how many watts do you have to power your home in a day?")
lbl11.grid(column=0, row=11, sticky=W, columnspan=6)
check = DoubleVar()
check_entry = Entry(root, textvariable=check, width=10).grid(column=1, row=12)

# this is a practice for them to do the basic math that the program (more complicated) will do
def compare():
    if check.get() == 1625:
        lbl12 = Label(root, text="Correct!", fg="red")
        lbl12.grid(column=2, row=12)
    else:
        lbl12 = Label(root, text="Try again!", fg="red")
        lbl12.grid(column=2, row=12)

#  this button is for them to see if their math was correct
btn = Button(root, text="Submit", fg="red", command=compare).grid(column=0, row=12)

# introduction for them to select their appliances
lbl13 = Label(root, text=" ")
lbl13.grid(column=0, row=13, sticky=W, columnspan=6)
lbl14 = Label(root, text="Knowing all of this, you have to make decisions on what to power and for how long.")
lbl14.grid(column=0, row=14, sticky=W, columnspan=6)
lbl15 = Label(root, text="Use the dropdown menus to decide what you were powering, and then input for how long.")
lbl15.grid(column=0, row=15, sticky=W, columnspan=6)

# now we are create the drop down menues
# this gives the 5 options for the menu
OPTIONS = ["None", "5 Light Bulbs", "Refrigerator", "Cell Phone", "Laptop"]

# these variables are used to create the menus and then get the selected information from them later
# variable 1 is for menu 1, etc.
variable1 = StringVar(root)
variable1.set(OPTIONS[0])  # default value
variable2 = StringVar(root)
variable2.set(OPTIONS[0])
variable3 = StringVar(root)
variable3.set(OPTIONS[0])
variable4 = StringVar(root)
variable4.set(OPTIONS[0])

# these are headings for the menues and entry boxes
lbl16 = Label(root, text=" ")
lbl16.grid(column=0, row=16, sticky=W, columnspan=6)
lbl17 = Label(root, text="Items")
lbl17.grid(column=0, row=17)
lbl18 = Label(root, text="Number of Hours")
lbl18.grid(column=1, row=17)

# this are the created menus, see how the variables correspond
menu1 = OptionMenu(root, variable1, *OPTIONS)
menu1.grid(column=0, row=18)
menu2 = OptionMenu(root, variable2, *OPTIONS)
menu2.grid(column=0, row=19)
menu3 = OptionMenu(root, variable3, *OPTIONS)
menu3.grid(column=0, row=20)
menu4 = OptionMenu(root, variable4, *OPTIONS)
menu4.grid(column=0, row=21)

# these inputs are for the number of hours that each item will be used for
input1 = DoubleVar()
input1_entry = Entry(root, textvariable=input1, width=10).grid(column=1, row=18)
input2 = DoubleVar()
input2_entry = Entry(root, textvariable=input2, width=10).grid(column=1, row=19)
input3 = DoubleVar()
input3_entry = Entry(root, textvariable=input3, width=10).grid(column=1, row=20)
input4 = DoubleVar()
input4_entry = Entry(root, textvariable=input4, width=10).grid(column=1, row=21)

lbl19 = Label(root, text='Note: If you selects "None" leave the "Number of Hours" as 0.0.')
lbl19.grid(column=0, row=22, sticky=W, columnspan=6)

# function to calculate how many hours you need to use a set of solar panels depending on what appliances are selected
def calculate():
    # this is assigning the watts to the appliance that is picked, for each menu
    if variable1.get() == '5 Light Bulbs':
        val1 = 300
    elif variable1.get() == 'Refrigerator':
        val1 = 130
    elif variable1.get() == 'Cell Phone':
        val1 = 5.45
    elif variable1.get() == 'Laptop':
        val1 = 197
    else:
        val1 = 0

    if variable2.get() == '5 Light Bulbs':
        val2 = 300
    elif variable2.get() == 'Refrigerator':
        val2 = 130
    elif variable2.get() == 'Cell Phone':
        val2 = 5.45
    elif variable2.get() == 'Laptop':
        val2 = 197
    else:
        val2 = 0

    if variable3.get() == '5 Light Bulbs':
        val3 = 300
    elif variable3.get() == 'Refrigerator':
        val3 = 130
    elif variable3.get() == 'Cell Phone':
        val3 = 5.45
    elif variable3.get() == 'Laptop':
        val3 = 197
    else:
        val3 = 0

    if variable4.get() == '5 Light Bulbs':
        val4 = 300
    elif variable4.get() == 'Refrigerator':
        val4 = 130
    elif variable4.get() == 'Cell Phone':
        val4 = 5.45
    elif variable4.get() == 'Laptop':
        val4 = 197
    else:
        val4 = 0

    # this gives the total number of watts for each menu choice and the number of hours they want to use that choice
    wat1 = val1 * input1.get()
    wat2 = val2 * input2.get()
    wat3 = val3 * input3.get()
    wat4 = val4 * input4.get()

    # this gives the total wats from all 4 menus
    totalwatt = wat1 + wat2 + wat3 + wat4

    # this is the total watts formatted with 2 decimal places
    total = '{:.2f}'.format(totalwatt)

    # gives the total watts that are needed to power all choices
    lbl20 = Label(root, text='The total watts you need are ' + total)
    lbl20.grid(column=0, row=24)

    # gives the number of hours that are needed per each available solar panel (1-8) to power all choices
    # all information will be displayed
    if totalwatt <= 1625:
        hrs1 = totalwatt/6.5/1
        hours1 = '{:.2f}'.format(hrs1)
        lbl21 = Label(root, text="For 1 solar panel you need to use it for " + hours1 + "each.")
        lbl21.grid(column=8, row=14, sticky=W, columnspan=6)
    else:
        lbl21 = Label(root, text=" ")
        lbl21.grid(column=8, row=14, sticky=W, columnspan=6)

    if totalwatt <= 3250:
        hrs2 = totalwatt/6.5/2
        hours2 = '{:.2f}'.format(hrs2)
        lbl22 = Label(root, text="For 2 solar panels you need to use them for " + hours2 + "each.")
        lbl22.grid(column=8, row=15, sticky=W, columnspan=6)
    else:
        lbl22 = Label(root, text=" ")
        lbl22.grid(column=8, row=15, sticky=W, columnspan=6)

    if totalwatt <= 4875:
        hrs3 = totalwatt/6.5/3
        hours3 = '{:.2f}'.format(hrs3)
        lbl23 = Label(root, text="For 3 solar panels you need to use them for " + hours3 + "each.")
        lbl23.grid(column=8, row=16, sticky=W, columnspan=6)
    else:
        lbl23 = Label(root, text=" ")
        lbl23.grid(column=8, row=16, sticky=W, columnspan=6)

    if totalwatt <= 6500:
        hrs4 = totalwatt/6.5/4
        hours4 = '{:.2f}'.format(hrs4)
        lbl24 = Label(root, text="For 4 solar panels you need to use them for " + hours4 + "each.")
        lbl24.grid(column=8, row=17, sticky=W, columnspan=6)
    else:
        lbl24 = Label(root, text=" ")
        lbl24.grid(column=8, row=17, sticky=W, columnspan=6)

    if totalwatt <= 8125:
        hrs5 = totalwatt/6.5/5
        hours5 = '{:.2f}'.format(hrs5)
        lbl25 = Label(root, text="For 5 solar panels you need to use them for " + hours5 + "each.")
        lbl25.grid(column=8, row=18, sticky=W, columnspan=6)
    else:
        lbl25 = Label(root, text=" ")
        lbl25.grid(column=8, row=18, sticky=W, columnspan=6)

    if totalwatt <= 9750:
        hrs6 = totalwatt/6.5/6
        hours6 = '{:.2f}'.format(hrs6)
        lbl26 = Label(root, text="For 6 solar panels you need to use them for " + hours6 + "each.")
        lbl26.grid(column=8, row=19, sticky=W, columnspan=6)
    else:
        lbl26 = Label(root, text=" ")
        lbl26.grid(column=8, row=19, sticky=W, columnspan=6)

    if totalwatt <= 11375:
        hrs7 = totalwatt/6.5/7
        hours7 = '{:.2f}'.format(hrs7)
        lbl27 = Label(root, text="For 7 solar panels you need to use them for " + hours7 + "each.")
        lbl27.grid(column=8, row=20, sticky=W, columnspan=6)
    else:
        lbl27 = Label(root, text=" ")
        lbl27.grid(column=8, row=20, sticky=W, columnspan=6)

    if totalwatt <= 13000:
        hrs8 = totalwatt/6.5/8
        hours8 = '{:.2f}'.format(hrs8)
        lbl28 = Label(root, text="For 8 solar panels you need to use them for " + hours8 + "each.")
        lbl28.grid(column=8, row=21, sticky=W, columnspan=6)
    else:
        lbl28 = Label(root, text="You do not have enough solar panels or peak light hours for this amount of power")
        lbl28.grid(column=8, row=21, sticky=W, columnspan=6)

# runs the entire calculate function and displays it on the screen
btn2 = Button(root, text="Submit", fg="red", command=calculate).grid(column=0, row=23)

# calling mainloop method which is used
# when your application is ready to run, plus it tells the code to keep displaying
root.mainloop()
