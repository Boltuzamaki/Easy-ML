from pascal_voc_writer import Writer
import re
import os

files = os.listdir('C:\\Users\\boltuzamaki\\Downloads\\PennFudanPed\\Annotation')

for file in files:

    mylines = []                                # Declare an empty list.
    with open (file, 'rt') as myfile:    # Open lorem.txt for reading text.
        for myline in myfile:                   # For each line in the file,
            mylines.append(myline.rstrip('\n')) # strip newline and add to list.
    co_ordinates = []
    for line in mylines:
        length_file = len("filename : ")
        length_cor =  len("(Xmin, Ymin) - (Xmax, Ymax) : ")
        length_dims = len("Image size (X x Y x C) : ")
        if line.find("filename : ") != -1:
            print(line.find("filename : "))
            file = line[length_file + line.find("filename : "):]
        if line.find("Image size (X x Y x C) : ")!=-1:
            size = line[length_dims +line.find("Image size (X x Y x C) : "): ]
        if line.find("(Xmin, Ymin) - (Xmax, Ymax) : ") != -1:
            co_ordinates.append(line[length_cor +line.find("(Xmin, Ymin) - (Xmax, Ymax) : "): ])    
    image = file.split("/")[2]
    height = int(size.split('x')[0])
    width = int(size.split('x')[1])
    #channel = int(size.split('x')[2])
    writer = Writer(image, height, width)
    if len(co_ordinates) > 1:
        for cor in co_ordinates:
            result = re.sub("\(|\)|-","", cor)
            result = re.sub(","," ",result )
            result = re.sub("  "," ", result)
            cordi = result.split()
            xmin = cordi[0]
            ymin = cordi[1]
            xmax = cordi[2]
            ymax = cordi[3]
            writer.addObject('person', xmin, ymin, xmax, ymax)
    if len(co_ordinates) == 1:
         result = re.sub("\(|\)|-","", co_ordinates[0])
         result = re.sub(","," ",result )
         result = re.sub("  "," ", result)
         cordi = result.split()
         xmin = cordi[0]
         ymin = cordi[1]
         xmax = cordi[2]
         ymax = cordi[3]
         writer.addObject('person', xmin, ymin, xmax, ymax)
         
    path = image.split(".")[0] + ".xml"        
    writer.save(path)