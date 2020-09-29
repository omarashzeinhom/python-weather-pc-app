import tkinter as tk #imports the tkinter module as tk # tk here is ,like a root . aswell as canvas and button everything must be assigned to tk for this project #
from tkinter import font #] #from tkinter it uploads the fonts#
import requests # to import request for apis#

EXT_BG_HEIGHT = 500 #EXTERNAL_BACKGROUND_HEIGHT#
EXT_BG_WIDTH = 600 #EXTERNAL_BACKGROUND_WIDTH#

def test_function(entry):
	print("This is the entry:", entry)
#b4282279712e16edf506b464398f2027
#http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=b4282279712e16edf506b464398f2027

def format_response(weather): #this will take the weather json#	
	print(weather)
	try:
		name = weather ['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str= 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'
	return final_str


def get_weather(city):
	weather_key = 'b4282279712e16edf506b464398f2027'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)

	name = weather['name']
	print(weather['name'])
	print(weather['weather'][0]['description'])
	print(weather['main']['temp'])

root = tk.Tk() # start for anything we write inside it and the end ....but when we recall this anything will be tk.() as in tkdotbutton anything we are going to build are going to be inside these 2 clients#

canvas = tk.Canvas(root, height=EXT_BG_HEIGHT, width=EXT_BG_WIDTH) # root here is the master persay as they call it in tutorials point & height parameter must be defined and then to placed again#
canvas.pack() #canvas.pack() places the previour command tk.canvas(user, height=700, width=800) note the canvas is actually used as a canvas for widgets#

background_image = tk.PhotoImage(file='Backgroundimg.png') # cmd used to add a background image we define the variable assignt it to tk with .PhotoImage() file='used to enter file path'#
background_label = tk.Label(root, image=background_image) # cmd used to add a Label in tk background_image#
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#ee8262', bd=5) # tk.frame(user, bg='Blue') *** note that you can use hexadecimal colours by just getting it online and using # between ''marks example bk='#6c8752', bd = 5 , which is key argument that stands for border is used to border the # 
frame.place (relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n') #relativex = 0.1, rely=0.1 used to allign them one one side and point one on the other side , same relative height and length ///// for grid anchor helps place the widget into the exact spot it may 'n' or 'e' or 'w' ,'s' Which are north, east, west, south#

entry = tk.Entry(frame, font=45)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Find Weather Data", font=('Calibri', 10), command=lambda: get_weather(entry.get())) #frame is where we pass it in like the tkinter tutorials & text to be "Test Button ", bg='maroon' as in background colour is maroon# 
button.place(relx=0.7, relheight=1, relwidth=0.3)
#button.pack(side='left', fill='x', expand=True)# the previous example is for learning purposes .button .pack() places the previous command for buttons******Note button.pack() can be used to organize buttons # fill='both'  is used to fill a button , & expand=True it will give a bigger amount of the space that the frame has for the button widget#
#button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25) used to fill a button with the quarter of the screen #

lower_frame = tk.Frame(root, bg="#ff6347", bd=10) 
lower_frame.place (relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

 #note**double check grid formation# 

label = tk.Label(lower_frame, text="Get Weather", bg='#ffa54f' , fg='#f3ffff', font=('Calibri', 15), anchor='nw', justify='left', bd='4')
label.place(relwidth=1, relheight=1)

print(tk.font.families())

root.mainloop() # the end for anything we are going to build are going to be inside these 2 clients#


# frame is where we pass it in like the tkinter tutorials & text to be "Test Button ", bg='maroon' as in background colour is maroon# 
#button.pack(side='left', fill='x', expand=True)# the previous example is for learning purposes .button .pack() places the previous command for buttons******Note button.pack() can be used to organize buttons # fill='both'  is used to fill a button , & expand=True it will give a bigger amount of the space that the frame has for the button widget#
#button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25) used to fill a button with the quarter of the screen #
