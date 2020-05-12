# linked_list.py
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================


'''
**********************************************************************************
Part1: Deque and Bag implemented with Linked List
**********************************************************************************
'''

class SLNode:
    def __init__(self):
        self.next = None
        self.data = None


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a head and tail node with None data
        """
        self.head = SLNode()
        self.tail = SLNode()
        self.head.next = self.tail

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just return []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head.next != self.tail:             
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out


    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        if index < 0:
            raise IndexError("Index out of bounds")
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        current = self.head
        if current.next is self.tail or current.next is None:   # if list is empty
            new_link.next = self.tail   # set next node to tail
            current.next = new_link     # add new link after head
        elif index == 0:                # if we want to insert at first position
            new_link.next = current.next    
            self.head.next = new_link
        else:
            for i in range(index):
                current = current.next  # advance to next node
                if (current.next is self.tail or current.next is None):
                    raise IndexError("Index out of bounds")
            new_link.next = current.next
            current.next = new_link

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """
        prev = None
        current = self.head
        next_link = current.next
        if next_link is self.tail:
            raise IndexError("Index out of bounds")
        if index == 0:
            current = next_link
            self.head.next = current.next
            current = None
        else:
            for i in range(index + 1):
                if (next_link is self.tail or next_link is None):
                    raise IndexError("Index out of bounds")
                prev = current
                current = next_link
                next_link = current.next
            prev.next = next_link
            current = None
           
    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        next_link = self.head.next
        new_link.next = next_link
        self.head.next = new_link

    def add_back(self, data):
        """
        Adds a new node before the tail that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        new_link.next = self.tail
        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = new_link

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        if self.head.next == self.tail:
            return None
        else:
            return self.head.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        if self.head.next == self.tail:
            return None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            return current.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        if self.head.next == self.tail:
           return
        else:
            self.remove_link(0)

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        if self.head.next == self.tail:
           return
        else:
            previous = None
            current = self.head
            while current.next != self.tail:
                previous = current
                current = current.next
            previous.next = self.tail
            current = None


    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        return self.head.next == self.tail

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        if self.head.next == self.tail:
           return False
        else:
            current = self.head
            while current != self.tail:
                current = current.next
                if current.data == value:
                    return True
            return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        if self.head.next is not self.tail:
            prev = None
            current = self.head
            next_link = current.next
            
            while next_link is not self.tail:
                prev = current
                current = next_link
                next_link = current.next
                if current.data == value:
                    prev.next = next_link
                    current = None
                    return


'''
**********************************************************************************
Part 2: Deque implemented with CircularlyDoublyLinked List
**********************************************************************************
'''

class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None

class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a single sentinel node containing None data
        """
        self.sentinel = DLNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 <-> value2 <-> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.sentinel.prev != self.sentinel:             
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.data)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        if index < 0:
            raise IndexError("Index out of bounds")

        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        current = self.sentinel.next

        if index == 0:
            new_link.prev = self.sentinel
            new_link.next = current
            self.sentinel.next = new_link
            current.prev = new_link
        else:
            for i in range(index - 1):
                current = current.next
                if current.next is self.sentinel:
                    raise IndexError("Index out of bounds")
            new_link.prev = current
            new_link.next = current.next
            current.next.prev = new_link
            current.next = new_link


    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """
        if index < 0:
            raise IndexError("Index out of bounds")

        current = self.sentinel.next

        if index == 0:
            if current.next == self.sentinel:   # if only one node in list
                self.sentinel.prev = self.sentinel
                self.sentinel.next = self.sentinel
            else:
                self.sentinel.next = current.next
                current.next.prev = self.sentinel
            current = None
            
        else:
            for i in range(index):
                if current.next is self.sentinel:
                    raise IndexError("Index out of bounds")
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev

    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        self.add_link_before(data, 0)

    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data
        new_link.prev = self.sentinel.prev
        new_link.next = self.sentinel
        self.sentinel.prev.next = new_link
        self.sentinel.prev = new_link

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        return self.sentinel.next.data


    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        return self.sentinel.prev.data


    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        self.remove_link(0)


    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """
        last_node = self.sentinel.prev
        self.sentinel.prev = last_node.prev
        self.sentinel.prev.next = last_node.prev


    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        return self.sentinel.prev == self.sentinel


    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """
        if self.sentinel.next == self.sentinel:
           return False
        else:
            current = self.sentinel.next
            while current is not self.sentinel:
                current = current.next
                if current.data == value:
                    return True
            return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """
        if self.sentinel.next is not self.sentinel:
            current = self.sentinel.next
            while current.next is not self.sentinel:
                if current.data == value:
                    current.prev.next = current.next
                    current = None
                    return
                current = current.next


    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new links to do so.
        (e.g. you cannot call DLNode()). If the list printed by following next was 0, 1, 2, 3,
        after the call it will be 3,2,1,0
        """

        if self.sentinel.next is not self.sentinel:
            new_head = None
            head = self.sentinel.next
            tail = self.sentinel.prev
            current = tail
            if head is not tail:    # if list is longer than 1 node
                while(current.prev is not self.sentinel):
                    self.add_back(current.data)
                    if current == tail:     # on first pass, save new head node
                        new_head = self.sentinel.prev
                    current = current.prev
                    current.next = None
                self.add_back(current.data)
                self.sentinel.next = new_head
            
            
