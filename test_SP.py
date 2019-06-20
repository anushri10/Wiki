import pickle, random, sys
import numpy as np
import pandas as pd

'''
Creating test data as HWest.txt X Dummy  with flavour - SP
'''

testColumns = ['A', 'B']
testData = pd.DataFrame(columns=testColumns)
papers=[[]]
lines = open('dummy.txt', 'r', encoding='utf-8').readlines()
papers[0] = lines

#list of paras in dummy created 
dummy_para=[] 
for para in papers[0]:
    dummy_para.append(para)
print(len(dummy_para))

#Hwest sentences created
HWest_sentences = open('HWest.txt', 'r', encoding='utf-8').readlines()
print(len(HWest_sentences))

#creating CSV of SP flavour
rowIndex = 0
for A in HWest_sentences:
    for B in dummy_para:
        testData.loc[rowIndex] = [A, B]
        rowIndex += 1
        #print([A, B])
        print(rowIndex)

testData.to_csv('test_sp.csv', encoding='utf-8',index = False)