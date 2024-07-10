# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 19:43:17 2024

@author: gbulb
"""
dna_strings={}
dna_strings['Rosalind_14']='ACGTACGTGACG'
dna_strings['Rosalind_18']='GTA'

#print(search_over_string(substring,string))

def determine_substring_string(dna_strings):
    val1,val2='',''
    for key in dna_strings.keys():
        if len(dna_strings[key])!=3:
            val1=dna_strings[key]
        elif len(dna_strings[key])==3:
             val2=dna_strings[key]
             return val1,val2
string,substring=determine_substring_string(dna_strings)


class substring_over_string:
      def __init__(self,string,substring):
          self.string=string
          self.substring=substring
      def search_over_string(string,substring):
          list_of_positions=[]
          list_of_motifs=[]
          dict_for_positions={}
          t,s=substring, string
          for i in range(len(t)-2):
             for j in range(len(s)-2):
                 if t[i] in s:
                     if t[i]==s[j]:
                         if t[i+1]==s[j+1]:
                             if t[i+2]==s[j+2]:
                                print(t[i]+''+t[i+1]+''+t[i+2])
                                list_of_motifs.append(t[i]+''+t[i+1]+''+t[i+2])
                                list_of_positions.append(j+1)
                                dict_for_positions[list_of_positions[-1]]=list_of_motifs[-1]
                     elif t[i]==s[j-1]:
                         if t[i+1]==s[j]:
                             if t[i+2]==s[j+2]:
                                print(t[i]+''+t[i+1]+''+t[i+2])
                                list_of_motifs.append(t[i]+''+t[i+1]+''+t[i+2])
                                list_of_positions.append(j+3)
                                dict_for_positions[list_of_positions[-1]]=list_of_motifs[-1]
                 if t[i+1] in s:
                                
                     if t[i+1]==s[j]:
                         if t[i]==s[j+1]:
                             if t[i+2]==s[j+2]:
                                print(t[i+1]+''+t[i]+''+t[i+2])
                                list_of_motifs.append(t[i+1]+''+t[i]+''+t[i+2])
                                list_of_positions.append(j+1)
                                dict_for_positions[list_of_positions[-1]]=list_of_motifs[-1]
                                return list_of_positions,dict_for_positions
if __name__=="__main__":
   print(substring_over_string.search_over_string(string,substring))