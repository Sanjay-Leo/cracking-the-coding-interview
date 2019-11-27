def ll_intersection(ll1, ll2):
    shorter_list = ll1 if len(ll1) < len(ll2) else ll2
    longer_list = ll2 if len(ll1) < len(ll2) else ll1

    diff = longer_list - shorter_list

    current_shorter = shorter_list.head
    current_longer = longer_list.head

    for i in range(diff):
        current_longer = current_longer.next

    while current_shorter is not current_longer:
        current_shorter = current_shorter.next
        current_longer = current_longer.next

    return current_longer
