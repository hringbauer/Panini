'''
Created on Apr 20, 2018
This is the main class. All the magic happens here
@author: Harald
'''

import numpy as np
import os.path
import matplotlib.pyplot as plt

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
            
            k = np.sum(self.stickers>0)
            print("Stickers loaded. You already have %i out of %i stickers. Wow!" 
                  % (k, len(self.stickers)))
            
        # If no: Create
        else:
            print("Creating new dataset of length %i" % self.n)
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
        
        fs=12
        xs=range(1, self.n+1)
        plt.figure(figsize=(12,4))
        plt.plot(xs, self.stickers, "ro")
        plt.ylabel("Count", fontsize=fs)
        plt.xlabel("Sticker Number", fontsize=fs)
        plt.title("Panini Doubles", fontsize=fs)
        plt.show()
        
    def save_stickers(self):
        """"Save the stickers"""
        np.savetxt(self.path, self.stickers, fmt='%i')
        print("Stickers saved to %s" % self.path)
        
    def reset_stickers(self):
        """Reset all Stickers to 0"""
        self.stickers = np.zeros(self.n)
        
    def print_doubles(self):
        """Prints all of my doubles"""  
        double_inds = np.where(self.stickers>=2)[0]
        
        print("Doubles: Total Nr: %i" % len(double_inds))
        
        print("Double Indices:")
        print(double_inds+1)
        
    def print_missing(self):
        """Prints all of my missing"""
        print("To Do!")
        
