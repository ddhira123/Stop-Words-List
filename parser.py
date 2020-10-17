import os

def repair_double_and_rearrange(file, filename):
    words = file.readlines()
    words = [i.strip() for i in words]
    words = list(dict.fromkeys(words))
    file1 = open("./list/" + filename, "w", encoding='utf-8')
    for word in words:
        file1.write(word+"\n")
    file1.close()

def remove_unwanted(file, filename):
    lists = file.readlines()
    file1 = open("./list/" + filename, "w", encoding='utf-8')
    words = []
    punc = '!"#$%&()*+,/:;<=>?@[\\]^`{|}~'
    for word in lists:
        if any(j.isdigit() or j in punc for j in word):
            continue
        # elif len(word.split()) > 1:
        #     continue
        else:
            words.append(word)
    for word in words:
        file1.write(word)
    return True

def repair_case(file, filename):
    lists = file.readlines()
    file1 = open("./list/" + filename, "w", encoding='utf-8')
    words = []
    for word in lists:
        if word.isalpha() and word.islower() == False:
            word = word.lower()
        words.append(word)
    for word in words:
        file1.write(word)
    return True

def runner():
    for filename in os.listdir('list'):
        file = open("./list/" + filename, encoding='utf-8')
        repair_case(file, filename)
        file.close()
        file = open("./list/" + filename, encoding='utf-8')
        remove_unwanted(file, filename)
        file.close()
        file = open("./list/" + filename, encoding='utf-8')
        repair_double_and_rearrange(file, filename)
        file.close()
    return "PASS"


runner()
