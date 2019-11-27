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

    def __len__(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter
