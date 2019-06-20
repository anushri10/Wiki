import pickle, random, sys
import utils
import numpy as np
import pandas as pd


#papers = list of list containing papers with paragraphs
#papers[paperIndex] - particular paper with multiple paras
#papers[paperIndex][paraIndex] - text in that para of that paper 

'''

Sampling training data as 10k tuples with 20% positive labels and 80% negative labels.
On experimentation np.random.randint() performs slower as compared to random.random().

'''

trainColumns = ['A','B','label']
trainData = pd.DataFrame(columns=trainColumns)
tuples=10000
papers=[[]]
#lines = open('dummy.txt', 'r', encoding='utf-8').readlines()
lines = utils.ToList('dummy.txt')
papers[0]=lines
#print(lines,'\n')
#print("Length is: ", len(papers),'\n')    
paperIndex = np.random.randint(0,len(papers))

#print("Length of papers[paperIndex]", len(papers[paperIndex]))

'''
for row in range(tuples):
    a = np.random.randint(0,5)
    if a == 0:
        paraIndex = np.random.randint(0,len(papers[paperIndex]))
        sentences = papers[paperIndex][paraIndex].split('. ')
        sentences = list(filter(None,sentences))
        #sentences.remove(" ")
        A = random.choice(sentences)
        B = random.choice(sentences)
        label = 1
        trainData.loc[row]=[A,B,label]
    else:
        paraIndex = np.random.randint(0,len(papers[paperIndex]))
        sentences = papers[paperIndex][paraIndex].split('. ')
        sentences = list(filter(None,sentences))
        #sentences.remove(" ")
        A = random.choice(sentences)
        paraIndex2 = list(range(0,len(papers[paperIndex])))
        #print(paraIndex2)
        paraIndex2.remove(paraIndex)
        paraIndex = np.random.choice(paraIndex2)
        sentences = papers[paperIndex][paraIndex].split('. ')
        sentences = list(filter(None,sentences))
        #sentences.remove(" ")
        B = random.choice(sentences)
        label = 0
        trainData.loc[row]=[A,B,label] 

trainData.to_csv('checking_1.csv', encoding='utf-8',index = False)
'''
for row in range(tuples):
    paraIndex = np.random.randint(0,len(papers[paperIndex]))
    sentences = papers[paperIndex][paraIndex].split('. ')
    sentences = list(filter(None,sentences))
    #sentences.remove(" ")
    A = random.choice(sentences)
    a = random.random() < 0.2
    if a:
        B = random.choice(sentences)
        label = 1
    else:
        paraIndex2 = list(range(0,len(papers[paperIndex])))
        #print(paraIndex2)
        paraIndex2.remove(paraIndex)
        paraIndex = np.random.choice(paraIndex2)
        sentences = papers[paperIndex][paraIndex].split('. ')
        sentences = list(filter(None,sentences))
        B = random.choice(sentences)
        label = 0
    trainData.loc[row]=[A,B,label] 
trainData.to_csv('checking_2.csv', encoding='utf-8',index = False)

