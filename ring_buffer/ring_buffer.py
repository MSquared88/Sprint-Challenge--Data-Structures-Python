from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == None:
            self.current = self.storage.head
        
        if self.storage.length == self.capacity:
            #make a temp var for self.current
            prev_current = self.current

            #if the current node is the tail 
            if self.current == self.storage.tail:

                self.current = self.storage.head
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)

            else:
                self.current = self.current.next
                prev_current.insert_after(item)
                self.storage.delete(prev_current)
                self.storage.length += 1
        else:
             self.storage.add_to_tail(item)
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        first_node = self.storage.head
        while first_node.next:
            list_buffer_contents.append(first_node.value)
            first_node = first_node.next
        list_buffer_contents.append(self.storage.tail.value)
        return list_buffer_contents



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
