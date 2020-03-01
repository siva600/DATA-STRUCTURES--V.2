class Tree:
    def __init__(self, initial=None):
        self.value = initial
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return()
    def is_empty():
        return (self.value == None)


    def inorder(self):
        if self.is_empty():
            return ([])
        else:
            return(self.left.inorder() + self.value + self.right.inorder())
    def __str__():
        return str(self.inorder())


