class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

    def get_val(self):
        return self.val

    def get_next_node(self):
        return self.next
        
    def set_next(self, next):
        self.next = next
        
class LinkedList(object):
    def __init__(self, value=None):
        self.head_node = value

    def get_head_node(self):
        return self.head_node

    def insert_end(self, new_value):
        new_node = ListNode(new_value)
        current_node = self.get_head_node()
        new_node.set_next(None)
        if self.head_node == None:
            self.head_node = new_node
            return
        while current_node.get_next_node() != None:
            current_node = current_node.get_next_node()
        current_node.set_next(new_node)

    def stringify_list(self):
        stringlist = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_val() != None:
                stringlist += str(current_node.get_val()) + '\n'
            current_node = current_node.get_next_node()
        return stringlist

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = LinkedList()
        list2 = LinkedList()
        list3 = LinkedList()
        for i in l1:
           list1.insert_end(i) 
        for i in l2:
            list2.insert_end(i)
        print(list1.stringify_list())
        print(list2.stringify_list())

        node1 = list1.get_head_node()
        node2 = list2.get_head_node()

        while node1 and node2 != None:
            x = node1.get_val() + node2.get_val()
            #print(x)
            if x >= 10:
                y = x % 10
                list3.insert_end(y)
                #print(y)
                node1 = node1.get_next_node()
                node2 = node2.get_next_node()
                x = node1.get_val() + node2.get_val() + 1
                #print(x)
                list3.insert_end(x)
                node1 = node1.get_next_node()
                node2 = node2.get_next_node()
            else:
                list3.insert_end(x)
                node1 = node1.get_next_node()
                node2 = node2.get_next_node()

        return print(list3.stringify_list())

l1 = [2, 4, 3]
l2 = [5, 6, 4]

Solution().addTwoNumbers(l1, l2)
