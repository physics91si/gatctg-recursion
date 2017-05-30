#!/usr/bin/env python3

# Lab 16: Recursion
# Levenshtein Distance
def lev(str1, str2, count=0):
    if str2 == "":
        return count
    elif str1  == "":
        count +=1
        return count
    char1 = strToChar(str1)
    temp = char1.pop()
    if temp == str2[len(str2) - 1:]:
        char2 = strToChar(str2)
        char2.pop()
        print("1 call")
        return lev(charToStr(char1),charToStr(char2), count)
    elif temp == str2[len(str2) - 2:len(str2) - 1]:
        count += 1
        char2 = strToChar(str2)
        char2.pop()
        char2.pop()
        print("2 call")
        return lev(charToStr(char1), charToStr(char2), count)
    count +=1
    temp = char1.pop()
    if temp == str2[len(str2) - 1:]:
        char2 = strToChar(str2)
        char2.pop()
        print("3 call")
        return lev(charToStr(char1), charToStr(char2), count)
    else:
        char2 = strToChar(str2)
        char2.pop()
        #char2.pop()
        print("4 call")
        print(charToStr(char2))
        return lev(charToStr(char1), charToStr(char2), count)
def strToChar(str):
    chars = []                                                                
    for char in str:                                                          
        chars.append(char)
    return chars
def charToStr(chars):
    str = ""
    for char in chars:                                                    
        str += char
    return str
