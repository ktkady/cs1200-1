class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        # Get the size of the left subtree
        left_size = 0
        if self.left is not None:
            left_size = self.left.size  # Size of the left subtree

        # If ind matches the size of the left subtree, return the current node
        if ind == left_size:
            return self
        
        # If ind is less than the left subtree size, recurse into the left subtree
        if ind < left_size:
            return self.left.select(ind) if self.left is not None else None
        
        # If ind is greater, recurse into the right subtree, adjusting the index
        # Here, we subtract the left size and 1 for the current node
        return self.right.select(ind - left_size - 1) if self.right is not None else None # Adjusting index to reflect change in positon 



    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        # The "if self == None" check is unncesseary because it is impossible for self object to be empty
        if self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    
    def insert(self, key):
        # Insert not handles correctly because should have three return statements, so that recursion can operate properly
        # This allows it to run in more efficient time because size is being updated as its being run 
        # This is the problem for which has too long of a runtime 
        if self.key is None:
            self.key = key
            self.size = 1 
            return self 
        elif self.key >= key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.size += 1 
            self.left.insert(key)
            return self 
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.size += 1 
            self.right.insert(key)
            return self 

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''



    def rotate(self, direction, child_side):
        # Assign child node we will be rotating around 
        if child_side == "L": 
            x = self.left
        else: 
            x = self.right
        
        if x is None: 
            return self
        
        # Right rotation 
        if direction == "R": 
            # Find sizes before modification 
            node_size = x.size 
            left_subtree_size = (x.right.size if x.right else 0) + (x.left.right.size if x.left.right else 0) + 1 

            if x.left is None: 
                return self # Right rotation can not occur without left child 
            
            left_subtree = x.left 
            
            x.left = left_subtree.right # Assign left child of OG node to the right subtree of left subtree 
            left_subtree.right = x # Make right subtree of left subtree the OG node

            # Augment size of tree 
            left_subtree.size = node_size 
            x.size = left_subtree_size

            # Reattach back to original tree 
            if child_side == "L": 
                self.left = left_subtree
            else: 
                self.right = left_subtree

            return self 
        
        # Left rotation 
        elif direction == "L": 
            # Find sizes before modification 
            node_size = x.size 
            right_subtree_size = (x.left.size if x.left else 0)+ (x.right.left.size if x.right.left else 0)+ 1 

            if x.right is None: 
                return self # Cannot perform left rotation without right child 
            right_subtree = x.right 

            x.right = right_subtree.left # Set right of OG node to the left side of right subtree 
            right_subtree.left = x # Set left child of right subtree to OG node
            
            # Update sizes 
            right_subtree.size = node_size 
            x.size = right_subtree_size

            # Reattach to tree 
            if child_side == "L": 
                self.left = right_subtree 
            else: 
                self.right = right_subtree 

            return self 

        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self