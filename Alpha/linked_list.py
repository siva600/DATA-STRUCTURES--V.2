class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # initially head is 0.
        self.head = ListNode()

    def append(self, data):
        # set new node.
        new_node = ListNode(data)
        # iterate through each node and find out 
        # the node, whose next node is None.
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        # while we get the last node set the new node
        current_node.next = new_node

    def length(self):
        count = 0
        current_node = self.head
        while current_node.next != None:
            count += 1
            current_node = current_node.next
        return count

    def display(self):
        data = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            data.append(current_node.data)
        return data

    def get(self, index):
        if index >= self.length():
            return "Index grater than total data"
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if index == cur_index:
                return cur_node.data
            cur_index += 1

obj = LinkedList()
obj.append(1)
obj.append(2)
obj.append(3)
print("data:", obj.display())
print("length:", obj.length())
print(obj.get(1))
