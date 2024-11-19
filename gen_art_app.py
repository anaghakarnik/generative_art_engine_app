from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Button, PhotoImage, colorchooser, messagebox

import turtle
import random

# COLORS
COLORS = []
# TURTLE SPEED
SPEED = 10

bgcolor = 'white'

def spiral():
    # Screen object
    screen = turtle.Screen()
    # Set the title of the window
    screen.title("Canvas")

    # Set up the screen
    turtle.bgcolor(bgcolor)
    turtle.tracer(None)

    # Set up the turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(SPEED)
    t.width(2)

    # Define the number of petals and the size
    num_petals = 50
    radius = 150

    # Draw the spiral flower pattern
    for i in range(num_petals):
        t.pencolor(COLORS[i%len(COLORS)])        
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.circle(radius, steps=6)  # Draw a hexagon-shaped petal
        t.right(360 / num_petals)  # Rotate for the next petal
        
        radius -= 2  # Reduce the radius slightly to create a spiral effect

    # Update and display the drawing
    turtle.update()

def flower():
    # Screen object
    screen = turtle.Screen()
    # Set the title of the window
    screen.title("Canvas")

    # Set up the screen
    turtle.bgcolor(bgcolor)
    turtle.tracer(None)

    # Set up the turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(SPEED)
    t.width(2)

    nums = [200, 190, 120, 100, 60, 50]

    for i in range(6):
        for j in range(6):
            t.fillcolor(COLORS[i])
            t.pencolor(COLORS[i])
            t.begin_fill()
            t.circle(nums[i]-j, 90)
            t.left(90)
            t.circle(nums[i]-j, 90)
            t.left(18)
            t.end_fill()

    turtle.update()


def destijl():
    # Screen object
    screen = turtle.Screen()
    # Set the title of the window
    screen.title("Canvas")

    # Set up the screen
    turtle.bgcolor(bgcolor)
    turtle.tracer(None)

    # Set up the turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(SPEED)
    t.pensize(3)
    t.pencolor('black')  

    rows = 10
    columns = 10
    spacing_x = 100
    spacing_y = 100

    def draw(x, y):         
        num1 = random.randint(0, 3)
        t.penup()
        t.goto(x, y - 30)
        t.pendown()
        t.fillcolor(COLORS[num1])
        t.begin_fill()
        w = random.randint(50, 200)
        h = random.randint(50, 200)
        for _ in range(2):
            t.forward(w)
            t.right(90)
            t.forward(h)
            t.right(90)
        t.end_fill()

    for row in range(rows):
        for col in range(columns):
            x = col * spacing_x - 500
            y = row * spacing_y - 200
            draw(x, y)
    
    # Update and display the drawing
    turtle.update()

def circles():
    # Screen object
    screen = turtle.Screen()
    # Set the title of the window
    screen.title("Canvas")

    # Set up the screen
    turtle.bgcolor(bgcolor)
    turtle.tracer(None)

    # Set up the turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(SPEED)
    t.pensize(3)
    t.pencolor('black') 

    # Function to draw a shape
    def draw_circles(x, y):        
        num1 = random.randint(0, 2)
        t.penup()
        t.goto(x, y - 30)
        t.pendown()
        t.pencolor(COLORS[num1])
        t.fillcolor(COLORS[num1])
        t.begin_fill()
        t.circle(60)
        t.end_fill()

        num2 = random.randint(0, 2)
        while num2 == num1:
            num2 = random.randint(0, 2)
        t.penup()
        t.goto(x, y-10)
        t.pendown()
        t.pencolor(COLORS[num2])
        t.fillcolor(COLORS[num2])
        t.begin_fill()
        t.circle(40)
        t.end_fill()

        num3 = random.randint(0, 2)
        while num3 == num1 or num3 == num2:
            num3 = random.randint(0, 2)
        t.penup()
        t.goto(x, y+10)
        t.pendown()
        t.pencolor(COLORS[num3])
        t.fillcolor(COLORS[num3])
        t.begin_fill()
        t.circle(20)
        t.end_fill()

    rows = 5
    columns = 5
    spacing_x = 150
    spacing_y = 150

    for row in range(rows):
        for col in range(columns):
            x = col * spacing_x - 300
            y = row * spacing_y - 300
            draw_circles(x, y)

    # Update and display the drawing
    turtle.update()

def mickey():
    # Screen object
    screen = turtle.Screen()
    # Set the title of the window
    screen.title("Canvas")

    # Set up the screen
    turtle.bgcolor(bgcolor)
    turtle.tracer(None)

    # Set up the turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(SPEED)
    t.pensize(10)
    t.pencolor(COLORS[0])
    t.fillcolor(COLORS[0])

    # Draw the main head circle
    t.penup()
    t.goto(0, -150)  # Position for the head
    t.pendown()
    t.begin_fill()
    t.circle(150)
    t.end_fill()

    # Draw the left ear
    t.penup()
    t.goto(-150, 90)  # Position for the left ear
    t.pendown()
    t.begin_fill()
    t.circle(75)
    t.end_fill()

    # Draw the right ear
    t.penup()
    t.goto(150, 90)  # Position for the right ear
    t.pendown()
    t.begin_fill()
    t.circle(75)
    t.end_fill()

    # Update and display the drawing
    turtle.update()

def smile():
    # Screen object
    screen = turtle.Screen()
    # Set the title of the window
    screen.title("Canvas")

    # Set up the screen
    turtle.bgcolor(bgcolor)
    turtle.tracer(None)

    # Set up the turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(SPEED)
    t.pensize(10)
    t.pencolor(COLORS[0])
    t.fillcolor(COLORS[0])

    # Draw the main head circle
    t.penup()
    t.goto(0, -150)  # Position for the head
    t.pendown()
    t.begin_fill()
    t.circle(150)
    t.end_fill()

    t.fillcolor(COLORS[1])
    t.pencolor(COLORS[1])

    # Draw the left eye
    t.penup()
    t.goto(-60, 20)  # Position for the left eye
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    # Draw the left eye
    t.penup()
    t.goto(60, 20)  # Position for the left eye
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    # Draw the smile
    t.penup()
    t.goto(-70, -40)  # Adjusted position for the smile
    t.setheading(-60)  # Set the initial angle
    t.pendown()
    t.circle(80, 120)  # Draw the arc for the smile

    # Update and display the drawing
    turtle.update()

def clear_art():
    turtle.clearscreen()
    turtle.bgcolor('white')

def add_color(color):
    global COLORS
    COLORS.append(color)

def reset_COLORS():
    global COLORS
    COLORS = []

type = 'none'

def setType(design):
    global type
    type = design

def action():
    pop.destroy()

def clicker(t, c):
    global pop
    pop = Toplevel(window)
    x_position = 450
    y_position = 300
    pop.geometry(f"300x100+{x_position}+{y_position}")
    pop.title(t)
    pop.geometry("250x150")
    pop.config(bg="#E0C3FF")
    pop.iconbitmap(r"C:\Users\aakar\Documents\1 UIC\DES Courses\DES 355 DESIGN SEMINAR\Personal Project\project files\assets\genart.ico")

    pop_copy = Label(pop, text=c, bg="#E0C3FF", fg="#401172", font=("Johnston ITC Std Medium", 15 * -1))
    pop_copy.pack(pady=20)

    frame = Frame(pop, bg="#E0C3FF")
    frame.pack(pady=10)

    okay_btn = Button(frame, text="Okay", command=lambda: action(), bg="#2D035B", fg='white')
    okay_btn.grid(row=0, column=0)

def generateArt(type):
    if type == 'none':
        clicker("Select Design", "Select a design to create!")
    if type == 'spiral':
        if len(COLORS) == 0 or len(COLORS) < 2:
            clicker("Spiral Shell", "Pick at least 2 colors for this design\nYour current color(s): " + str(len(COLORS)))
        else:
            spiral()
    elif type == 'flower':
        if len(COLORS) == 0 or len(COLORS) < 6:
            clicker("Flower", "Pick 6 colors for this design\nYour current color(s): " + str(len(COLORS)))
        else:
            flower()
    elif type == 'de stijl':
        if len(COLORS) == 0 or len(COLORS) < 3:
            clicker("De Stijl", "Pick 4 colors for this design\nYour current color(s): " + str(len(COLORS)) + "\nTip: Choose within white, red, blue, and yellow!")
        else:
            destijl()
    elif type == 'circles':
        if len(COLORS) == 0 or len(COLORS) < 3:
            clicker("Circle Pattern", "Pick 3 colors for this design\nYour current color(s): " + str(len(COLORS)))
        else:
            circles()
    elif type == 'mickey':
        if len(COLORS) == 0 or len(COLORS) < 1:
            clicker("Circle Pattern", "Pick 1 color for this design\nYour current color(s): " + str(len(COLORS)))
        else:
            mickey()
    elif type == 'smile':
        if len(COLORS) == 0 or len(COLORS) < 2:
            clicker("Smile", "Pick 2 color for this design\nYour current color(s): " + str(len(COLORS)))
        else:
            smile()
    else:
        print("Error")

def choose_background():
    global bgcolor
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose Background Color")
    bgcolor = (color_code[1])

def choose_colors():
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose Color(s)")
    add_color(color_code[1])

def skip_to_art():
    turtle.tracer(0,0)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\aakar\Documents\1 UIC\DES Courses\DES 355 DESIGN SEMINAR\Personal Project\project files\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# GUI Starts Here
# Credits: https://github.com/ParthJadhav/Tkinter-Designer

window = Tk()

window.geometry("1000x600")
window.configure(bg = "#FFFFFF")
window.title('Generative Art Engine')
window.iconbitmap(r"C:\Users\aakar\Documents\1 UIC\DES Courses\DES 355 DESIGN SEMINAR\Personal Project\project files\assets\genart.ico")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    103.26277160644531,
    1000.0,
    520.3310699462891,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: setType('smile'),
    relief="flat"
)
button_1.place(
    x=832.8115844726562,
    y=167.974609375,
    width=134.97943115234375,
    height=163.30599975585938
)

button_image_hover_1 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

def button_1_hover(e):
    button_1.config(
        image=button_image_hover_1
    )
def button_1_leave(e):
    button_1.config(
        image=button_image_1
    )

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: setType('mickey'),
    relief="flat"
)
button_2.place(
    x=672.6910400390625,
    y=167.974609375,
    width=134.97943115234375,
    height=163.30599975585938
)

button_image_hover_2 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

def button_2_hover(e):
    button_2.config(
        image=button_image_hover_2
    )
def button_2_leave(e):
    button_2.config(
        image=button_image_2
    )

button_2.bind('<Enter>', button_2_hover)
button_2.bind('<Leave>', button_2_leave)


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: setType('circles'),
    relief="flat"
)
button_3.place(
    x=512.5704345703125,
    y=167.974609375,
    width=134.97955322265625,
    height=163.30599975585938
)

button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

def button_3_hover(e):
    button_3.config(
        image=button_image_hover_3
    )
def button_3_leave(e):
    button_3.config(
        image=button_image_3
    )

button_3.bind('<Enter>', button_3_hover)
button_3.bind('<Leave>', button_3_leave)


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: setType('de stijl'),
    relief="flat"
)
button_4.place(
    x=352.4501953125,
    y=167.97454833984375,
    width=134.97943115234375,
    height=163.30599975585938
)

button_image_hover_4 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

def button_4_hover(e):
    button_4.config(
        image=button_image_hover_4
    )
def button_4_leave(e):
    button_4.config(
        image=button_image_4
    )

button_4.bind('<Enter>', button_4_hover)
button_4.bind('<Leave>', button_4_leave)


button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: setType('flower'),
    relief="flat"
)
button_5.place(
    x=192.32955932617188,
    y=167.97454833984375,
    width=134.97943115234375,
    height=163.30599975585938
)

button_image_hover_5 = PhotoImage(
    file=relative_to_assets("button_hover_5.png"))

def button_5_hover(e):
    button_5.config(
        image=button_image_hover_5
    )
def button_5_leave(e):
    button_5.config(
        image=button_image_5
    )

button_5.bind('<Enter>', button_5_hover)
button_5.bind('<Leave>', button_5_leave)


button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: setType('spiral'),
    relief="flat"
)
button_6.place(
    x=32.208953857421875,
    y=167.97454833984375,
    width=134.97943115234375,
    height=163.30599975585938
)

button_image_hover_6 = PhotoImage(
    file=relative_to_assets("button_hover_6.png"))

def button_6_hover(e):
    button_6.config(
        image=button_image_hover_6
    )
def button_6_leave(e):
    button_6.config(
        image=button_image_6
    )

button_6.bind('<Enter>', button_6_hover)
button_6.bind('<Leave>', button_6_leave)


button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: skip_to_art(),
    relief="flat"
)
button_7.place(
    x=849.6825561523438,
    y=386.8802795410156,
    width=118.10848999023438,
    height=78.7389907836914
)

button_image_hover_7 = PhotoImage(
    file=relative_to_assets("button_hover_7.png"))

def button_7_hover(e):
    button_7.config(
        image=button_image_hover_7
    )
def button_7_leave(e):
    button_7.config(
        image=button_image_7
    )

button_7.bind('<Enter>', button_7_hover)
button_7.bind('<Leave>', button_7_leave)


button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clear_art(),
    relief="flat"
)
button_8.place(
    x=686.1878662109375,
    y=386.8802795410156,
    width=118.10848999023438,
    height=78.7389907836914
)

button_image_hover_8 = PhotoImage(
    file=relative_to_assets("button_hover_8.png"))

def button_8_hover(e):
    button_8.config(
        image=button_image_hover_8
    )
def button_8_leave(e):
    button_8.config(
        image=button_image_8
    )

button_8.bind('<Enter>', button_8_hover)
button_8.bind('<Leave>', button_8_leave)


button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generateArt(type),
    relief="flat"
)
button_9.place(
    x=522.6931762695312,
    y=386.8802795410156,
    width=118.10848999023438,
    height=78.7389907836914
)

button_image_hover_9 = PhotoImage(
    file=relative_to_assets("button_hover_9.png"))

def button_9_hover(e):
    button_9.config(
        image=button_image_hover_9
    )
def button_9_leave(e):
    button_9.config(
        image=button_image_9
    )

button_9.bind('<Enter>', button_9_hover)
button_9.bind('<Leave>', button_9_leave)


button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choose_colors(),
    relief="flat"
)
button_10.place(
    x=359.1983947753906,
    y=386.8802795410156,
    width=118.10848999023438,
    height=78.7389907836914
)

button_image_hover_10 = PhotoImage(
    file=relative_to_assets("button_hover_10.png"))

def button_10_hover(e):
    button_10.config(
        image=button_image_hover_10
    )
def button_10_leave(e):
    button_10.config(
        image=button_image_10
    )

button_10.bind('<Enter>', button_10_hover)
button_10.bind('<Leave>', button_10_leave)


button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choose_background(),
    relief="flat"
)
button_11.place(
    x=195.70367431640625,
    y=386.8802795410156,
    width=118.10848999023438,
    height=78.7389907836914
)

button_image_hover_11 = PhotoImage(
    file=relative_to_assets("button_hover_11.png"))

def button_11_hover(e):
    button_11.config(
        image=button_image_hover_11
    )
def button_11_leave(e):
    button_11.config(
        image=button_image_11
    )

button_11.bind('<Enter>', button_11_hover)
button_11.bind('<Leave>', button_11_leave)


button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: reset_COLORS(),
    relief="flat"
)
button_12.place(
    x=32.208953857421875,
    y=386.8802795410156,
    width=118.10848999023438,
    height=78.7389907836914
)

button_image_hover_12 = PhotoImage(
    file=relative_to_assets("button_hover_12.png"))

def button_12_hover(e):
    button_12.config(
        image=button_image_hover_12
    )
def button_12_leave(e):
    button_12.config(
        image=button_image_12
    )

button_12.bind('<Enter>', button_12_hover)
button_12.bind('<Leave>', button_12_leave)


canvas.create_rectangle(
    0.0,
    0.0,
    1000.0,
    103.26277160644531,
    fill="#E0C3FF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    59.91056823730469,
    51.62800598144531,
    image=image_image_1
)

canvas.create_text(
    560,
    37.831390380859375,
    anchor="nw",
    text="GENERATIVE ART ENGINE",
    fill="#3F1171",
    font=("MADE Evolve Sans EVO", 35 * -1)
)

canvas.create_rectangle(
    0.0,
    520.3310546875,
    1000.0,
    599.9999847412109,
    fill="#E0C3FF",
    outline="")

canvas.create_text(
    222.112060546875,
    550.7810668945312,
    anchor="nw",
    text="Select a design, customize it with colors, and generate!",
    fill="#2D025A",
    font=("Johnston ITC Std Medium", 20 * -1)
)
window.resizable(False, False)
window.mainloop()