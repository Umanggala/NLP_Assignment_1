#string = "how much for the maple syrup? $20.99? That's ricidulous!!!"
#string = re.sub('[^\w]', '', string)
#print(string)
#'mississippi'.rstrip('ipz')

import glob, os
import re

class input_processing:

    global total_count
    total_count = 0

    global distinct_words
    distinct_words = []

    def __init__(self,dir,sub_dir):
        self.dir = dir
        self.sub_dir = sub_dir


    def extract_token(self):
        list = []
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
                            line = ''.join(line.splitlines())
                            for word in line.split():
                                word = re.sub('[^\w]', '', word)
                                list.append(word)
                                global distinct_words
                                if (word not in distinct_words):
                                    distinct_words.append(word)
        return list, count

    def calculate_probability(self,list):

        new_dict = {}

        for words in list:
            if words not in new_dict:
                new_dict[words] = 1
            else:
                new_dict[words] = new_dict.get(words) + 1

        global distinct_words

        for i in distinct_words:
            if(i not in new_dict):
                new_dict[i] = 1
            else:
                new_dict[i] = new_dict.get(i) + 1


        return new_dict


    def calculate_word_given_class(self, new_dict1):

        count_word_total = 0

        for i in new_dict1:
            count_word_total = count_word_total + new_dict1.get(i)

        #print(count_word_total)

        for i in new_dict1:
            new_dict1[i] = new_dict1.get(i)/count_word_total

        return new_dict1



spam = input_processing("/Users/umanggala/desktop/courses/nlp/code/","spam")
ham = input_processing("/Users/umanggala/desktop/courses/nlp/code/","ham")

probability_spam_words, spam_file_count = spam.extract_token()
probability_ham_words, ham_file_count = ham.extract_token()

probabilityspam = spam_file_count/total_count
probabilityham = ham_file_count/total_count

probability_spam_words = spam.calculate_probability(probability_spam_words)
probability_ham_words = ham.calculate_probability(probability_ham_words)

probability_word_given_spam = spam.calculate_word_given_class(probability_spam_words)
probability_word_given_ham = ham.calculate_word_given_class(probability_ham_words)

global distinct_words

target = open("/Users/umanggala/desktop/courses/nlp/code/nbmodel.txt", 'w')

target.write(str(probabilityspam))
target.write("\n")
target.write(str (probabilityham))
target.write("\n")

for i in distinct_words:
    target.write(i)
    target.write("\t")
    target.write(str (probability_word_given_spam.get(i)))
    target.write("\t")
    target.write( str (probability_word_given_ham.get(i)))
    target.write("\n")

target.close()




