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
        self.cache_list = []
    
    
    def __getitem__(self, key):
        if not self.isExist(key):
            print("not found")
            # raise Exception("not found")
        
        # move the key to the end of dict and return its value   
        else:
            self.cache_list.append(key)
            print(self.catch[key])
            return self.catch[key]
        
        
    def __setitem__(self, key, value):
        self.cache_list.append(key)
        self.catch[key] = value
         # make the key as recently used key -  O(1) complexity
        # Evict the least recently used key
        if self.isFull():
            self.catch.pop(self.cache_list[len(self.cache_list) - self.capacity - 1]) # O(1) complexity


    # checks if exceed the capacity
    def isFull(self) :
        # print(len(self.catch))
        return len(self.catch) > self.capacity
    
    # checks if the key exist in the dict
    def isExist(self, key : int):
        return key in self.catch
    
cache = lru_cache(10)
cache[10] = 13 # cache is {1=1}
cache[3] = 17
cache[6] = 11
cache[10] = 5
cache[9] = 10
cache[13]
cache[2] = 19
cache[2]
cache[3]
cache[5] = 25
cache[8]
cache[9] = 22
cache[5] = 5
cache[1] = 30
cache[11]
cache[9] = 12
cache[7]
cache[5]
cache[8]
cache[9]
cache[4] = 30
cache[9] = 3
cache[9]
cache[10]
cache[10]
cache[6] = 14
cache[3] = 1
cache[3]
cache[10] = 11
cache[8]
cache[2] = 14
cache[1]
cache[5]
cache[4]
cache[11] = 4
cache[12] = 24
cache[5] = 18
cache[13]
cache[7] = 23
cache[8]
cache[12]
cache[3] = 27
cache[2] = 12
cache[5]
cache[2] = 9
cache[13] = 4
cache[8] = 18
cache[1] = 7
cache[6]
# cache[9] = 29
# cache[8] = 21
# cache[5]
# cache[6] = 30
# cache[1] = 12
# cache[10]
# cache[4] = 15
# cache[7] = 22
# cache[11] = 26
# cache[8] = 17
# ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
# [[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]