# need to get tkinter GUI
from tkinter import *
# need to get matplotlib
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# create the main window, object named root
root = Tk()

# giving title to the main window
root.title("Hourly Efficiency of Solar Cells")
# root.geometry(width x height)
root.geometry('1250x1000')

# Label is what output will be
# show on the window
lbl = Label(root, text="Hi! In this module you will be looking at the temperature profile and light intensity for a day in your life.")
lbl.grid(column=0, row=0, sticky=W, columnspan=6)
lbl2 = Label(root, text="These two parameters will be used to calculate the efficiency of a solar cell hourly, throughout the day.")
lbl2.grid(column=0, row=1, sticky=W, columnspan=6)
lbl3 = Label(root, text="Go to engaging-data.com/solar-intensity/ to gather the solar intensity and a local weather site for the temperature.")
lbl3.grid(column=0, row=2, sticky=W, columnspan=6)
lbl4 = Label(root, text="On engaging-data, click on your relative region on the map and input the day of the year.")
lbl4.grid(column=0, row=3, sticky=W, columnspan=6)
lbl5 = Label(root, text="Input the temperature and solar intensity for each hour listen below and hit submit.")
lbl5.grid(column=0, row=4, sticky=W, columnspan=6)

lbl6 = Label(root, text=" ").grid(column=0, row=5)
lbl7 = Label(root, text="Note: Temperature should be in degrees Celsius and the solar intensity must be a non-zero number.")
lbl7.grid(column=0, row=6, sticky=W, columnspan=6)
lbl8 = Label(root, text=" ").grid(column=0, row=7)

# the label for inputting temperature data
eightT_label = Label(root, text='8:00 Temperature').grid(column=0, row=10, sticky=W)
# double variable to hold numbers
eightT = DoubleVar()
eightT_entry = Entry(root, textvariable=eightT, width=20).grid(column=1, row=10, sticky=W)

nineT_label = Label(root, text="9:00 Temperature").grid(column=0, row=11, sticky=W)
nineT = DoubleVar()
nineT_entry = Entry(root, textvariable=nineT, width=20).grid(column=1, row=11, sticky=W)

tenT_label = Label(root, text="10:00 Temperature").grid(column=0, row=12, sticky=W)
tenT = DoubleVar()
tenT_entry = Entry(root, textvariable=tenT, width=20).grid(column=1, row=12, sticky=W)

elevenT_label = Label(root, text="11:00 Temperature").grid(column=0, row=13, sticky=W)
elevenT = DoubleVar()
elevenT_entry = Entry(root, textvariable=elevenT, width=20).grid(column=1, row=13, sticky=W)

twelveT_label = Label(root, text="12:00 Temperature").grid(column=0, row=14, sticky=W)
twelveT = DoubleVar()
twelveT_entry = Entry(root, textvariable=twelveT, width=20).grid(column=1, row=14, sticky=W)

thirteenT_label = Label(root, text="13:00 Temperature").grid(column=0, row=15, sticky=W)
thirteenT = DoubleVar()
thirteenT_entry = Entry(root, textvariable=thirteenT, width=20).grid(column=1, row=15, sticky=W)

fourteenT_label = Label(root, text="14:00 Temperature").grid(column=0, row=16, sticky=W)
fourteenT = DoubleVar()
fourteenT_entry = Entry(root, textvariable=fourteenT, width=20).grid(column=1, row=16, sticky=W)

fifteenT_label = Label(root, text="15:00 Temperature").grid(column=0, row=17, sticky=W)
fifteenT = DoubleVar()
fifteenT_entry = Entry(root, textvariable=fifteenT,  width=20).grid(column=1, row=17, sticky=W)

sixteenT_label = Label(root, text="16:00 Temperature").grid(column=0, row=18, sticky=W)
sixteenT = DoubleVar()
sixteenT_entry = Entry(root, textvariable=sixteenT, width=20).grid(column=1, row=18, sticky=W)

seventeenT_label = Label(root, text="17:00 Temperature").grid(column=0, row=19, sticky=W)
seventeenT = DoubleVar()
seventeenT_entry = Entry(root, textvariable=seventeenT, width=20).grid(column=1, row=19, sticky=W)

eighteenT_label = Label(root, text="18:00 Temperature").grid(column=0, row=20, sticky=W)
eighteenT = DoubleVar()
eighteenT_entry = Entry(root, textvariable=eighteenT, width=20).grid(column=1, row=20, sticky=W)

nineteenT_label = Label(root, text="19:00 Temperature").grid(column=0, row=21, sticky=W)
nineteenT = DoubleVar()
nineteenT_entry = Entry(root, textvariable=nineteenT, width=20).grid(column=1, row=21, sticky=W)

twentyT_label = Label(root, text="20:00 Temperature").grid(column=0, row=22, sticky=W)
twentyT = DoubleVar()
twentyT_entry = Entry(root, textvariable=twentyT, width=20).grid(column=1, row=22, sticky=W)


# light intensity input
eightL_label = Label(root, text="8:00 Light Intensity").grid(column=2, row=10, sticky=W)
eightL = DoubleVar()
eightL_entry = Entry(root, textvariable=eightL, width=20).grid(column=3, row=10, sticky=W)

nineL_label = Label(root, text="9:00 Light Intensity").grid(column=2, row=11, sticky=W)
nineL = DoubleVar()
nineL_entry = Entry(root, textvariable=nineL, width=20).grid(column=3, row=11, sticky=W)

tenL_label = Label(root, text="10:00 Light Intensity").grid(column=2, row=12, sticky=W)
tenL = DoubleVar()
tenL_entry = Entry(root, textvariable=tenL, width=20).grid(column=3, row=12, sticky=W)

elevenL_label = Label(root, text="11:00 Light Intensity").grid(column=2, row=13, sticky=W)
elevenL = DoubleVar()
elevenL_entry = Entry(root, textvariable=elevenL, width=20).grid(column=3, row=13, sticky=W)

twelveL_label = Label(root, text="12:00 Light Intensity").grid(column=2, row=14, sticky=W)
twelveL = DoubleVar()
twelveL_entry = Entry(root, textvariable=twelveL, width=20).grid(column=3, row=14, sticky=W)

thirteenL_label = Label(root, text="13:00 Light Intensity").grid(column=2, row=15, sticky=W)
thirteenL = DoubleVar()
thirteenL_entry = Entry(root, textvariable=thirteenL, width=20).grid(column=3, row=15, sticky=W)

fourteenL_label = Label(root, text="14:00 Light Intensity").grid(column=2, row=16, sticky=W)
fourteenL = DoubleVar()
fourteenL_entry = Entry(root, textvariable=fourteenL, width=20).grid(column=3, row=16, sticky=W)

fifteenL_label = Label(root, text="15:00 Light Intensity").grid(column=2, row=17, sticky=W)
fifteenL = DoubleVar()
fifteenL_entry = Entry(root, textvariable=fifteenL, width=20).grid(column=3, row=17, sticky=W)

sixteenL_label = Label(root, text="16:00 Light Intensity").grid(column=2, row=18, sticky=W)
sixteenL = DoubleVar()
sixteenL_entry = Entry(root, textvariable=sixteenL, width=20).grid(column=3, row=18, sticky=W)

seventeenL_label = Label(root, text="17:00 Light Intensity").grid(column=2, row=19, sticky=W)
seventeenL = DoubleVar()
seventeenL_entry = Entry(root, textvariable=seventeenL, width=20).grid(column=3, row=19, sticky=W)

eighteenL_label = Label(root, text="18:00 Light Intensity").grid(column=2, row=20, sticky=W)
eighteenL = DoubleVar()
eighteenL_entry = Entry(root, textvariable=eighteenL, width=20).grid(column=3, row=20, sticky=W)

nineteenL_label = Label(root, text="19:00 Light Intensity").grid(column=2, row=21, sticky=W)
nineteenL = DoubleVar()
nineteenL_entry = Entry(root, textvariable=nineteenL, width=20).grid(column=3, row=21, sticky=W)

twentyL_label = Label(root, text="20:00 Light Intensity").grid(column=2, row=22, sticky=W)
twentyL = DoubleVar()
twentyL_entry = Entry(root, textvariable=twentyL, width=20).grid(column=3, row=22, sticky=W)

# data for silicon
# Voc decreases 2.2 mV/degC = 0.0022 V/degC
deltaV = 0.0022

# Isc increases 0.0006 amp/degC
deltaI = 0.0006

# start at room temp 25 degC
startT = 25.0

# get Voc, Isc, Vmp, and Imp from cells we are using
Voc = 7.2
Isc = 0.075
Vmp = 6.0
Imp = 0.07

# Voc temp change
Voc8 = Voc - (deltaV*(eightT.get() - startT))
Voc9 = Voc - (deltaV*(nineT.get() - startT))
Voc10 = Voc - (deltaV*(tenT.get() - startT))
Voc11 = Voc - (deltaV*(elevenT.get() - startT))
Voc12 = Voc - (deltaV*(twelveT.get() - startT))
Voc13 = Voc - (deltaV*(thirteenT.get() - startT))
Voc14 = Voc - (deltaV*(fourteenT.get() - startT))
Voc15 = Voc - (deltaV*(fifteenT.get() - startT))
Voc16 = Voc - (deltaV*(sixteenT.get() - startT))
Voc17 = Voc - (deltaV*(seventeenT.get() - startT))
Voc18 = Voc - (deltaV*(eighteenT.get() - startT))
Voc19 = Voc - (deltaV*(nineteenT.get() - startT))
Voc20 = Voc - (deltaV*(twentyT.get() - startT))

# Vmp temp change
Vmp8 = Vmp - (deltaV*(eightT.get() - startT))
Vmp9 = Vmp - (deltaV*(nineT.get() - startT))
Vmp10 = Vmp - (deltaV*(tenT.get() - startT))
Vmp11 = Vmp - (deltaV*(elevenT.get() - startT))
Vmp12 = Vmp - (deltaV*(twelveT.get() - startT))
Vmp13 = Vmp - (deltaV*(thirteenT.get() - startT))
Vmp14 = Vmp - (deltaV*(fourteenT.get() - startT))
Vmp15 = Vmp - (deltaV*(fifteenT.get() - startT))
Vmp16 = Vmp - (deltaV*(sixteenT.get() - startT))
Vmp17 = Vmp - (deltaV*(seventeenT.get() - startT))
Vmp18 = Vmp - (deltaV*(eighteenT.get() - startT))
Vmp19 = Vmp - (deltaV*(nineteenT.get() - startT))
Vmp20 = Vmp - (deltaV*(twentyT.get() - startT))

# Isc temp change
Isc8 = Isc + (deltaI*((eightT.get()) - startT))
Isc9 = Isc + (deltaI*((nineT.get()) - startT))
Isc10 = Isc + (deltaI*((tenT.get()) - startT))
Isc11 = Isc + (deltaI*((elevenT.get()) - startT))
Isc12 = Isc + (deltaI*((twelveT.get()) - startT))
Isc13 = Isc + (deltaI*((thirteenT.get()) - startT))
Isc14 = Isc + (deltaI*((fourteenT.get()) - startT))
Isc15 = Isc + (deltaI*((fifteenT.get()) - startT))
Isc16 = Isc + (deltaI*((sixteenT.get()) - startT))
Isc17 = Isc + (deltaI*((seventeenT.get()) - startT))
Isc18 = Isc + (deltaI*((eighteenT.get()) - startT))
Isc19 = Isc + (deltaI*((nineteenT.get()) - startT))
Isc20 = Isc + (deltaI*((twentyT.get()) - startT))

# Imp temp change
Imp8 = Imp + (deltaI*((eightT.get()) - startT))
Imp9 = Imp + (deltaI*((nineT.get()) - startT))
Imp10 = Imp + (deltaI*((tenT.get()) - startT))
Imp11 = Imp + (deltaI*((elevenT.get()) - startT))
Imp12 = Imp + (deltaI*((twelveT.get()) - startT))
Imp13 = Imp + (deltaI*((thirteenT.get()) - startT))
Imp14 = Imp + (deltaI*((fourteenT.get()) - startT))
Imp15 = Imp + (deltaI*((fifteenT.get()) - startT))
Imp16 = Imp + (deltaI*((sixteenT.get()) - startT))
Imp17 = Imp + (deltaI*((seventeenT.get()) - startT))
Imp18 = Imp + (deltaI*((eighteenT.get()) - startT))
Imp19 = Imp + (deltaI*((nineteenT.get()) - startT))
Imp20 = Imp + (deltaI*((twentyT.get()) - startT))

# calculate the Fill Factor = (Vmp*Imp)/(Voc*Isc)
FF8 = (Vmp8*Imp8)/(Voc8*Isc8)
FF9 = (Vmp9*Imp9)/(Voc9*Isc9)
FF10 = (Vmp10*Imp10)/(Voc10*Isc10)
FF11 = (Vmp11*Imp11)/(Voc11*Isc11)
FF12 = (Vmp12*Imp12)/(Voc12*Isc12)
FF13 = (Vmp13*Imp13)/(Voc13*Isc13)
FF14 = (Vmp14*Imp14)/(Voc14*Isc14)
FF15 = (Vmp15*Imp15)/(Voc15*Isc15)
FF16 = (Vmp16*Imp16)/(Voc16*Isc16)
FF17 = (Vmp17*Imp17)/(Voc17*Isc17)
FF18 = (Vmp18*Imp18)/(Voc18*Isc18)
FF19 = (Vmp19*Imp19)/(Voc19*Isc19)
FF20 = (Vmp20*Imp20)/(Voc20*Isc20)

# calculate and display hourly efficiency and graph
def calculate():
    # calculate cell conversion efficiency (eta) eta=(Voc*Isc*FF)/Pinput
    # needs to be in def calculate so that it doesn't run until the user inputs power data
    eta8s = 100 * (Voc8 * Isc8 * FF8) / eightL.get()
    # this is the efficiency formatted to 2 decimal places
    eta8 = '{:.2f}'.format(eta8s)
    eta9s = 100 * (Voc9 * Isc9 * FF9) / nineL.get()
    eta9 = '{:.2f}'.format(eta9s)
    eta10s = 100 * (Voc10 * Isc10 * FF10) / tenL.get()
    eta10 = '{:.2f}'.format(eta10s)
    eta11s = 100 * (Voc11 * Isc11 * FF11) / elevenL.get()
    eta11 = '{:.2f}'.format(eta11s)
    eta12s = 100 * (Voc12 * Isc12 * FF12) / twelveL.get()
    eta12 = '{:.2f}'.format(eta12s)
    eta13s = 100 * (Voc13 * Isc13 * FF13) / thirteenL.get()
    eta13 = '{:.2f}'.format(eta13s)
    eta14s = 100 * (Voc14 * Isc14 * FF14) / fourteenL.get()
    eta14 = '{:.2f}'.format(eta14s)
    eta15s = 100 * (Voc15 * Isc15 * FF15) / fifteenL.get()
    eta15 = '{:.2f}'.format(eta15s)
    eta16s = 100 * (Voc16 * Isc16 * FF16) / sixteenL.get()
    eta16 = '{:.2f}'.format(eta16s)
    eta17s = 100 * (Voc17 * Isc17 * FF17) / seventeenL.get()
    eta17 = '{:.2f}'.format(eta17s)
    eta18s = 100 * (Voc18 * Isc18 * FF18) / eighteenL.get()
    eta18 = '{:.2f}'.format(eta18s)
    eta19s = 100 * (Voc19 * Isc19 * FF19) / nineteenL.get()
    eta19 = '{:.2f}'.format(eta19s)
    eta20s = 100 * (Voc20 * Isc20 * FF20) / twentyL.get()
    eta20 = '{:.2f}'.format(eta20s)

    # display the efficiency for each hour
    Label(root, text='8:00 % efficiency = ' + str(eta8)).grid(column=0, row=24, sticky=W)
    Label(root, text='9:00 % efficiency = ' + str(eta9)).grid(column=0, row=25, sticky=W)
    Label(root, text='10:00 % efficiency = ' + str(eta10)).grid(column=0, row=26, sticky=W)
    Label(root, text='11:00 % efficiency = ' + str(eta11)).grid(column=0, row=27, sticky=W)
    Label(root, text='12:00 % efficiency = ' + str(eta12)).grid(column=1, row=24, sticky=W)
    Label(root, text='13:00 % efficiency = ' + str(eta13)).grid(column=1, row=25, sticky=W)
    Label(root, text='14:00 % efficiency = ' + str(eta14)).grid(column=1, row=26, sticky=W)
    Label(root, text='15:00 % efficiency = ' + str(eta15)).grid(column=1, row=27, sticky=W)
    Label(root, text='16:00 % efficiency = ' + str(eta16)).grid(column=2, row=24, sticky=W)
    Label(root, text='17:00 % efficiency = ' + str(eta17)).grid(column=2, row=25, sticky=W)
    Label(root, text='18:00 % efficiency = ' + str(eta18)).grid(column=2, row=26, sticky=W)
    Label(root, text='19:00 % efficiency = ' + str(eta19)).grid(column=2, row=27, sticky=W)
    Label(root, text='20:00 % efficiency = ' + str(eta20)).grid(column=3, row=24, sticky=W)

    # graph it
    figure = Figure(figsize=(5, 4), dpi=100)
    pl = figure.add_subplot(1, 1, 1)

    x = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    y = [eta8s, eta9s, eta10s, eta11s, eta12s, eta13s, eta14s, eta15s, eta16s, eta17s, eta18s, eta19s, eta20s]
    pl.plot(x, y)

    pl.set_title('Solar Cell Efficiency per Hour')
    pl.set_xlabel('Time of the Day by Hour')
    pl.set_ylabel('Efficiency in %')

    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().grid(column=8, row=6, rowspan=20)

# button widget with red color text
# btn = Button(root, text="Submit", fg="red", command=clicked)
btn = Button(root, text="Submit", fg="red", command=calculate).grid(column=0, row=23)

# calling mainloop method which is used
# when your application is ready to run, plus it tells the code to keep displaying
root.mainloop()
