# -*- coding: utf-8 -*-
#בן בשביץ
"""
Spyder Editor

This is a temporary script file.
"""
import random


def CreateDictionary():
    trap_list = []
    test_list = []
    for i in range(1000):
        trap_list.append(random.randint(0,256))
        test_list.append(random.randint(0,10))
    dic = {'trap': trap_list, 'test': test_list}
    return dic

def Normalize(trap_list):
    for i in range(1000):
        trap_list[i] /= 255
    return trap_list
        
def CheckLists(trap_list, test_list):
    counter = 0
    for i in range(1000):
        if (trap_list[i] == 1) & (test_list[i] == 1):
            counter += 1
        elif(int(trap_list[i]*10) == test_list[i]):
            counter += 1
    return float(counter)/10
            
def main():
    dic = CreateDictionary()
    dic['trap'] = Normalize(dic['trap'])
    print (float(CheckLists(dic['trap'], dic['test'])))
  
if __name__ == "__main__":
    main()          
            
            
            
            
            
            
            
            
            
            
            
            