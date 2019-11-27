from linked_list import LinkedList


def sum_lists(l1, l2):
    current1 = l1.head
    current2 = l2.head

    sums = []
    while current1 and current2:
        sums.append(current1.value + current2.value)
        current1 = current1.next
        current2 = current2.next

    if current2 and current1 is None:
        while current2:
            sums.append(current2.value)
            current2 = current2.next
    if current1 and current2 is None:
        while current1:
            sums.append(current1.value)
            current1 = current1.next

    result = ''
    print(sums)
    for i, item in enumerate(sums):
        if item < 10:
            result = str(item) + result
        else:
            result = str(item)[-1] + result
            if i < len(sums) - 1:
                sums[i + 1] += int(str(item)[:-1])
            else:
                result = str(item)[:-1] + result

    print(result)


if __name__ == '__main__':
    l1 = LinkedList(1)
    l1.insert_list([2, 3, 4, 5, 6])

    l2 = LinkedList(2)
    l2.insert_list([3, 4, 5, 6, 7, 9, 11])

    sum_lists(l1, l2)
