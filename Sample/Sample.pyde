from Images import loadImageNames
from Images import loadImages

def setup():
    global imageList, imageListNames, fileName, screen, homeBounds, textBounds
    global allBoundaries, whichBoundary, numBoundaries
    
    size(540,960)
    
    screen = 1
    
    #Image File Reader
    fileName = "ImageNames.txt"
    imageListNames = loadImageNames(fileName)
    imageList = loadImages(imageListNames)
    
    imageList[2].resize(435, 60)
    imageList[3].resize(435, 60)
    
    allBoundaries = []
    whichBoundary = -1
    numBoundaries = len(allBoundaries)
    
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
    global allBoundaries, whichBoundary, numBoundaries
    
    if screen == 0:
        image(imageList[0], 0, 0)
        
        allBoundaries = homeBounds
        
        if whichBoundary == 0:
            screen = 1
        elif whichBoundary == 1:
            print("INFO")
        elif whichBoundary == 2:
            delay(250)
            exit()
        
        fill(255, 100)
        for i in range(len(homeBounds)):
            rect(homeBounds[i][0][0], homeBounds[i][0][1], homeBounds[i][1][0]-homeBounds[i][0][0], homeBounds[i][1][1]-homeBounds[i][0][1])
        
    elif screen == 1:
        image(imageList[1], 0, 0)
        
        allBoundaries = textBounds
        
        if whichBoundary == 0:
            screen = 0
        elif whichBoundary == 1:
            print("Option 1")
        elif whichBoundary == 2:
            print("Option 2")
        elif whichBoundary == 3:
            print("Option 3")
        
        
        
        fill(255, 100)
        for i in range(len(textBounds)):
            rect(textBounds[i][0][0], textBounds[i][0][1], textBounds[i][1][0]-textBounds[i][0][0], textBounds[i][1][1]-textBounds[i][0][1])
        
        #Person A (Pink Bubbles)
        image(imageList[2], 40, 110)
        rect(108, 112 + 160*0, 361, 55)
        
        image(imageList[2], 40, 270)
        rect(108, 112 + 160*1, 361, 55)
        
        image(imageList[2], 40, 430)
        rect(108, 112 + 160*2, 361, 55)

        
        #Person B(Green Bubbles)
        image(imageList[3], 65, 190)
        rect(70, 192 + 160*0, 361, 55)
        
        image(imageList[3], 65, 350)
        rect(70, 192 + 160*1, 361, 55)

    whichBoundary = -1

def mouseReleased(): #FOR RECTANGLES
    global allBoundaries, whichBoundary, numBoundaries

    validLocation = False
    for i in range(len(allBoundaries)):        
        validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
        validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
        validLocation = validXRange and validYRange
        if validLocation:
            whichBoundary = i
            break
