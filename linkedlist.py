class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

  def remove_by_key(self, value_to_remove):
    current_node = self.get_head_node()
    prev_node = None
    while current_node and current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
      current_node = self.get_head_node()
    
    while current_node:
      while current_node.get_value() != value_to_remove:
        pre_node = current_node
        current_node = current_node.get_next_node()
      if not current_node:
        return self.get_head_node()
      pre_node.next_node = current_node.get_next_node()
      current_node = pre_node

      return current_node

  def swap_nodes_by_value(self, va1, va2):
    if va1 == va2:
      print("Elements are the same - no swap needed!")
      return
    
    node1 = self.get_head_node()
    node2 = self.get_head_node()
    node1_prev = None
    node2_prev = None

    while node1 != None:
      if node1.get_value() == va1:
        break
      node1_prev = node1
      node1 = node1.get_next_node()

    while node2 != None:
      if node2.get_value() == va2:
        break
      node2_prev = node2
      node2 = node2.get_next_node()

    if (node1 is None or node2 is None):
      print("Swap note possible - one or more element is not in the list.")
      return  
    
    if node1_prev == None:
      self.head_node = node2
    else:
      node1_prev.set_next_node(node2)

    if node2_prev == None:
      self.head_node = node1
    else:
      node2_prev.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)
  
  def return_nth_last(self, n):
    nth_last = None
    count = 1
    tail_point = self.get_head_node()

    while tail_point:
      tail_point = tail_point.get_next_node()
      count += 1

      if count >= n + 1:
        if nth_last == None:
          nth_last = self.get_head_node()
        else:
          print(nth_last.get_value())
          nth_last = nth_last.get_next_node()

    return nth_last.get_value()
  
  def return_middle(self):
    fast_pointer = self.get_head_node()
    slow_pointer = self.get_head_node()

    while fast_pointer:
      fast_pointer = fast_pointer.get_next_node()
      if fast_pointer != None:
        fast_pointer = fast_pointer.get_next_node()
        slow_pointer = slow_pointer.get_next_node()
    
    return slow_pointer.get_value()
    
    
    

"""
phrase = LinkedList('hell')
phrase.insert_beginning('what')
phrase.insert_beginning('the')
phrase.insert_beginning('what')
phrase.insert_beginning('what')
phrase.insert_beginning('what')
phrase.swap_nodes_by_value('the', 'hell')
print(phrase.stringify_list())
"""

list1 = LinkedList()

for i in range(1, 8):
  list1.insert_beginning(i)

print(list1.stringify_list())
print(list1.return_middle())
