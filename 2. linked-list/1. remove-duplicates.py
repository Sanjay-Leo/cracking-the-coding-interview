from linked_list import LinkedList


def remove_duplicates(ll):
    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next

        if current.next is None:
            ll.tail = current
        current = current.next


if __name__ == '__main__':
    ll = LinkedList(0)
    ll.insert_node(2).insert_node(2).insert_node(2).insert_node(3).insert_node(2).insert_node(2)
    print(ll, ll.tail)
    remove_duplicates(ll)
    print(ll, ll.tail)
