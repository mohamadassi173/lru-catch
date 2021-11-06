from collections import OrderedDict
"""
Implementation of "least recently used cache" using dict of keys,
and every key have a list of [value, previous added key, next added key]
which make the dict to act like a linked list and keep the order of inserted 
keys  with O(1) complexity.
tested on: Python 3.9
written in: vs code.
"""
class lru_cache:
    
    # init the capacity with given capacity value, and empty dictionary:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.catch = {} # every key => [value, prev, next]
        self.first = None # pointer to the "least recently used node"
        self.last = None # pointer to the "most recently used node"
    
    
    def __getitem__(self, key):
        # key is not exist in the dict:
        if not self.isExist(key):
            raise Exception("not found")
        # update the element place and return its value:   
        else:
            self.update_place(key)
            self.last = key
            return self.catch[key][0]
        
        
    def __setitem__(self, key, value):
        # first add(dict is empty):
        if self.first is None:
            self.first = key
        # put key in the right place:
        if self.isExist(key):
            self.update_place(key, value)
        else:
            self.catch[key] = [value, self.last, None]
        # update last element:
            if self.last is not None:
                self.catch[self.last] = [self.catch[self.last][0], self.catch[self.last][1], key]
        self.last = key
        # Evict the least recently used key if dict is full:
        if self.isFull():
            remove = self.first
            self.first = self.catch[self.first][2]
            self.catch.pop(remove)
 
 
    def update_place(self, key, value=None):
        # first element: 
        if key == self.first and key != self.last:
            self.first = self.catch[self.first][2]
            self.catch[self.first] = [self.catch[self.first][0], None, self.catch[self.first][2]]
            self.catch[key] = [self.catch[key][0] if value == None else value, self.last, None]
            self.catch[self.last] = [self.catch[self.last][0], self.catch[self.last][1], key]
            return
        # last element: 
        if key == self.last:
            self.catch[key] = [self.catch[key][0] if value == None else value, self.catch[key][1], None]        
            return
        # in middle: 
        prev, nex = self.catch[key][1], self.catch[key][2]
        self.catch[prev] = [self.catch[prev][0], self.catch[prev][1], nex]
        self.catch[nex] = [self.catch[nex][0], prev, self.catch[nex][2]]
        self.catch[key] = [self.catch[key][0] if value == None else value, self.last, None]
        self.catch[self.last] = [self.catch[self.last][0], self.catch[self.last][1], key]

        
        
    # checks if exceed the capacity
    def isFull(self) :
        # print(len(self.catch))
        return len(self.catch) > self.capacity
    
    # checks if the key exist in the dict
    def isExist(self, key : int):
        return key in self.catch
