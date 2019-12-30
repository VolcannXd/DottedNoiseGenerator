import noiseManager

class noiseFile :
    def __init__(self, noise, infos) :
        self.noise = noise
        self.infos = infos

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
    f.read()

    fl = f.split('\n')
    mode = 'None'
    for i in range(0, len(fl)) :
        line = fl[i]

        if line[0] == ':' or line == '\n' :
            if line[1:] == 'PREFS' :
                mode = 'prefs'
            elif line[1:] == 'INFOS' :
                mode = 'infos'
            elif line[1:] == 'POINTS' :
                mode = 'points'
            else :
                mode = 'unknown'

        else :
            content = line.split(' ')
            if mode == 'prefs' :
                pass
            elif mode == 'infos' :
                pass
            elif mode == 'points' :
                pass
            else :
                pass
