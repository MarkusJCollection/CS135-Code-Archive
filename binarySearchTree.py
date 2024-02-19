#BinarySearchTree

from RootTree import *

class BinarySearchTree(RootedTree):
    """A Binary Search Tree. Assumes unique keys"""
    
    def __init__(self,root):
        self.root = root
        self.edgeSet={root:[None,None]}
        self.vertexList =[root]
    
    def addVertex(self):
        return 'Error: addVertex method is invalid for BST. Use addItem'
    
    def addEdge(self):
        return 'Error:addEdge method is invalid for BST. Use addItem'
    
    def addItem(self,item):
        
        if item in self.edgeSet:
            return 'Error: {0} is already in the tree'.format(item)
            
        """adds a new item to the tree"""
        currentVertex=self.root
        added =False
        
        while not added:   #Look for a None child and add the new item
            if item < currentVertex:
                
                if self.edgeSet[currentVertex][0] == None:
                    self.edgeSet[currentVertex][0]=item
                    added=True
                    self.edgeSet[item]=[None,None]
                    self.vertexList.append(item)
                else:
                    currentVertex=self.edgeSet[currentVertex][0]
            else:
                
                if self.edgeSet[currentVertex][1] == None:
                    self.edgeSet[currentVertex][1]=item
                    added=True
                    self.edgeSet[item]=[None,None]
                    self.vertexList.append(item)
                else:
                    currentVertex=self.edgeSet[currentVertex][1]
    
    def findItem(self,item):
        """Returns the depth of item in the tree or -1 if item is not in the tree"""
        currentVertex = self.root
        depth = -1
        searching = True
        while searching:
            if currentVertex == None:
                searching = False
                depth = -1
            elif item == currentVertex:
                depth +=1
                searching = False
            elif item < currentVertex:
                currentVertex = self.edgeSet[currentVertex][0]
                depth +=1
            else:
                currentVertex = self.edgeSet[currentVertex][1]
                depth +=1
        return depth
    
    
        
#Example

data=[56,34,78,67,23,14,33,40,66,25,80]
bs1=BinarySearchTree(data[0])
for item in data[1:]:
    bs1.addItem(item)

def createBST(lst):
    bst = BinarySearchTree(lst[0])
    for x in lst[1:]:
        bst.addItem(x)
    return bst

def dynamic(bst):
    q = int(input('To add an item, enter 0. To find an item, enter 1: '))
    itemType = input('What is your item type? int or str: ')
    item = input('Enter your item: ')
    if itemType == 'int':
            item = int(item)
    if q == 0:
        bst.addItem(item)
        print('\n{0} has been added to the tree.'.format(item))
    else:
        result = bst.findItem(item)
        if result == -1:
            print('\n{0} is not in the tree.'.format(item))
        else:
            print('\n{0} is in the tree at depth {1}.'.format(item,result))
        
    return bst

def process(bst):
    loop = True
    while loop:
        more = input('\nIf you want to work with the tree, enter y: ')
        if more != 'y':
            loop = False
        else:
            bst=dynamic(bst)
    return bst

#process(bs1)













      