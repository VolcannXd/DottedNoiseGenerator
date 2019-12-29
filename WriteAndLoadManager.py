def load(filename) :
    infos = []
    f = open(filename, "r")
    fl = f.read()

    infos = fl.split(' ')

    return infos

def loadNoise(filename) :
    prefs = []
    infos = []
    points = []

    f = open(filename, "r")