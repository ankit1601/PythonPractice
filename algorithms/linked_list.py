"""
NODE[DATA|LINK to NEXT Node]
Dynamic Memory operation
Complexity O(n)
We have head keep track of current Node
and it should point to first node at the beginning
Tail keep track of last Node
We can create custom function to find
out the number of nodes in Linked List
"""


class Node:
    # constructor

    def __init__(self):
        self.data = None
        self.next = None
        self.head = None
        self.length = 0

    def set_data(self, data):
        """ Method for setting data of current node"""
        self.data = data

    def get_data(self):
        """ Method for getting data of current node"""
        return self.data

    def set_next(self, next_node):
        """ Method for setting next link to next node"""
        self.next = next_node

    def get_next(self):
        """ Method for getting next link to current node"""
        return self.next

    def has_next(self):
        """ Method to check if next Node available"""
        has_next_flag = False
        if self.next:
            has_next_flag = True
        return has_next_flag

    def list_length(self):
        """ Method to check length of list"""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def set_length_list(self):
        """ This method will set counter to latest count of node"""
        pass

    def insert_at_beginning(self, data):
        """ This method is to insert at beginning"""
        new_node = Node()
        new_node.set_data(data)

        if self.length == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1


if __name__ == '__main__':
    new_node1 = Node()
    new_node1.insert_at_beginning(1)
    # print(new_node1.list_length())
    new_node1.insert_at_beginning(2)
    # print(new_node1.list_length())
    new_node1.insert_at_beginning(3)
    new_node1.insert_at_beginning(4)
    new_node1.insert_at_beginning(5)

    if new_node1.head:
        print(new_node1.head.data)
        next_node = new_node1.head
        while next_node.has_next():
            next_node = next_node.get_next()
            print(next_node.data)









