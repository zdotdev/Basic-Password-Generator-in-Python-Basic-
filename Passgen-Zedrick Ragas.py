# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:04:03 2019

@author: Zedo Ragas
"""

import time
import random
import pickle
import os

print("\n-----Welcom to my Program-----")



def start():
    print("\n-----Password Generator-----")
    nun = input("Input Username: ")
    site = input("What site do you want to use my Program? ")
    a = input('Name: ')
    b = input('Age: ')
    c = input('Birthday(mm/dd/yyyy): ')
    d = ("!@#$%^&*()")
    
    sec=5
    
    aa = a.upper()
    aaa = a.lower()
    characters1 = list(aa + b)
    characters2 = list(aa + aaa + b + c)
    characters3 = list(aa + aaa + b + c + d)
    def grp1():
        random.shuffle(characters1)
        password1 = []
        for length1 in range (15):
            password1.append(random.choice(characters1))
        random.shuffle(password1)
        print("".join(password1))
    
        random.shuffle(characters2)
        password2 = []
        for length2 in range (15):
            password2.append(random.choice(characters2))
        random.shuffle(password2)
        print("".join(password2))
        
        random.shuffle(characters3)
        password3 = []
        for length3 in range (15):
            password3.append(random.choice(characters3))
        random.shuffle(password3)
        print("".join(password3))
        
        new = ("".join(password1),"".join(password2),"".join(password3))

        
        yes = ('Y')
        no = ('N')
        sv = input('Do you want to save your password(Y/N)? ')
        
        if sv == yes:
            pickle.dump(new, open(f'{nun}{site}.txt', 'wb'))
            print('\nPassword saved!!!') 
                
        elif sv == no:
            print('\nPassword not saved!!!\n   ')
    
    print('\nGenerating Password please wait...\n')
    
    
    
    while sec>0:
        print(sec)
        time.sleep(1)
        sec=sec-1
        
    print("\nHere's your Password!!!\n    ")
        
    grp1()

a = ("A")
b = ("B")

print("\nA. Create Password B. Load Password")
Q1 = input("What do you want to do? ")

if Q1 == a:
    start()
elif Q1 == b:
        un = input("Whats your Username? ")
        st = input("What site did you save? ")  
        check = os.path.isfile((f"{un}{st}.txt"))
        if check == True: 
            spw = pickle.load(open(f'{un}{st}.txt', 'rb'))
            print(spw)
        else:
            print("Input Username or Site is wrong!!!")

for loop1 in range(999999):
    y = ('Y')
    n = ('N')
    rerun = input('Do you want to create new password(Y/N)? ')
    if rerun == y:
        start()    
    elif rerun == n:
            print('\nThanks for using my Program!!!')
            break
