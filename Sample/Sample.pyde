from Images import loadImageNames
from Images import loadImages
add_library('minim')
minim = Minim(this)

def setup():
    global imageList, imageListNames, fileName 
    global screen, homeBounds, textBounds, textA, textB, textANum, textBNum, textPast, textOrder
    global allBoundaries, whichBoundary, numBoundaries
    global scrollNum
    global bubbleX, bubbleY, textBubble
    global musicbackground
    
    size(540,960)
    
    musicbackground = minim.loadFile("music.mp3")
    musicbackground.loop()
    
    screen = 0
    scrollNum = 0
    
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
    
    textANum = 1
    textBNum = 0
    
    textA = [["Hi, how are you?"],
             ["I\'m doing fantastic! I\'m glad to have someone to talk to today.","... Pardon? Love your enthusiasm","Oh... that doesn\'t go with the spirit of the website."],
             ["I love to travel is there anything you want to visit"],
             ["Oh yes I have, the atmosphere was lovely.","I see... ","Well it\'s never too late to start"],
             ["I love them! They\'re so adorable and fluffy.","sorry? I\'m not comfortable answering that...","Are you there? It\'s not very polite to leave people on read."],
             ["I see...","Yeah, we have so much in common","Hmm, you don\'t see that interested"],
             ["What\'s your favourite genre of books or tv shows?"],
             ["Eh? That\'s kinda off-putting..."," mhm fantasy allows for new possibilities just like scifi my favourite.","huh sorry that was random"],
             ["Its pretty rainy today","... i see bye","You forgot who I am? I wasn\'t important enough? I see"],
             ["Out of curiosity, what\'s your favourite food?"],
             ["hm you might what to avoid that","Good to know. You favourite food tho?","oh yess that is delicious especially when it\'s fresh."]]
             
    textB = [["Great! What about you?"," Yaaa I know righttt","I don\'t talk to strangers."],
             ["I\'ve always dreamed of visiting Paris to see the Eiffel Tower. Have you been before? ","Traveling is so boring, there\'s no way you enjoy it.","I haven\'t really thought about it."],
             ["Do you like dogs?","Where do you live?","..."],
             ["I hate em","Mhm I totally agree. They\'re soo cute","Ya"],
             ["Horror, i like to watch people die..."," I love fantasy it allows you to imagine a whole new whole.","Have you been fishing?"],
             ["How\'s the weather today?","Don\'t talk to me","Who are you again?"],
             ["Definitely battery acid you should try sometime","I like to sleep","Mm sushi is by far my favourite. "]]
    
    textOrder = [1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1]
    #If textOrder[6] option/whichBoundary == 1, append [2] into textOrder[8]
    
    bubbleX = 40
    bubbleY = 430
    
    textPast = [textA[0][0]]
    textBubble = imageList[2]
    
    image(imageList[0], 0, 0)

def draw():
    global imageList, imageListNames, fileName 
    global screen, homeBounds, textBounds, textA, textB, textANum, textBNum, textPast, textOrder
    global allBoundaries, whichBoundary, numBoundaries
    global scrollNum
    global bubbleX, bubbleY, textBubble
    
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
        print(textPast)
        print(textOrder, textANum + textBNum)
        
        if whichBoundary == 0:
            screen = 0
        elif whichBoundary == 1 or whichBoundary == 2 or whichBoundary == 3:
            
            if textOrder[textANum + textBNum] == 2:
                if whichBoundary == 1:
                    print("Option 1")
                    textPast.append(textB[textBNum][whichBoundary-1])
                    textBNum += 1
                elif whichBoundary == 2:
                    print("Option 2")
                    textPast.append(textB[textBNum][whichBoundary-1])
                    textBNum += 1
                elif whichBoundary == 3:
                    print("Option 3")
                    textPast.append(textB[textBNum][whichBoundary-1])
                    textBNum += 1
            
        
        #if len(textPast) <= 5:
        bubbleY = 430
        for i in range(len(textPast)-1, -1, -1):
        #for i in range(len(textPast)):
            print(i)
            if textOrder[i] == 1:
                bubbleX = 40
                textBubble = imageList[2]
            elif textOrder[i] == 2:
                bubbleX = 65
                textBubble = imageList[3]
            
            
            if bubbleY >= 110:
                delay(500)
                image(textBubble, bubbleX, bubbleY)
                
                fill(0)
                textMode(CENTER)
                textAlign(CENTER)
                textSize(16)
                text(textA[i][0], 218+bubbleX, bubbleY+36)

                bubbleY -= 80

            
            '''
            for i in range(5):
                if (scrollNum >= len(textPast)-5):
                    scrollNum = len(textPast)-5
                elif (scrollNum < 0):
                    scrollNum = 0
                
                bubbleY = 430
            
                print(i)
                if textOrder[i] == 1:
                    bubbleX = 40
                    textBubble = imageList[2]
                elif textOrder[i] == 2:
                    bubbleX = 65
                    textBubble = imageList[3]
                delay(500)
                image(textBubble, bubbleX, bubbleY)
                bubbleY -= 80
               ''' 
        
        
        if textOrder[textANum + textBNum] == 1:
            if len(textA[textANum]) == 3:
                textPast.append(textA[textANum][whichBoundary-1])
            else:
                textPast.append(textA[textANum][0])
            textANum += 1
            
        #Person A (Pink Bubbles)
        #image(imageList[2], 40, 110)
        #rect(108, 112 + 160*0, 361, 55)

        #image(imageList[2], 40, 270)
        #rect(108, 112 + 160*1, 361, 55)
        
        #image(imageList[2], 40, 430)
        #rect(108, 112 + 160*2, 361, 55)

        
        #Person B(Green Bubbles)
        #image(imageList[3], 65, 190)
        #rect(70, 192 + 160*0, 361, 55)
        
        #image(imageList[3], 65, 350)
        #rect(70, 192 + 160*1, 361, 55)
        
        #Person A Text
                
        fill(0)
        #text(textPast[textANum + textBNum - 1], 30, 30)
        
        fill(255)
        textSize(20)
        
        myFont = createFont("Calibri", 20)
        textFont(myFont)
        
        #text(textA[0][0], 128, 112 + 55*3/5)
        #text(textB[0][0], 128 + 50, (112 + 55*3/5) + 80)
        
        for i in range(len(textBounds)):
            #fill(255, 100)
            #rect(textBounds[i][0][0], textBounds[i][0][1], textBounds[i][1][0]-textBounds[i][0][0], textBounds[i][1][1]-textBounds[i][0][1])
            if i != 0:
                fill(255)
                textMode(CENTER)
                text("text", width/2-10, textBounds[i][0][1]+(textBounds[i][1][1]-textBounds[i][0][1])*3/5)
                
    whichBoundary = -1

def mouseReleased(): #FOR RECTANGLES
    global allBoundaries, whichBoundary, numBoundaries
    global sound

    validLocation = False
    for i in range(len(allBoundaries)):        
        validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
        validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
        validLocation = validXRange and validYRange
        if validLocation:
            sound = minim.loadFile("click.mp3")
            sound.play()
            whichBoundary = i
            break
        
#Function to store mouseWheel scroll value
def mouseWheel(event):
    global scrollNum
    scrollNum += event.getCount()
