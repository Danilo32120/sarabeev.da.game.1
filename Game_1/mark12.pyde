f = 0.4
overButton = False
overButton2 = False
x = 0
y = 0
r = 0
g = 0
b = 0
cX = []
cY = []
sqor = 0
a1 = True


def drawType(x):
    #ОТРИСОВКА КНОПКИ
    fill(255);
    text("Start game", x, 304);
    noFill()
    stroke(255)
    noFill()
    rect(425, 270, 150, 50);


def setup():
    size(1000, 700)

    printArray(PFont.list())
    f = createFont("Georgia", 24)
    textFont(f)

    global img, img2
    img = loadImage("car.jpg")
    img2 = loadImage("boy.jpg") 

def draw():
    global cX, cY, r, g, b, sqop
    if a1 == True:
        image(img2, 0, 0) 
        img2.loadPixels()
        textAlign(CENTER)
        drawType(width * 0.5)
    if a1 == False:

        for i in range(1):
            
            y = int(40 + random(img.width)) 
            x = int(150 + random(img.height))
            cX.append(x)
            cY.append(y)
            #цвета кругов
            r = random(255)
            g = random(255)
            b = random(255)
            pix = img.get(x, y)
            fill(pix, 128)
            noStroke()
            ellipse(x, y, 30, 30)
            global f
            f = f + 0.02
            frameRate(f)
            fill(255)
            rect(0, 0, 80, 40)
            fill(0)
            text(str(sqor), 20, 20)

def mousePressed():
    global sqor, a1
    #нажатие на кнопку
    if overButton2:
        a1  = False
        background(255)
    for i in range(len(cX)):
        if checkButtons(i):
            noStroke()
            fill(255)
            ellipse(cX[i], cY[i], 32, 32)
            sqor = sqor + 1


def mouseMoved():
    checkButtons2()


def mouseDragged():
    checkButtons2()


def checkButtons(ind):
    global overButton, cX, cY
    return cX[ind] - 15 < mouseX < cX[ind] + 15 and cY[ind] - 15 < mouseY < cY[ind] + 15;
    
    
def checkButtons2():
    global overButton2
    overButton2 = 425 < mouseX < 575 and 270 < mouseY < 320;

    
    
