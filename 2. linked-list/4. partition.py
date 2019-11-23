from linked_list import LinkedList


def partition(ll, value):
    current = ll.tail = ll.head

    while current:
        if current.value < value:
            ll.insert_head(current.value)
        else:
            ll.insert_tail(current.value)
        current = current.next

    ll.tail.next = None


if __name__ == '__main__':
    ll = LinkedList(0)
    # ll.insert_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll.insert_list([2])
    ll.insert_head(-1)
    ll.insert_tail(11)
    print(ll)
    partition(ll, 5)
    print(ll)
