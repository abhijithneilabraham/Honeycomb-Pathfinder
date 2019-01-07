#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:33:00 2019

@author: abhijithneilabraham
"""
'''
I am gonna modify A* as per my own rules
'''

def distance(x,y,a,b):
    return (((a-x)**2)+((b-y)**2))**.5
print(distance(3,4))

'''
now I need a function to move to the shortest path
'''
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
start=[20,30] 

end=[100,200]
def far(start,end):
    return distance(end[0],start[0],end[1],start[1])
    
def astar(maze, start, end):#maze is contours.start and end are the initial coordinates
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    start_node=[]
    end_node=[]
    # Create start and end node
  
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(far(start,end))
    
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index