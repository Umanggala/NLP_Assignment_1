import sys

filename = sys.argv[-1]

newDict = {}

'''
def StemWords(line_stop_words):
    leaf_words = "s","es","ed","er","ly","ing"
    i=0
    while i < 6:
        count = 0
        length = len(leaf_words[i])
        while count < len(line_stop_words):
            line = line_stop_words[count]
            count2 = 0
            while count2 < len(line):
                #line is the particular list(or line) that we are dealing with, count if the specific word
                if leaf_words[i] == line[count2][-length:]:
                    line[count2] = line[count2][:-length]
                count2 += 1
            line_stop_words[count] = line
            count2 = 0
            count += 1
        count = 0
        i += 1
    return(line_stop_words)
'''
stopwords = []
with open(filename + "/stopwords.txt") as f1:
    for line in f1:
        for word in line.split():
            stopwords.append(word)

with open(filename + '/nbmodel1.txt') as f:

    probability_spam = f.readline()
    probability_ham = f.readline()

    for line in f:
        splitLine = line.split()
        #if(splitLine[0] != ' '):
        newDict[splitLine[0]] = [splitLine[1], splitLine[2]]

    for word in stopwords:
        if word in newDict:
            del newDict[word]

print(stopwords)

