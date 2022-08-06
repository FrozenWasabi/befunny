def setup():
    size(540,960)
    
def draw():

    img = loadImage('Simp.png')
    image(img, 0, 0)
    
    rect(83, 480, 373, 96)
    
def mousePressed():
    if mouseX >= 83 and mouseX <= 456 and mouseY >= 480 and mouseY <= 576:
        println("clicked")
        
        
#test
    
    
