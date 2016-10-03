# NLP_Email_Classification

This project classifies the data into Spam emails or Ham emails using Naive Bayes classification algorithm. 
We initially train our model by using the training data and then we test it on a couple of examples using testing data. 

Training data: Data/train
Testing data: Data/dev

I divided the task of using this Naive Bayes classification algorithm into two parts.
i) I did not clean the data and performed Naive Bayes classification algorithm on it. 
ii) I cleaned the data and then performed Naive Bayes classification algorithm on it. 

# 1. This was the first task. 
Modeling: Code/nblearn.py
Classify: Code/nbclassify.py. 

Performance: 
1a. spam precision: 0.99
1b. spam recall: 0.98
1c. spam F1 score: 0.99
1d. ham precision: 0.95
1e. ham recall: 0.98
1f. ham F1 score: 0.96


# 2. Description of enhancement I tried. 

Modeling: Code/nblearnmod.py
Classify: Code/nbclassifymod.py.

a. Initially I removed all the stop words from the test file and then used the cleaned text file to calculate the probability. This helps to remove the common words and hence reduces their calculation for probabilities. 
b. Then I removed all the special characters from the file and hence it thus improved the probabilities for the ham calculation and spam calculation.
	 
Performance:
2a. spam precision: 0.9913
2b. spam recall: 0.9929
2c. spam F1 score: 0.9921
2d. ham precision: 0.9826
2e. ham recall: 0.9786
2f. ham F1 score: 0.9763
