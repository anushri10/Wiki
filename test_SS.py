import pickle, random, sys
import numpy as np
import pandas as pd

'''
Creating test data as Dummy X HWest.txt  with flavour - SS
'''

testColumns = ['A', 'B']
testData = pd.DataFrame(columns=testColumns)
papers=[[]]
lines = open('dummy.txt', 'r', encoding='utf-8').readlines()
papers[0] = lines

#dummy sentences created 
dummy_sentences=[] 
for para in papers[0]:
    for line in para.split('. '):
        line = line.lstrip()
        line = line.rstrip()
        dummy_sentences.append(line)
dummy_sentences = list(filter(None,dummy_sentences))
#print("Sentences are:\n",dummy_sentences,'\n',"Length: ",len(dummy_sentences))
'''
print(len(dummy_sentences))
for sentence in dummy_sentences:
    print(sentence)
'''
#Hwest sentences created
HWest_sentences = open('HWest.txt', 'r', encoding='utf-8').readlines()
print(len(HWest_sentences))

#creating CSV of SS flavour
rowIndex = 0
for A in dummy_sentences:
    for B in HWest_sentences:
        testData.loc[rowIndex] = [A, B]
        rowIndex += 1
        #print([A, B])
        print(rowIndex)

testData.to_csv('test_ss.csv', encoding='utf-8',index = False)
