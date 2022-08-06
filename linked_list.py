class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def __insert_at(self, index, value):
        if index < 0:
            raise IndexError("Index out of range")
        current_head = self.head
        if self.head == None:
            self.head = Node(value)
            self.length += 1
            return self.head
        if index == 0:
            self.head = Node(value)
            self.head.next = current_head
            self.length += 1
            return self.head
        else:
            for _ in range(index - 1):
                current_head = current_head.next
            new_node = Node(value)
            current_head.next = new_node
            self.length += 1
            return new_node
    
    def __nth_index_of(self, value, n):
        if self.head == None:
            return -1
        else:
            current_head = self.head
            index = 0
            while current_head != None:
                if current_head.data == value:
                    index += 1
                    if index == n:
                        return index
                current_head = current_head.next
                index += 1
            return -1
    
    def insert_last(self, value):
        return self.__insert_at(self.length, value)
    
    def insert_first(self, value):
        return self.__insert_at(0, value)

    def first_index_of(self, value):
        return self.__nth_index_of(value, 0)
    
    def last_index_of(self, value):
        return self.__nth_index_of(value, self.length - 1)
    
    def contains(self, value):
        node = Node(value)
        while self.head != None:
            if self.head == node:
                return True
            self.head = self.head.next
        return False
    
    def __remove_at(self, index):
        if index >= self.length or index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            print(self.head)
            self.head = self.head.next
            self.length -= 1
            return self.head
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next
            self.length -= 1
            return current.next
    
    def delete_first(self):
        return self.__remove_at(0)
    
    def delete_last(self):
        return self.__remove_at(self.length - 1)

    def find_at(self, index):
        if index >= self.length or index < 0:
            raise IndexError("Index out of range")
        count = 0
        current = self.head
        while current != None:
            if count == index:
                return current.data
            current = current.next
            count += 1

    def __getitem__(self, index):
        return self.find_at(index)

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_first(1)
    linked_list.insert_first(2)
    linked_list.insert_last(3)
    linked_list.insert_last(4)
    linked_list.insert_last(5)
    linked_list.insert_last(6)
    linked_list.insert_last(7)
    linked_list.insert_first(8)
    for i in range(linked_list.length):
        print(linked_list[i])
    print("Length after insertions: ", linked_list.length)
    linked_list.delete_first()
    linked_list.delete_last()
    linked_list_copy = linked_list
    for i in range(linked_list.length):
        print(linked_list[i])
    print("Length after deletions: ", linked_list.length)
