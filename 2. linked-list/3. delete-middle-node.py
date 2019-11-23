from linked_list import LinkedList

if __name__ == '__main__':
    ll = LinkedList(0)
    ll.insert_node(2).insert_node(2).insert_node(2)
    print(ll)
    ll.del_middle_node(ll.return_kth_last(3))
    print(ll)
