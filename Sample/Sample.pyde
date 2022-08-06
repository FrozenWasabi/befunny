from Images import loadImageNames
from Images import loadImages

'''
#Function to check which rectangle bounds mouse clicked on
def mouseReleased(): #FOR RECTANGLES
    global allBoundaries, whichBoundary, numBoundaries

    validLocation = False
    for i in range(numBoundaries):        
        validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
        validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
        validLocation = validXRange and validYRange
        if validLocation:
            whichBoundary = i
            break

#Function to check which circle bounds mouse clicked on
def mousePressed(): #FOR CIRCLES
    global circleBoundaries, whichCircle, numCircles

    for i in range(numCircles):
        if circleBoundaries[i]:
            circleX = circleBoundaries[i][0]
            circleY = circleBoundaries[i][1]
            circleW = circleBoundaries[i][2]
            circleH = circleBoundaries[i][3]
            circleR = circleW/2
            
            parendicularX = abs(mouseX - circleX)
            baseY = abs(mouseY - circleY)
            
            #Checks the radius distance between mouse and center of circle
            if (math.hypot(parendicularX, baseY) <= circleR):
                whichCircle = i
                break

#Function to check which key is released
def keyReleased():
    global whichKey, asciList, controlKeys     
    global Keys, boolKeys, selectKey
    
    #Regular key entering code
    if key == CODED:
       if keyCode in controlKeys:
        whichKey = keyCode
    elif key in asciList:
        whichKey = key
    else:
        whichKey = ''
    
    #Makes 2 keys pressed at the same time possible
    if key != CODED:
        selectKey = key.upper()
    else:
        selectKey = keyCode
    
    for i in range(len(boolKeys)):
        if selectKey == Keys[i]:
            boolKeys[i] = False

#Function to check which key is pressed
def keyPressed():
    global Keys, boolKeys, selectKey
    
    #Makes 2 keys pressed at the same time possible
    if key != CODED:
        selectKey = key.upper()
    else:
        selectKey = keyCode

    for i in range(len(boolKeys)):
        if selectKey == Keys[i]:
            boolKeys[i] = True
'''


def setup():
    global imageList, imageListNames, fileName, screen, homeBounds, textBounds
    
    size(540,960)
    
    screen = 1
    
    #Image File Reader
    fileName = "ImageNames.txt"
    imageListNames = loadImageNames(fileName)
    imageList = loadImages(imageListNames)
    
    homeBounds = []
    homeY = 480
    homeW = 0
    
    textBounds = [[[26, 26], [66, 66]]]
    textY = 642
    textW = 0
    
    for i in range(3):
        homeY = 480 + homeW + 37*i
        textY = 642 + textW + 22*i
        
        homeBounds.append([[84, homeY], [458, 96+homeY]])
        textBounds.append([[60, textY], [480, 70+textY]])
        
        
        homeW += 96
        textW += 70
    print(homeBounds)
    print(textBounds)    
    
    image(imageList[0], 0, 0)

def draw():
    global imageList, imageListNames, fileName, screen, homeBounds, textBounds
    
    if screen == 0:
        image(imageList[0], 0, 0)
        
        fill(255, 100)
        for i in range(len(homeBounds)):
            rect(homeBounds[i][0][0], homeBounds[i][0][1], homeBounds[i][1][0]-homeBounds[i][0][0], homeBounds[i][1][1]-homeBounds[i][0][1])
        
    elif screen == 1:
        image(imageList[1], 0, 0)
        fill(255, 100)
        for i in range(len(textBounds)):
            rect(textBounds[i][0][0], textBounds[i][0][1], textBounds[i][1][0]-textBounds[i][0][0], textBounds[i][1][1]-textBounds[i][0][1])

def mousePressed():
    global screen
    
    if mouseX >= 83 and mouseX <= 456 and mouseY >= 480 and mouseY <= 576:
        screen = 1
        println("clicked")
    elif mouseX >= 26 and mouseX <=66 and mouseY >= 26 and mouseY <= 66:
        screen = 0
