import random
import math
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import webbrowser

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

def generate_points(noise) :
    points_temps = []
    for i in range(noise.scale) :
        points_temps.append(Vec2(random.randint(0, noise.size), random.randint(0, noise.size)))

    return points_temps

def generateNoiseMap(noiseParameters) :
    points = generate_points(noiseParameters)

    pixels = []

    for y in range(0, noiseParameters.size) :
        for x in range(0, noiseParameters.size) :
            index = (y * noiseParameters.size) + x
            pixels.append(Pixel(Vec2(x, y), "white"))

    return pixels

def hexToRGB(rgb) :
    return "#%02x%02x%02x" % rgb

def drawNoise() :
    if _canvas != None :
        noise = perlinNoise(512, [], 10, 15)
        pixels = generateNoiseMap(noise)

        for y in range(0, noise.size) :
            for x in range(0, noise.size) :
                index = (y * noise.size) + x
                b = pixels[index].brightness
                _canvas.create_rectangle(x, y, x, y, fill=b)
    else :
        print("err: _canvas type == none type!")

def about() :
    tkinter.messagebox.showinfo("A propos","Test of a dotted noise generator\n(C) Arthur Detaille - 2020")

def help_() :
    webbrowser.open_new("https://github.com/VolcannXd/DottedNoiseGenerator")

root = Tk()
root.title("Dotted noise generator")
root.resizable(False, False)

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
menuHelp.add_command(label="Help", command=help_)

# SETUP MENUS
menubar.add_cascade(label="File", menu=menuFile)
menubar.add_cascade(label="Help", menu=menuHelp)
root.config(menu=menubar)

# Noise Generation parameters
generationGroup = LabelFrame(root, text="Generation paramters")
generationGroup.pack(side = RIGHT, fill="both", expand="yes", padx = 5, pady = 5)

threshold = IntVar()
thresholdScale = Scale(generationGroup, label="Threshold (in pixel's distance)", orient="horizontal", from_=1, to=500, resolution=1, length=450)
thresholdScale.pack()

scale = IntVar()
scaleScale = Scale(generationGroup, label="scale", orient="horizontal", from_=1, to=100, resolution=1, length=450)
scaleScale.pack()

isInvert = IntVar()
InvertChecker = Checkbutton(generationGroup, text="invert noise", variable=isInvert)
InvertChecker.pack(side=LEFT, padx = 25, pady = 5)

isSeamless = IntVar()
SeamlessChecker = Checkbutton(generationGroup, text="seamless noise", variable=isSeamless)
SeamlessChecker.pack(side=RIGHT, padx = 25, pady = 5)

generateButton = Button(generationGroup, text = "Generate Noise", command=drawNoise)
generateButton.pack(side=BOTTOM, padx = 5, pady = 5)

thresholdScale.set(50)
scaleScale.set(7)

#   CANVAS
_canvas = Canvas(root, width = 512, height = 512, bg = 'black')
_canvas.pack(side = LEFT, padx =5, pady =5)

root.mainloop()