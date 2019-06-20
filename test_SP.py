import pickle, random, sys
import numpy as np
import pandas as pd
import utils

'''
Creating test data as HWest.txt X Dummy  with two flavour - SP/PS based on arg toggle. 
SP is the default result, if toggled then PS is created.
A and B are filenames of respective sentences
'''
def test_sp(A,B,toggle=False):
    testColumns = ['A', 'B']
    testData = pd.DataFrame(columns=testColumns)
    papers=[[]]
    #lines = open(B, 'r', encoding='utf-8').readlines()
	#lines = open('dummy.txt', 'r', encoding='utf-8').readlines()
    #papers[0] = lines
    papers[0]=utils.ToList(B)
	#print()

    #list of paras in dummy (B) created 
    dummy_para=[] 
    for para in papers[0]:
        dummy_para.append(para)
    print(len(dummy_para))

    #List of sentences in HWest (A) created
    #HWest_sentences = open('HWest.txt', 'r', encoding='utf-8').readlines()
    HWest_sentences = open(A,'r',encoding='utf-8').readlines()
	# print(len(HWest_sentences))
    print(len(HWest_sentences))

    #creating CSV of SP/PS flavour based on toggle value.
    if toggle:
        filename = 'test_toggled_ps.csv'
        out_loop = dummy_para
        in_loop= HWest_sentences
    else:
        filename='test_sp.csv'
        out_loop = HWest_sentences
        in_loop = dummy_para
    rowIndex = 0
    for A in out_loop:
        for B in in_loop:
            testData.loc[rowIndex] = [A, B]
            rowIndex += 1
            #print([A, B])
            print(rowIndex)
        
    testData.to_csv(filename, encoding='utf-8',index = False)
    return

if __name__ == "__main__":

    '''
    main/ driver function
    '''
    test_sp('HWest.txt','dummy.txt',True)