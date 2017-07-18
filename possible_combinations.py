# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:36:32 2017

@author: Anirban Das
"""
import csv

#==============================================================================
# from itertools import product
# stringReq = 'ABCDEFGH' #valid letters string
# stringLength = 4
# all_combinations = [''.join(i) for i in product(stringReq, repeat = stringLength)]
# print(all_combinations)
#==============================================================================


proteinSeq = 'MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQRVEDAFYTLVREIRQYRLKKISKEEKTPGCVKIKKCIIM'
#proteinSeq = 'MTEYK'
validAlphabet = 'GALMFWKQESPVICYHRNDT'
allCombinations = list()
for i in range(len(proteinSeq)):
    for letter in validAlphabet:
        dummySeq = list(proteinSeq)
        dummySeq[i] = letter
        dummySeq = ''.join(dummySeq)
        allCombinations.append(dummySeq)
totalGenerated = len(allCombinations)
print("Number of entries generated = ", totalGenerated)
filename = 'proteinSequence'+ str(totalGenerated) + '.csv'
with open(filename, 'w') as myfile:
    wr = csv.writer(myfile,delimiter=' ', quoting=csv.QUOTE_NONE)
    wr.writerow(allCombinations)

