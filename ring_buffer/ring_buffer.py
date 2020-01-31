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
                #set current to head
                self.current = self.storage.head

                #remove the tail item
                self.storage.remove_from_tail()

                #add the new tail
                self.storage.add_to_tail(item)

            else:
                #set the current to the next item
                self.current = self.current.next

                #insert the new item where the prev item was
                prev_current.insert_after(item)

                #delete the prev item
                self.storage.delete(prev_current)

                # insert after dosent add to the DLL size
                #TODO refacture to not do this
                self.storage.length += 1
        else:
             self.storage.add_to_tail(item)
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        
        #make a var for the head
        first_node = self.storage.head

        #while there is a next node
        while first_node.next:
            #append the node to the list
            list_buffer_contents.append(first_node.value)

            # got to the next node
            first_node = first_node.next

        # since the while loop stops on the last node I just 
        # appened the tail to the list
        # TODO there is probably a better way to do this    
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
