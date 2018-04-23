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
              "\n(4) Print Stickers \n(5) Print Doubles \n(6) Print Missing Stickers" 
              "\n(7) Show Total Stats \n(8) Reset Stickers \n(9) Overlap \n(0) Exit\n"))
        
        if i==1:
            s.load_stickers()
            
        if i==2:
            s.save_stickers()
            
        if i==3:
            s.add_stickers()
        
        if i==4:
            s.print_stickers()
            
        if i==5:
            s.print_doubles()
            
        if i==6:
            s.print_missing()
        
        if i==7:
            s.show_stats()  
        
        if i==8:
            s.reset_stickers()
            print("WARNING: Stickers deleted!!!")
            
        if i==9:
            s.print_overlap()
            
        if i==0:
            break
        
    
    print("Goodbye Horses!")
    
