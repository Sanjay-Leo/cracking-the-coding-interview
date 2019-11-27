from collections import defaultdict


def detect_ll_loop(head):
    visited = defaultdict(list)
    current = head
    while current:
        if current in visited[current.value]:
            return current
        visited[current.value].append(current)
        current = current.next
    return None


if __name__ == '__main__':
    pass
