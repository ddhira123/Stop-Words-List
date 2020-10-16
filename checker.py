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
        if ad.is_latin(word) and word.islower() == False:
            return "Please repair the case to lowercase in "+file.name+"."
    return "PASS"