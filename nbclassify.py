import glob,os
import re, math

newDict = {}

with open('/Users/umanggala/desktop/courses/nlp/code/nbmodel.txt') as f:

    probability_spam = f.readline()
    probability_ham = f.readline()

    for line in f:
        splitLine = line.split()
        #if(splitLine[0] != ' '):
        newDict[splitLine[0]] = [splitLine[1], splitLine[2]]

target = open("/Users/umanggala/desktop/courses/nlp/code/nboutput.txt", 'w')
classified_correct_spam = 0
classified_incorrect_spam = 0
classified_correct_ham = 0
classified_incorrect_ham = 0
total_files = 0
classified_as_spam = 0
classified_as_ham = 0

for root, subdirs, files in os.walk("/Users/umanggala/desktop/courses/nlp/code/dev/testdemo"):
    #if (os.path.basename(os.path.normpath(root)) == "spam1" || os.path.basename(os.path.normpath(root)) == 'ham1' ):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            with open(file, "r", encoding="latin1") as f1:

                probability_spam_given_text = 0
                probability_ham_given_text = 0

                for line in f1:
                    line = ''.join(line.splitlines())

                    for word in line.split():
                        #word = re.sub('[^\w]', '', word)
                        #list.append(word)
                        if word in newDict:
                            probability_spam_given_text = probability_spam_given_text + math.log(float(newDict.get(word)[0]))
                            probability_ham_given_text = probability_ham_given_text + math.log(float(newDict.get(word)[1]))

                #print(probability_spam_given_text)
                #print(probability_ham_given_text)

                spam_pro = probability_spam_given_text + math.log(float(probability_spam))
                ham_pro = probability_ham_given_text + math.log(float(probability_ham))

                total_files = total_files + 1

                if(spam_pro > ham_pro):

                    target.write("Spam")
                    classified_as_spam = classified_as_spam + 1
                    if(os.path.basename(os.path.normpath(root)) == "spam1"):

                        classified_correct_spam = classified_correct_spam + 1
                    else:
                        classified_incorrect_spam = classified_incorrect_spam + 1

                else:
                    target.write("Ham")
                    classified_as_ham = classified_as_ham + 1
                    if (os.path.basename(os.path.normpath(root)) == "ham1"):
                        classified_correct_ham = classified_correct_ham + 1
                    else:
                        classified_incorrect_ham = classified_incorrect_ham + 1

                target.write("\t")
                target.write(root + "/" + file)
                target.write("\n")

precision_spam = classified_correct_spam / classified_as_spam
precision_ham = classified_correct_ham / classified_as_ham

print(precision_spam)
print(precision_ham)



target.close()





