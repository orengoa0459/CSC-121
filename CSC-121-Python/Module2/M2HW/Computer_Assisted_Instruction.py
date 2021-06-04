#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:18:25 2021

@author: orengoa0459
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:06:30 2021

@author: orengoa0459
"""
import  functions as functions

def main():
    
   
    menuLoop = 0
    choice = ""
    while(menuLoop == 0):
        functions.StandardMessages.main_menu()
        
        choice = input("Choose from the menu --> ")
        
        if choice == "1":
            functions.StandardMessages.multiplication_problem()
            
        elif choice == "2":
            menuLoop = 1
            
if __name__ == "__main__":
    main()
