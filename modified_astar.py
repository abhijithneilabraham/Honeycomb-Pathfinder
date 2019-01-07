#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:33:00 2019

@author: abhijithneilabraham
"""
'''
I am gonna modify A* as per my own rules
'''
length=12#creating dummy value for side of hexagon.side of hexagon is the value that each step of the algorithm takes
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
    

def far(start,end):
    return distance(end[0],start[0],end[1],start[1])
    
def astar(maze, start, end):#maze is contours.start and end are the initial and final coordinates
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    start_node=[120,90] #dummy values for start and end
    end_node=[420,90]
    # Create start and end node
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):#enumerate gives index and the object inside list
            if item.f < current_node.f:
                current_node = item
                current_index = index
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        children = []
        corners=[]#putting this here for reference
        contours=[]#putting this here for reference
        for new_position in corners:
            
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
             
            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)
        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in contours:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + length
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
