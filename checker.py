import os
from alphabet_detector import AlphabetDetector

def check_double(file):
    words = file.readlines()
    words1 = list(dict.fromkeys(words))
    if len(words) != len(words1):
        return "Duplicate words on "+file.name+". Please check again."
    return "PASS"

def check_case(file):
    lists = file.readlines()
    ad = AlphabetDetector()
    for word in lists:
        if word.isalpha() and ad.is_latin(word) and word.islower() == False:
            print(word)
            return "Please repair the case to lowercase in "+file.name+"."
    return "PASS"

def check_unwanted_occurences(file):
    lists = file.readlines()
    punc = '!"#$%&()*+,/:;<=>?@[\\]^`{|}~'
    for word in lists:
        if any(j.isdigit() or j in punc for j in word):
            return "Unwanted occurence in "+word+" in "+file.name+"."
    return "PASS"


filename = "urdu.txt"
file = open("./list/" + filename, encoding='utf-8')
print(check_case(file))
file.close()