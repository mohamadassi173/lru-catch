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
        self.catch = {}
        self.first = None
        self.last = None
    
    
    def __getitem__(self, key):
        if not self.isExist(key):
            print("not found")
            # raise Exception("not found")
        
        # move the key to the end of dict and return its value   
        else:
            self.update_place(key)
            self.last = key
            print(self.catch[key][0])
            return self.catch[key][0]
        
        
    def __setitem__(self, key, value):
        if self.isExist(key):
            self.update_place(key)
        if self.first is None:
            self.first = key 
        self.catch[key] = [value, self.last, None]
        if self.last is not None:
            self.catch[self.last] = [self.catch[self.last][0], self.catch[self.last][1], key]
        self.last = key
        # Evict the least recently used key
        if self.isFull():
            remove = self.first
            self.first = self.catch[self.first][2]
            self.catch.pop(remove)
            
    def update_place(self, key):
        # first element: 
        if key == self.first and key != self.last:
            self.first = self.catch[self.first][2]
            self.catch[self.first] = [self.catch[self.first][0], None, self.catch[self.first][2]]
            self.catch[key] = [self.catch[key][0], self.last, None]
            self.catch[self.last] = [self.catch[self.last][0], self.catch[self.last][1], key]
            return
        # last element: 
        if key == self.last:
            return
        # in middle: 
        prev, nex = self.catch[key][1], self.catch[key][2]
        self.catch[prev] = [self.catch[prev][0], self.catch[prev][1], nex]
        self.catch[nex] = [self.catch[nex][0], prev, self.catch[nex][2]]
        self.catch[key] = [self.catch[key][0], self.last, None]
        self.catch[self.last] = [self.catch[self.last][0], self.catch[self.last][1], key]

        
        
    # checks if exceed the capacity
    def isFull(self) :
        # print(len(self.catch))
        return len(self.catch) > self.capacity
    
    # checks if the key exist in the dict
    def isExist(self, key : int):
        return key in self.catch
    

cache = lru_cache(2)
cache[1] = 1 # cache is {1=1}
cache[2] = 2 # cache is {1=1, 2=2}
cache[1] # return 1
cache[3] = 3 # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
cache[2] # Throws an exception (not found)
cache[4] = 4 # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
cache[1] # Throws an exception (not found)
cache[4] # return 4
cache[3] # return 3
cache[5] = 5 # LRU key was 4, evicts key 4, cache is {3=3, 5=5}
cache[4] # Throws an exception (not found)
cache[3] # return 3
cache[5] # return 5