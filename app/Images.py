#loads all images used

def loadImageNames(fileName):
    
    file = open(fileName)
    fileList = []                 
    text = file.readlines()
     
    for line in text:
        line = line.strip()
        row = ""
        for c in line:
            row = row + c
        rowList = row.split(",")
    file.close
    return (rowList)

def loadImages( imageListNames ):
     
    numImages = len(imageListNames)
    imageList = ["" for i in range(numImages)]
    for i in range( numImages ):
        imageList[i] = loadImage(imageListNames[i])
    return(imageList)
