from collections import OrderedDict
"""
Implementation of "least recently used cache" using ordered dictionary data structure, 
which keep the order of inserted keys and move specific key to the end of
dict with O(1) complexity.
tested on: Python 3.9
"""

class lru_cache:
    
    # init the capacity with given capacity value, and empty ordered dictionary
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.catch = OrderedDict()
    
    
    def __getitem__(self, key):
        if not self.isExist(key):
            print("not found")
            
        # move the key to the end of dict and return its value   
        else:
            self.catch.move_to_end(key)
            return self.catch[key]
        
        
    def __setitem__(self, key, value):
        self.catch[key] = value
         # make the key as recently used key -  O(1) complexity
        self.catch.move_to_end(key)
        
        # Evict the least recently used key
        if self.isFull():
            self.catch.popitem(last = False) # O(1) complexity



    # checks if exceed the capacity
    def isFull(self) :
        # print(len(self.catch))
        return len(self.catch) > self.capacity
    
    # checks if the key exist in the dict
    def isExist(self, key : int):
        return key in self.catch
    
    