# basic node class, consists of left and right child
class Node:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None
  
# bst class
class BST:
  def __init__(self):
    # initialize the root to none
    self.root = None
  
  def insert(self, data):
    # check if root is none
    if self.root is None:
      self.root = Node(data)
    else:
      # if root is not none then compare data with current node data. (helper function)
      self._insert(data, self.root)
  
  def _insert(self, data, current_node):
    # checking left side. If data is < current_node's data:
    if data < current_node.data:
      # if data is less, then pass through left side and check if left node exists..
      if current_node.left is None:
        # if left node is not available then insert the node here.
        current_node.left = Node(data)
      else:
        # if available then recursively check if child nodes to this exists.
        self._insert(data, current_node.left)
    elif data > current_node.data:
      # if the data is grater than current node's data.. then pass through right
      if current_node.right is None:
        # check if current node do not have right child. then insert here
        current_node.right = Node(data)
      else:
        # if current_node have right child check recusively and insert right.
        self._insert(data, current_node.right)
    else:
      # if data == current node's data the do nothing to avoils duplicates.
      print("Value is already present in tree")

  def find(self, data):
    if self.root:
      # check if root exists. If so compare the data with root's data
      is_found = self._find(data, self.root)
      if is_found:
        return True
      return False
    else:
      return None
    
  def _find(self, data, current_node):
    # helper function
    # check if data > current_node's data and current node has right child..
    if data > current_node.data and current_node.right:
      # if available recursively check the right side.
      return self._find(data, current_node.right)
    # check if data < current_node's data and currnet node has left child.
    elif data < current_node.data and current_node.left:
      # if so recursively check the left side
      return self._find(data, current_node.left)
    # if data == currnent node's data then return true (data is found)
    elif data == current_node.data:
      return True


bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.find(10))
print(bst.find(4))

