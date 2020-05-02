Filling in the Gaps is a project using the os and shutile modules of python.  It will take a given folder (absolute location) and a given prefix, and number the files begining with the prefix.  If numbering already exists but there are gaps it will fill in those gaps.

eg.  FOLDER
        >example001.txt
        >example003.txt
        >example005.txt 

    becomes

    FOLDER
        >example001.txt
        >example002.txt (formerly example003.txt)
        >example003.txt (formerly example005.txt)

Requirements:

python 3

Instructions:

1.Download the git repo
2.Note the example folder
3.open the terminal and cd into the repo directory
4.run chmod +x fillingInTheGaps.py in the command line
5.run ./fillingInTheGaos.py
6.Note the example folder