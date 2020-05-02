#! /Users/stephenlang/anaconda/bin/python
# fillingInTheGaps.py - finds all files with a given prefix eg spam001.txt, spam002.txt
# in a given folder and locates any gaps in the numbering eg spam001.txt, spam003.txt,
# but no spam002.txt, it then renames the files to fill in those gaps

import re, os

def fillInTheGaps(folder, prefix):

    #create a regex using the prefix
    prefixRegex = re.compile( r'(%s)(/d*)(.?)' %(prefix))

    allfiles = os.listdir(folder).sort()

    #loop through each file in the folder
    for filename in allfiles:
   
            mo = prefixRegex.search(filename)
            #move on if there is no match
            if mo == None:
                continue
    
            newfilename = mo.group(1) + str(i) + mo.group(3)

    #have an integer variable starting at 1
    #for each file compare the prefix to the regex
    #if it matches add the integer var to the end and increment the integer