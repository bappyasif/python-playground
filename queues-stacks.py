# queues and stacks
# queues and stacks they are both data structures that can hold a collection of items
# they both are not built-in data structures in python
# but we can leverage pythons built in data structures such as lists to create them
# difference between queues and stacks is that queues have a FIFO (first in first out) order, while stacks have a LIFO (last in first out) order


# queues
# a queue is a data structure that holds a collection of items in a particular order
# items are added to the end of the queue and removed from the beginning of the queue
# the first item added to the queue will be the first item removed from the queue
# queues are also known as FIFO (first in first out) data structures

# implementation
# queues can be implemented using lists in python
# we can use append() method to add items to the end of the queue
# we can use pop() method to remove an item from the beginning of the queue
# we can use len() method to get the number of items in the queue
# we can use index() method to get the index of an item in the queue
# we can use count() method to get the number of times an item appears in the queue
# we can use sort() method to sort the items in the queue
# we can use reverse() method to reverse the order of the items in the queue
# we can use clear() method to remove all items from the queue
# we can use copy() method to create a copy of the queue
# we can use extend() method to add multiple items to the end of the queue
# we can use insert() method to add an item to a specific position in the queue
# we can use remove() method to remove an item from the

# examples
print("queues example \n")
queue = []
queue.append(1) # add 1 to the end of the queue
queue.append(2) # add 2 to the end of the queue
queue.append(3) # add 3 to the end of the queue
print(queue) # prints [1, 2, 3]
queue.pop(0) # remove the first item from the queue
print(queue) # prints [2, 3]
print(len(queue)) # prints 2
print(queue.index(2)) # prints 0
print(queue.count(2)) # prints 1
queue.sort() # sort the items in the queue
print(queue) # prints [2, 3]
queue.reverse() # reverse the order of the items in the queue
print(queue) # prints [3, 2]
queue.clear() # remove all items from the queue
print(queue) # prints []
queue.extend([4, 5, 6]) # add multiple items to the end of the queue
print(queue) # prints [4, 5, 6]
queue.insert(0, 0) # add an item to a specific position in the queue
print(queue) # prints [0, 4, 5, 6]
queue.remove(0) # remove an item from the queue
print(queue) # prints [4, 5, 6]
print(queue.copy()) # create a copy of the queue


# stacks
# a stack is a data structure that holds a collection of items in a particular order
# items are added to the end of the stack and removed from the end of the stack
# the last item added to the stack will be the first item removed from the stack
# stacks are also known as LIFO (last in first out) data structures

# implementation
# stacks can be implemented using lists in python
# we can use append() method to add items to the end of the stack
# we can use pop() method to remove an item from the end of the stack
# we can use len() method to get the number of items in the stack
# we can use index() method to get the index of an item in the stack
# we can use count() method to get the number of times an item appears in the stack
# we can use sort() method to sort the items in the stack
# we can use reverse() method to reverse the order of the items in the stack
# we can use clear() method to remove all items from the stack
# we can use copy() method to create a copy of the stack
# we can use extend() method to add multiple items to the end of the stack
# we can use insert() method to add an item to a specific position in the stack
# we can use remove() method to remove an item from the stack

# examples
print("stacks example\n")
stack = []
stack.append(1) # add 1 to the end of the stack
stack.append(2) # add 2 to the end of the stack
stack.append(3) # add 3 to the end of the stack
print(stack) # prints [1, 2, 3]
stack.pop() # remove the last item from the stack
print(stack) # prints [1, 2]
print(len(stack)) # prints 2
print(stack.index(2)) # prints 0
print(stack.count(2)) # prints 1
stack.sort() # sort the items in the stack
print(stack) # prints [1, 2]
stack.reverse() # reverse the order of the items in the stack
print(stack) # prints [2, 1]
stack.clear() # remove all items from the stack
print(stack) # prints []
stack.extend([4, 5, 6]) # add multiple items to the end of the stack
print(stack) # prints [4, 5, 6]
stack.insert(0, 0) # add an item to a specific position in the stack
print(stack) # prints [0, 4, 5, 6]
stack.remove(0) # remove an item from the stack
print(stack) # prints [4, 5, 6]
print(stack.copy()) # create a copy of the stack

# examples with classes from codecademy
# from node import Node
 
# class Queue:
#   def __init__(self):
#     self.head = None
#     self.tail = None
#     self.size = 0
  
#   def enqueue(self, value):

#     item_to_add = Node(value)
#     print("Adding " + str(item_to_add.get_value()) + " to the queue!")
#     if self.is_empty():
#       self.head = item_to_add
#       self.tail = item_to_add
#       self.size = 1
#     else:
#       self.tail.set_next_node(item_to_add)
#       self.tail = item_to_add
#       self.size += 1
       
#   def dequeue(self):
#     if self.get_size() > 0:
#       item_to_remove = self.head
#       print(str(item_to_remove.get_value()) + " is served!")
#       if self.get_size() == 1:
#         self.head = None
#         self.tail = None
#       else:
#         self.head = self.head.get_next_node()
#         self.size -= 1
#         return item_to_remove.get_value()
#     else:
#       print("The queue is totally empty!")


#   def peek(self):
#     if self.size > 0:
#       return self.head.get_value()
#     else:
#       print("No orders waiting!")
     
#   def get_size(self):
#     return self.size
  
#   def is_empty(self):
#     return self.size == 0
 


# print("Creating a deli line with up to 10 orders...\n------------")
# deli_line = Queue()
# print("Adding orders to our deli line...\n------------")
# deli_line.enqueue("egg and cheese on a roll")
# deli_line.enqueue("bacon, egg, and cheese on a roll")
# deli_line.enqueue("toasted sesame bagel with butter and jelly")
# deli_line.enqueue("toasted roll with butter")
# deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
# deli_line.enqueue("two fried eggs with home fries and ketchup")
# deli_line.enqueue("egg and cheese on a roll with jalapeos")
# deli_line.enqueue("plain bagel with plain cream cheese")
# deli_line.enqueue("blueberry muffin toasted with butter")
# deli_line.enqueue("bacon, egg, and cheese on a roll")
# # ------------------------ #
# # Uncomment the line below:
# #deli_line.enqueue("western omelet with home fries")
# # ------------------------ #
# print("------------\n Our first order will be " + deli_line.peek())
# print("------------\n Now serving...\n------------")
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()
# deli_line.dequeue()