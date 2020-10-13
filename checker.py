import os
from alphabet_detector import AlphabetDetector

def check_double(file):
    words = []
    for word in file.readlines():
        if word in words:
            print(word)
            return False
        else:
            words.append(word)
    return True

def check_lower(file):
    ad = AlphabetDetector()
    for word in file.readlines():
        if ad.is_latin(word) and word.islower() == False:
            return False
    return True

def runner():
    for filename in os.listdir('list'):
        file = open("./list/" + filename, encoding='utf-8')
        if check_double(file) == False:
            file.close()
            return "Duplicate records in "+filename
        elif check_lower(file) == False:
            file.close()
            return "Uppercase found in "+filename
        file.close()
    return "PASS"