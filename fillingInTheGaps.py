#! /Users/stephenlang/anaconda/bin/python
# fillingInTheGaps.py - finds all files with a given prefix eg spam001.txt, spam002.txt
# in a given folder and locates any gaps in the numbering eg spam001.txt, spam003.txt,
# but no spam002.txt, it then renames the files to fill in those gaps

import re, os, shutil

def fillInTheGaps(folder, prefix):
    allfiles = os.listdir(folder)
    print(allfiles)
    allfiles.sort()
    print(allfiles)
    #create a regex using the prefix
    prefixRegex = re.compile( r'(%s)(\d*)(.*)' %(prefix))
    print(prefixRegex)
    
    
    i = 1
    #loop through each file in the folder
    for filename in allfiles: 
            print('filename: '+ filename)
            mo = prefixRegex.search(filename)
            
            print('mo: '+ mo.group())
            print('mo(1): '+ str(mo.group(1)))
            print('mo(2): '+ str(mo.group(2)))
            print('mo(3): '+ str(mo.group(3)))
            
            #case when the file isn't part of the sequence
            if mo == None:
                continue

            #make the ordered file name
            newfilename = mo.group(1) + str(i).zfill(3) + mo.group(3)
            print('newfilename: '+ newfilename)

            

            source = os.path.join(folder, filename)
            destination = os.path.join(folder, newfilename)

            shutil.move(source, destination)

            i += 1
            
fillInTheGaps(os.path.abspath(os.path.join('.','Example')),'spam')
