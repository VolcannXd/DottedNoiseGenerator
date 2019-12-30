import random
import math
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import webbrowser
import WriteAndLoadManager as WLM
import noiseManager

print("Log: random, math, tkinter and webbrowser were imported correctly.")

def generate_points(noise) :
    points_temps = []
    for i in range(noise.scale) :
        points_temps.append(noiseManager.Vec2(random.randint(0, noise.size), random.randint(0, noise.size)))

    return points_temps

def generateNoiseMap(noiseParameters) :
    points = generate_points(noiseParameters)

    pixels = [None] * (512*512)
    print(len(pixels))

    for y in range(0, noiseParameters.size) :
        for x in range(0, noiseParameters.size) :
            index = (y * noiseParameters.size) + x
            color = (255, 255, 255)

            pixels[index] = noiseManager.Pixel(
                noiseManager.Vec2(x, y),
                RgbToHex(color)
            )

    return pixels

def RgbToHex(rgb) :
    # Return Hex value corresponding to the rgb value
    return "#%02x%02x%02x" % rgb

def drawNoise() :
    print("Log: Action: Draw Noise")
    if _canvas != None :
        noise = noiseManager.perlinNoise(
            512,
            [],
            scaleScale.get(),
            thresholdScale.get()
        )

        b_background = int(255 * invertion.get())

        points = generate_points(noise)

        # CLEAR CANVAS
        _canvas.delete("all")
        _canvas.create_rectangle(0, 0, noise.size + 5, noise.size + 5, fill=RgbToHex((b_background, b_background, b_background)))


        for p in points :
            r = noise.threshold
            b = 255 - b_background
            color = RgbToHex((b, b, b))
            _canvas.create_oval(p.x - r, p.y - r, p.x + r, p.y + r, fill=color, outline=color)

        """
        for y in range(0, noise.size) :
            for x in range(0, noise.size) :
                index = (y * noise.size) + x
                b = RgbToHex((255, 255, 255))

                distances = []

                for i in range (0, len(noise.points)) :
                    xD = abs(noise.points[i].x - x)
                    yD = abs(noise.points[i].y - y)
                    
                    distances.append(math.sqrt(xD * xD + yD * yD))

                distance = threshold
                for i in range(0, len(distances)) :
                    distance = distance - distances[i]

                color = (0, 0, 0)
                if distance >= 0 :
                    b = b_background - ((distance / 255) * threshold)
                    color = (b, b, b)

                _canvas.create_rectangle((x, y) * 2, fill = RgbToHex(color))
        """

    else :
        print("err: _canvas type == none type!")

def about() :
    print("Log: Action: infos")
    tkinter.messagebox.showinfo("About","Test of a dotted noise generator\n(C) Arthur Detaille - 2020")

def aboutImage() :
    print("Log: Action: infos")
    tkinter.messagebox.showinfo("About Image","512 x 512 pixels\nno AA")

def help_() :
    print("Log: Action: help")
    webbrowser.open_new("https://github.com/VolcannXd/DottedNoiseGenerator")

def debug() :
    print("Log: debug")

def newFile() :
   prefs =  WLM.load("default-options.pref")
   scaleScale.set(int(prefs[1]))
   thresholdScale.set(int(prefs[2]))

   if prefs[4] == 0 : SeamlessChecker.select()
   else : SeamlessChecker.deselect()

   drawNoise()
    
def loadExampleNoise() :
    print("Log: Action: Load Example Noise")

root = Tk()
root.title("Dotted noise generator")
root.resizable(False, False)
print("Log: Frame has been created.")
# MENU BAR
menubar = Menu(root)

# FILE MENU
menuOpenExamples = Menu(menubar, tearoff = 0)
menuOpenExamples.add_command(label="noiseExample.noise", command=loadExampleNoise)

menuFile = Menu(menubar, tearoff=0)
menuFile.add_command(label="New", command=newFile)
menuFile.add_command(label="Open")
menuFile.add_cascade(label="Open Examples", menu=menuOpenExamples)
menuFile.add_command(label="Save As")
menuFile.add_separator()
menuFile.add_command(label="Quit", command=root.destroy)

# HELP MENU
menuHelp = Menu(menubar, tearoff = 0)
menuHelp.add_command(label="About", command=about)
menuHelp.add_command(label="Help", command=help_)

# IMAGE MENU
menuImage = Menu(menubar, tearoff = 0)
menuImage.add_command(label="About", command=aboutImage)
menuImage.add_command(label="Save Image As")

# SETUP MENUS
menubar.add_cascade(label="File", menu=menuFile)
menubar.add_cascade(label="Help", menu=menuHelp)
menubar.add_cascade(label="Image", menu=menuImage)
root.config(menu=menubar)

print("Log: Menubar has been created and setup.")

# Noise Generation parameters
generationGroup = LabelFrame(root, text="Generation paramters")
generationGroup.pack(side = RIGHT, fill="both", expand="yes", padx = 5, pady = 5)

threshold = IntVar()
thresholdScale = Scale(generationGroup, label="Threshold (in pixel's distance)", orient="horizontal", from_=1, to=500, resolution=1, length=450, variable=threshold)
thresholdScale.pack()

scale = IntVar()
scaleScale = Scale(generationGroup, label="scale", orient="horizontal", from_=1, to=100, resolution=1, length=450, variable=scale)
scaleScale.pack()

invertion = DoubleVar()
invertionScale = Scale(generationGroup, orient="horizontal", label="Brightness Multiplier", from_=0, to=1, resolution=0.01, length=450, variable=invertion)
invertionScale.pack()

isSeamless = IntVar()
SeamlessChecker = Checkbutton(generationGroup, text="seamless noise", variable=isSeamless)
SeamlessChecker.pack(padx = 25, pady = 5)

generateButton = Button(generationGroup, text = "Generate Noise", command=drawNoise)
generateButton.pack(side=BOTTOM, padx = 5, pady = 5)

thresholdScale.set(50)
scaleScale.set(7)

print("Log: generation label Frame has been created and setup.")

#   CANVAS
_canvas = Canvas(root, width = 512, height = 512, bg = 'black')
_canvas.pack(side = LEFT, padx =5, pady =5)

print("Log: Canvas has been created and setup.")

drawNoise()

root.mainloop()