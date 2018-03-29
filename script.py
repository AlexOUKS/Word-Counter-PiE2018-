import sys
import re

# Count number of characters
def count_carac(file):
    f = open(file, "r")
    length = len(f.read())
    f.close()
    return length

# Count number of words
def count_words(file):
     f = open(file, "r")
     ch = f.read()
     f.close()
     return len(re.findall("\S+",ch))

# Count number of lines
def count_lines(file):
    f = open(file, "r")
    ch = f.read()
    lines = len(re.findall('[\r\n]+', ch))
    f.close()
    if (ch == ""):
        return 0
    elif (lines == 0):
        return 1
    else:
        return lines


# Validation of inputs
if 1 < len(sys.argv):
    f = sys.argv[1]
    try:
        file = open(f, "r")
    except:
        print("No file existing with this name : "+f)
    else:
        print("Number of characters : " + str(count_carac(f)))
        print("Number of words : " + str(count_words(f)))
        print("Number of lines : " + str(count_lines(f)))

else:
    print("Put your file name as an argument")





