

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
 
"""
Created on Tue Jun  1 12:07:19 2021

@author: orengoa0459
"""

import random
import sys
import random

 

class StandardMessages():
    
    staticmethod(0)
    def main_menu():
        
        print("Main Menu\n" +
              "*********************\n" +
              "1. Multiplication Game\n" +
              "2. Exit")
        
    staticmethod(0)
    def invalidMessages():
        
        print("Invalid Option! Try Again!")


    def multiplication_problem():
        score = 0;         
        loop = 0
        while(loop < 10):
            count = 0
            retryLoop = False
            numOne = random.randrange(1,10)
            numTwo = random.randrange(1,10)
            answer = numOne * numTwo
            answer = str(answer)
            
            
            print("How much is ", numOne, "times", numTwo,"?")
            choice = input("Enter Answer: ")
            
            if choice == answer:
                score += 1
                print("Great Job!\n")
            elif choice != answer:
                print("Sorry your answer is incorrect! Try Again\n")
                count += 1
                while(retryLoop == False):
                    
                    print("How much is ", numOne, "times", numTwo,"?")
                    choice = input("Enter Answer: ")
                    
                    if choice == answer:
                        print("Great Job!")
                        score += 1
                        retryLoop = True
                    elif choice != answer and count < 3:
                        print("Sorry your answer is incorrect! Try Again\n")
                        count += 1
                        
                    elif count >=3:
                            print("Sorry but you failed to answer correctly!\n" +
                              "The correct answer is: ", answer,"\n\n")
                            retryLoop = True
                    
                    else:
                
                        print("Incorrect Response! ")
                        
            else:
                
                        print("Incorrect Response! ")     
                
            loop += 1
        print("\n\nYou scored ",score, "out of ", score)
        if score == 10:
            print("Great Job! You scored a perfect score...")
        elif score >=8 and score < 10:
            print("Good Job! You almost scored perfectly...")
        elif score > 5 and score <= 7:
            print("Good Job! You multiplication skills are average...")
        elif score > 3 and score < 5:
            print("Ok job! You need some work...")
        elif score < 3:
            print("You need to hit the books!\n\n")
 
    
 
