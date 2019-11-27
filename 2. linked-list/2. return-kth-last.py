from linked_list import LinkedList


def return_kth_last(head, k):
    counter = 1
    first = second = head
    while counter <= k and second:
        counter += 1
        second = second.next

    if second is None:
        return None

    while second:
        first = first.next
        second = second.next
    return first


if __name__ == '__main__':
    ll = LinkedList(0)
    ll.insert_node(2).insert_node(2).insert_node(2).insert_node(3).insert_node(2)
    print(return_kth_last(ll, 3))
