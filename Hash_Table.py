#!/usr/bin/python
import hashlib

class HashTable():
    """A class to construct hash tables"""
    def __init__(self):
        self.hash_table = []
        for i in range(10000):
            self.hash_table.append([])
    
    def insert(self, key, value):
        """insert an entry to the hash table"""
        h = hashlib.sha256(key)
        index = int(h.hexdigest(), 16) % 10000
        self.hash_table[index].append([key, value])
    
    def delete(self, key):
        """delete an item from the hash table"""
        h = hashlib.sha256(key)
        index = int(h.hexdigest(), 16) % 10000
        bucket = self.hash_table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del self.hash_table[index][i]
        
    def lookup(self, key):
        """lookup the value of an item"""
        h = hashlib.sha256(key)
        index = int(h.hexdigest(), 16) % 10000
        bucket = self.hash_table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]

# Test Harness
h = HashTable()
h.insert('Yao', 100)
h.insert('Tao', 99)
print h.lookup('Yao')
print h.lookup('Tao')
h.delete('Yao')
print h.lookup('Yao')
    