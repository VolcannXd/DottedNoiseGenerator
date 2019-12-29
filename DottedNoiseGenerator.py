import random
import math
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog

class Vec2 :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

class Pixel :
    def __init__(self, pos, brightness) :
        self.pos = pos
        self.brightness = brightness

class perlinNoise :
    def __init__(self, size, points, scale, threshold) :
        self.size = size
        self.points = points
        self.scale = scale
        self.threshold = threshold

class noisePixelMap :
    def __init__(self, pixels) :
        self.pixels = pixels

def generate_points(noise) :
    points_temps = []
    for i in range(noise.scale) :
        points_temps.append(Vec2(random.randint(0, noise.size), random.randint(0, noise.size)))

    return points_temps

def generateNoiseMap(noiseParameters) :
    points = generate_points(noiseParameters)

    pixels = []

    for x in range(0, noiseParameters.size) :
        for y in range(0, noiseParameters.size) :
            index = (y * noiseParameters.size) + x
            pixels.append(Pixel(Vec2(x, y), 255))

    return noisePixelMap(pixels)

def hexToRGB(rgb) :
    return "#%02x%02x%02x" % rgb

def drawNoise(canvas) :
    noise = perlinNoise(512, [], 10)
    pixels = generateNoiseMap(noise)

    for y in range(0, noise.size) :
        for x in range(0, noise.size) :
            index = (y * noise.size) + x
            canvas.create_rectangle( (x, y)*2, fill=hexToRGB((255, 255, 255)))

def frame() :
    root = Tk()
    root.title("Dotted noise generator")

    # MENU BAR
    menubar = Menu(root)

    # FILE MENU
    menuFile = Menu(menubar, tearoff=0)
    menuFile.add_command(label="New")
    menuFile.add_command(label="Open")
    menuFile.add_command(label="Save")
    menuFile.add_separator()
    menuFile.add_command(label="Quit", command=root.destroy)
    
    # HELP MENU
    menuHelp = Menu(menubar, tearoff = 0)
    menuHelp.add_command(label="About", command=about)
    menuHelp.add_command(label="Help")

    # SETUP MENUS
    menubar.add_cascade(label="File", menu=menuFile)
    menubar.add_cascade(label="Help", menu=menuHelp)
    root.config(menu=menubar)

    #   CANVAS
    canvasToDraw = Canvas(root, width = 512, height = 512, bg = 'black')
    canvasToDraw.pack(padx =5, pady =5)

    # GUI - BUTTON
    quitButton = Button(root, text = "Quit", command=root.destroy)
    quitButton.pack(side = LEFT, padx = 5, pady = 5)

    generateButton = Button(root, text = "Generate Noise")
    generateButton.pack(side = RIGHT, padx = 5, pady = 5)

    root.mainloop()

def about() :
    tkinter.messagebox.showinfo("A propos","Test of a dotted noise generator\nA dotted noise generator is a new type of generator wich color pixels from near random positions called dots\n(C) Arthur Detaille - 2020\n\narthurdetaille.pro@gmail.com")

frame()