from matplotlib.widgets import Slider, Button  # import the Slider widget
import numpy as np
import matplotlib.pyplot as plt

# set the x coordinate values from 0 to 1 with a 0.01 step size
v = np.arange(0, 1, 0.01)

# first we create the general layout of the figure that the plot will go in
fig = plt.figure(figsize=(12, 5))

# with two axes objects: one for the plot of the function and the other for the slider
IV_ax = plt.axes([0.1, 0.2, 0.8, 0.65])
slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])

# variables for equation
Il = 0.5
I0 = 1.0*(10**(-10))
q = 1.602*(10**(-19))
k = 1.381*(10**(-23))
T = 293.0
n = 1.0

# diode equation for the first quadrant
I = Il - I0*(np.exp((q*v)/(n*k*T))-1)

# in plot_ax we plot the function with the initial value of the parameter T
plt.axes(IV_ax)
# plot labels
plt.title('IV')
plt.xlabel('Volts (V)')
plt.ylabel('Current (A)')
IVplot, = plt.plot(v, I, 'r')
# axes limits
plt.xlim(0, 1)
plt.ylim(0, 1)

# set values for the slider, this one deals with temperature
T_min = 0    # the minimum value of the parameter T
T_max = 40   # the maximum value of the parameter T
T_init = 20   # the value of the parameter a to be used initially, when the graph is created

# here we create the slider
T_slider = Slider(slider_ax,      # the axes object containing the slider
                  'Temperature',  # the name of the slider parameter
                  T_min,          # minimal value of the parameter
                  T_max,          # maximal value of the parameter
                  valinit=T_init)  # initial value of the parameter

# Next we define a function that will be executed each time the value indicated by the slider changes.
# The variable of this function will be assigned the value of the slider.
def update(val):
    temp = T_slider.val
    IVplot.set_ydata((Il - I0*(np.exp((q*v)/(n*k*(-temp+273.0)))-1.0)))  # set new y-coordinates of the plotted points
    fig.canvas.draw_idle()          # redraw the plot

# the final step is to specify that the slider needs to
# execute the above function when its value changes
T_slider.on_changed(update)

resetax = plt.axes([0.8, 0.005, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

# create a reset function for the slider
def reset(event):
    T_slider.reset()

# a button that activates the reset function
button.on_clicked(reset)

# display the plot
plt.show()
