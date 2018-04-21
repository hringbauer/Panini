'''
Created on Apr 20, 2018
This is the main class. All the magic happens here
@author: Harald
'''

import numpy as np
import os.path

class PaniniSticker(object):
    """General Class for Panini Stickers.
    Substickers inherit from here."""
    
    n = 681
    stickers = []
    path="./WC18.csv"
    
    def __init__(self, path=None, n=None):
        if path:
            self.path = path
        if n:
            self.n=n
        
        print("Using Path: %s" % self.path)
        print("Nr of Stickers: %i" % self.n)
        
        self.load_stickers()
        k = np.sum(self.stickers>0)
        print("Stickers loaded. You already have %i out of %i stickers. Wow!" 
              % (k, len(self.stickers)))
        # Automatically loads resp. generates the Stickers    
        
        
    def add_sticker(self, i):
        """Add Sticker i to List"""
        self.stickers[i-1] += 1
    
    def load_stickers(self):
        """Load all stickers"""
        # First Check whether Sticker is there
        # If not: Create
        
        # If yes: Load
        if os.path.exists(self.path):
            self.stickers = np.loadtxt(self.path, dtype="int")
            
        # If no: Create
        else:
            print("Creating new dataset.")
            self.stickers = np.zeros(self.n)
            
    def add_stickers(self):
        """"Add Stickers to the album.\n"""
        
        while True:
            i=input("Please enter sticker numbers. " 
                    "0 to stop!\n")
            i = int(i) # Make to Integer
            
            if i==0:
                print("Ending Input")
                break
            
            assert(0<i<=self.n)   # Sanity Check
            self.add_sticker(i) 
            
    def print_stickers(self):
        """"Prints the stickers"""
        print(self.stickers)

    def save_stickers(self):
        """"Save the stickers"""
        np.savetxt(self.path, self.stickers, fmt='%i')
        print("Stickers saved to %s" % self.path)
        
