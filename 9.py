def readText(txtFile):
    NUMBER_OF_WORDS = 0
    NUMBER_OF_LINES = 0
    f = open(txtFile, "r")
    NUMBER_OF_LINES = len(f.readlines())
    f = open(txtFile, "r")
    for lines in f.readlines():
        lines = lines.replace('\n','')
        NUMBER_OF_WORDS  = NUMBER_OF_WORDS + len(lines.split())
    return [NUMBER_OF_WORDS, NUMBER_OF_LINES]


if name=="main":
    print(readText('path/main.txt'))