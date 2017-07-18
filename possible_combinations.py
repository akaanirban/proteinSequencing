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

def writeToTextFile(combinations, filename):  #if you want text file
    filename = filename + '.txt'
    with open(filename, 'w') as myfile:
        myfile.write(" ".join(combinations))
    print("Generated text file :", filename)

#==============================================================================
def writeToCSV(combinations, filename): #if you want csv
    filename = filename + '.csv'
    delimeter = ',' #enter the delimeter you want
    with open(filename, 'w') as myfile:
        wr = csv.writer(myfile,delimiter= delimeter, quoting=csv.QUOTE_NONE) 
        wr.writerow(combinations)
    print("Generated CSV file :", filename)



if __name__ == '__main__':
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
    name_of_generated_File = 'proteinSequence_'+ str(totalGenerated)
    #generate text file
    writeToTextFile(allCombinations, name_of_generated_File)
    #generate CSV file
    writeToCSV(allCombinations, name_of_generated_File)

    

