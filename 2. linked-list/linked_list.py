class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = Node(value)

    def insert_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.tail = new_node

        return self

    def insert_list(self, values):
        for value in values:
            self.insert_node(value)

    def remove_duplicates(self):
        pass

    def return_kth_last(self, k):
        counter = 1
        first = second = self.head
        while counter <= k and second:
            counter += 1
            second = second.next

        if second is None:
            return None

        while second:
            first = first.next
            second = second.next
        return first

    def del_middle_node(self, node):
        node.value = node.next.value
        node.next = node.next.next

    def insert_head(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head = node

    def insert_tail(self, value):
        node = Node(value)
        if self.tail is None:
            self.insert_head(node.value)
            return

        self.tail.next = node
        self.tail = node

    def __repr__(self):
        if self.head is None:
            return 'None'

        statement = ''
        current = self.head
        while current:
            statement += str(current.value)
            current = current.next
            if current:
                statement += ' -> '

        return statement
