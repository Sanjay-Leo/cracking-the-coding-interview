from linked_list import Node


def del_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


if __name__ == '__main__':
    node = Node(2)
    node.next = Node(3)
    node.next.next = Node(4)

    print(node, node.next)
    del_middle_node(node)
    print(node, node.next)
