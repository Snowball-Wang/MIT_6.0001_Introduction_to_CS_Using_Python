#!/usr/bin/env python3
#*******************************************************
#       Filename: test.py
#       Author: Snowball Wang
#       Mail: wjq1996@mail.ustc.edu.cn
#       Description: ---
#       Created on: 2018-11-14 15:37:43
#*******************************************************
import string

def is_phrase_in(phrase, text):
    found = False
    text = text.lower()
    for char in text:
        if char in string.punctuation:
            text = text.replace(char, ' ')
    text = ' '.join(text.split())
    text_list = text.split()
    loc_list = []
    for w in phrase.lower().split():
        if w in text_list:
            loc_list.append(text_list.index(w))
        else:
            return False


    for i in range(1, len(loc_list)):
        if int(loc_list[i]) - int(loc_list[i-1]) == 1:
            found = True
        else:
            return False
    return found



phrase = "PURPLE COW"
phrase1 = 'purple cow'
text1 = "Purple!!! Cow!!!"
text2 = 'purple@#$%cow'
text3 = "Did you see a purple   cow?"
text4 = 'Purple cows are cool!'
text5 = 'The purple blob over there is a cow.'
text6 = 'purplecowpurplecow'
text7 = 'how now brown cow.'
text8 = 'Cow!!! Purple!!!!'
result1 = is_phrase_in(phrase, text1)
result1_1 = is_phrase_in(phrase1, text1)
result2 = is_phrase_in(phrase, text2)
result3 = is_phrase_in(phrase, text3)
result4 = is_phrase_in(phrase, text4)
result5 = is_phrase_in(phrase, text5)
result6 = is_phrase_in(phrase, text6)
result7 = is_phrase_in(phrase, text7)
result8 = is_phrase_in(phrase, text8)
print("True: ", result1)
print("True: ", result1_1)
print()

print("True: ", result2)
print("True: ", result3)
print("False: ", result4)
print("False: ", result5)
print("False: ", result6)
print("False: ", result7)
print("False: ", result8)

print()
phrase1 = "this is a phrase"
text1 = "ohh, this is a phrase for me."
text2 = "ohh, this is a phrases for me."
result1 = is_phrase_in(phrase1, text1)
result2 = is_phrase_in(phrase1, text2)
print("True: ", result1)
print("False: ", result2)

