# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:36:32 2017

@author: Anirban Das
"""
import csv
from textwrap import TextWrapper
#==============================================================================
# from itertools import product
# stringReq = 'ABCDEFGH' #valid letters string
# stringLength = 4
# all_combinations = [''.join(i) for i in product(stringReq, repeat = stringLength)]
# print(all_combinations)
#==============================================================================

def writeToTextFile(combinations, filename):  #if you want text file
    wrapper = TextWrapper(width=80)
    filepath = 'Outputs/' + filename + '.fasta'
    with open(filepath, 'w') as myfile:
        for element in range(len(combinations)):
            myfile.write(">sequence_combination#{}\n"\
                             .format(element))
            myfile.write("\n".join(wrapper.wrap(combinations[element])))
            myfile.write("\n")
    print("Generated text file :", filename+'.fasta')

#==============================================================================
def writeToCSV(combinations, filename): #if you want csv
    filepath = 'Outputs/'+ filename + '.csv'
    delimeter = "," #enter the delimeter you want
    with open(filepath, 'w') as myfile:
        wr = csv.writer(myfile,delimiter= delimeter, quoting=csv.QUOTE_NONE) 
        wr.writerow(combinations)
    print("Generated CSV file :", filename+'.csv')



if __name__ == '__main__':
    validAlphabet = 'GALMFWKQESPVICYHRNDT'
    file = open('sequenceFile.conf', 'r')
    proteinSeq = file.read().strip().split('\n')
    file.close()
    for sequence in proteinSeq:
        sequenceName, actualSequence = sequence.split('=')
        allCombinations = list()
        for i in range(len(actualSequence.strip())):
            for letter in validAlphabet:
                dummySeq = list(actualSequence.strip())
                dummySeq[i] = letter
                dummySeq = ''.join(dummySeq)
                allCombinations.append(dummySeq)

        uniqueCombinations = list(set(allCombinations)) #unique combinations
        totalUniqueGenerated = len(uniqueCombinations)  #number of unique combinations
        print("\nNumber of entries generated for sequence: {} = {}".format(sequenceName,totalUniqueGenerated))
        name_of_generated_File = 'proteinSequence_'+ sequenceName.strip() + '_'+ str(totalUniqueGenerated)
        #generate text file
        writeToTextFile(uniqueCombinations, name_of_generated_File)
        #generate CSV file
        writeToCSV(uniqueCombinations, name_of_generated_File)

    


