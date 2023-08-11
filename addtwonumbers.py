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

    def insert_beginning(self, new_value):
        new_node = ListNode(new_value)
        new_node.set_next(self.head_node)
        self.head_node = new_node

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
           list1.insert_beginning(i) 
        for i in l2:
            list2.insert_beginning(i)
        print(list1.stringify_list())
        print(list2.stringify_list())

        node1 = list1.get_head_node()
        node2 = list2.get_head_node()

        while node1 and node2 != None:
            x = node1.get_val() + node2.get_val()
            if x >= 10:
                y = x % 10
                list3.insert_beginning(y)
                node1 = node1.get_next_node()
                node2 = node2.get_next_node()
                x = node1.get_val() + node2.get_val() + 1
                list3.insert_beginning(x)
                node1 = node1.get_next_node()
                node2 = node2.get_next_node()
            else:
                list3.insert_beginning(x)
                node1 = node1.get_next_node()
                node2 = node2.get_next_node()

        return print(list3.stringify_list())

l1 = [2, 4, 3]
l2 = [5, 6, 4]

Solution().addTwoNumbers(l1, l2)
