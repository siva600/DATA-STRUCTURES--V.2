# 2. Add Two Numbers - LeetCode
class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = ListNode()
        
    def append(self, data):
        new_node = ListNode(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
    
    def display(self):
        data = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            data.append(current_node.data)
        return data

class Solution:
    def to_int(self, l):
        s = ""
        for i in l:
            s += str(i)
        return s
            
    def addTwoNumbers(self, l1, l2):
        a = self.to_int(l1)
        b = self.to_int(l2)
        total_str = str(int(a) + int(b))[::-1]
        obj = LinkedList()
        print(total_str)
        for i in total_str:
            obj.append(int(i))
        return obj.display()
            

resp = Solution()
l1 = [2,3,4]
l2 = [2,3,4]
print(resp.addTwoNumbers(l1,l2))
        