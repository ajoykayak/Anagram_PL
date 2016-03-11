import os,sys
from itertools import permutations
from collections import defaultdict
import csv
# This code takes a dictionary file and converts words that are greater than 4 characters to their anagrams. Then writes the values to a text file
# Author : Andrea Vander Woude 
def open_OSdict(filename):
    word_list = []
    with open(filename, 'r') as f:
        word_list = [word.strip('\n') for word in f.readlines()]
    return word_list

def anagrams(word_list,directory):
    #output file name
    outputfile=directory+'/anagrams.txt'
    
    #opening dictionary file
    dictfile=directory+'/wordsEn.txt'
    dict_list = []
    with open(dictfile,'r') as g:
        dict_list=[word.strip('\r\n') for word in g.readlines()]
    
    #going through each word in the word_list from the OS dictionary
    for word in word_list:
        if len(word) >= 4: #only words that are greater than 4 characters
            # print 'we are in the loop', word.lower()
            word=word.lower()
            perms = [''.join(p) for p in permutations(word)] #find all the permutations of that word
            perms_s=set(perms)
            perms_s.remove(word) # remove original word from permutations list
            anas = [y for y in perms_s if y in dict_list] #anagrams
            
            # only write out anagrams if they have atleast one anagram
            if len(anas) >= 1:
                #print anas
                #write answers to a text file
                with open(outputfile,'a+b') as h:
                    writer=csv.writer(h)
                    anas.append(word)
                    writer.writerow(anas)
            else:
                pass
            pass

def main():
    filename=input("Enter the library location on your OS in single quotes:  ")
    directory=input("Enter the directory you want the output file to go to, without the / at the end:  ")
    start=open_OSdict(filename)
    anagrams(start,directory)

if __name__ == '__main__':
    main()
