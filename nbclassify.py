import glob,os
import re, math

newDict = {}

with open('/Users/umanggala/desktop/courses/nlp/code/nboutput.txt') as f:

    probability_spam = f.readline()
    probability_ham = f.readline()

    for line in f:
        splitLine = line.split()
        #if(splitLine[0] != ' '):
        newDict[splitLine[0]] = [splitLine[1], splitLine[2]]

for root, subdirs, files in os.walk("/Users/umanggala/desktop/courses/nlp/code/dev"):
    if (os.path.basename(os.path.normpath(root)) == "spam1"):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            with open(file, "r", encoding="latin1") as f1:

                probability_spam_given_text = 0
                probability_ham_given_text = 0

                for line in f1:
                    line = ''.join(line.splitlines())

                    for word in line.split():
                        word = re.sub('[^\w]', '', word)
                        #list.append(word)
                        for word in newDict:
                            probability_spam_given_text = probability_spam_given_text + math.log(float(newDict.get(word)[0]))
                            probability_ham_given_text = probability_ham_given_text + math.log(float(newDict.get(word)[1]))

            spam_pro = probability_spam_given_text * float(probability_spam)
            ham_pro = probability_ham_given_text * float(probability_ham)

            if(spam_pro > ham_pro):
                print("Spam")
            else:
                print("Ham")





