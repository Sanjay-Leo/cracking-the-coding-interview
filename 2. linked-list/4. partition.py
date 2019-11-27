from linked_list import LinkedList


def partition(ll, value):
    current = ll.tail = ll.head

    while current:
        next_node = current.next
        current.next = None
        if current.value < value:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node

    ll.tail.next = None


if __name__ == '__main__':
    ll = LinkedList(0)
    ll.insert_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(ll)
    partition(ll, 5)
    print(ll)
