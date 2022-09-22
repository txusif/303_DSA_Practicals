# Write a program to create a basic Hash Table for Insertion, Deletion, Traversal operations 
# (Assume that there are no collisions)
# Hashing is a tecnique for storing and retrieveing information as soon as possible
# Used for storing data
# Hash function= x % 10

hashTable = [[], ] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0
    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

def getPrime(n):
    if n % 2 == 0:
        n = n+1
    while not checkPrime(n):
        n += 2
    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

insertData(123, "Apple")
insertData(432, "Mango")
insertData(213, "Guava")
insertData(654, "Banana")
print("HashTable:\n", hashTable)
removeData(123)
print("After deleting: 123\n", hashTable)