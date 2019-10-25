# -*- coding: utf-8 -*-
#בן בשביץ
"""
Spyder Editor

This is a temporary script file.
"""
import random

def main():
    

if __name__ == "__main__":
    main()


def CreateDictionary():
    trap_list = []
    test_list = []
    for i in range(1000):
        trap_list.append(random.randint(0,256))
        test_list.append(random.randint(0,10))
    dic = ['trap': trap_list, 'test': test_list]
    return dic


def Normalize(trap_list):
    for i in range(1000):
        trap_list[i] = trap_list[i]/255
        

def CheckLists(trap_list, test_list):
    counter = 0
    for i in range(1000):
        if(trap_list[i] == 1 && test_list[i] == 1)
            counter++
        elif(int(trap_list[i]*10) == test_list[i])
            counter++
    return counter/10
            
            
            
            
            
            
            
            
            
            
            
            
            
            