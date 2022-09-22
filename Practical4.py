# Write a program to implement Stack with insertion, deletion, traversal operations.

from collections import deque

stack = deque()

stack.append("Java")
stack.append("Python")
stack.append("C++")

print("Initial stack: ")
print(stack)

print(" ")
print("Elements popped from stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(" ")
print("Stack after elements are popped: ")
print(stack)