'''
Created on Apr 20, 2018
The main class, where stickers are loaded
@author: Harald
'''
from stickers import PaniniSticker


if __name__ == '__main__':
    print("Hello there.")
    
    s = PaniniSticker()
    
    while True:
        i=int(input("\nWhat do you want to do?\n"
              "(1) Load Stickers \n(2) Save Stickers \n(3) Add Stickers"
              "\n(4) Print Stickers \n(5) Exit\n"))
        
        if i==1:
            s.load_stickers()
            
        if i==2:
            s.save_stickers()
            
        if i==3:
            s.add_stickers()
        
        if i==4:
            s.print_stickers()
            
        if i==5:
            break
        
    
    print("Goodbye Horses!")
    
