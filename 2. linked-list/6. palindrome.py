from linked_list import LinkedList


def is_ll_palindrome(head):
    current = head
    stack = []
    while current:
        if len(stack) > 1 and current.value == stack[-2]:
            stack.pop()
            stack.pop()
        elif len(stack) > 0 and current.value == stack[-1]:
            stack.pop()
        else:
            stack.append(current.value)
        current = current.next

    return len(stack) == 0


if __name__ == '__main__':
    ll = LinkedList(1)
    ll.insert_list([2, 3, 4, 3, 2, 1])
    print(is_ll_palindrome(ll.head))
