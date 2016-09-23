#string = "how much for the maple syrup? $20.99? That's ricidulous!!!"
#string = re.sub('[^\w]', '', string)
#print(string)
#'mississippi'.rstrip('ipz')

import glob, os
import sys, re

filename = sys.argv[-1]

target = open(filename + "/nbmodel1.txt", 'w')

class input_processing:

    global total_count
    total_count = 0

    global count_word_spam
    count_word_spam = 0

    global count_word_ham
    count_word_ham = 0

    def __init__(self,dir,sub_dir):
        self.dir = dir
        self.sub_dir = sub_dir


    def extract_token(self):
        new_dict = {}
        count = 0
        for root, subdirs, files in os.walk(self.dir):
            if(os.path.basename(os.path.normpath(root)) == self.sub_dir):
                os.chdir(root)
                for file in glob.glob("*.txt"):
                    count = count + 1
                    global total_count
                    total_count += 1
                    with open(file, "r", encoding="latin1") as f1:
                        for line in f1:
                            for word in line.strip().split():
                                #word = re.sub('[^\w]', '', word)
                                if word not in new_dict:
                                    new_dict[word] = 1
                                else:
                                    new_dict[word] = new_dict.get(word) + 1

        return new_dict, count


    def calculate_probability(self,new_dict1,new_dict2):

        global count_word_spam
        global count_word_ham

        for words in new_dict2:
            if words not in new_dict1:
                new_dict1[words] = 0

        for words in new_dict1:
            new_dict1[words] = new_dict1.get(words) + 1
            count_word_spam = count_word_spam + new_dict1.get(words)

        #HAM

        for words in new_dict1:
            if words not in new_dict2:
                new_dict2[words] = 0

        for words in new_dict2:
            new_dict2[words] = new_dict2.get(words) + 1
            count_word_ham = count_word_ham + new_dict2.get(words)

        for words in new_dict1:
            new_dict1[words] = new_dict1.get(words) / count_word_spam

        for words in new_dict2:
            new_dict2[words] = new_dict2.get(words) / count_word_ham


        return new_dict1,new_dict2


spam = input_processing(filename+"/train","spam")
ham = input_processing(filename+"/train","ham")

probability_spam_words, spam_file_count = spam.extract_token()
probability_ham_words, ham_file_count = ham.extract_token()

probability_spam_words,probability_ham_words = spam.calculate_probability(probability_spam_words,probability_ham_words)

probabilityspam = spam_file_count/total_count
probabilityham = ham_file_count/total_count



target.write(str(probabilityspam))
target.write("\n")
target.write(str (probabilityham))
target.write("\n")

for i in probability_spam_words:
    target.write(i)
    target.write("\t")
    target.write(str (probability_spam_words.get(i)))
    target.write("\t")
    target.write( str (probability_ham_words.get(i)))
    target.write("\n")

target.close()




