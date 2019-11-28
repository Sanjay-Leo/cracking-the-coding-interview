class StackNode:
    def __init__(self, value, min_before=float('-inf')):
        self.value = value
        self.min_before = min_before


class StackMin:
    def __init__(self):
        self.stack = []

    def push(self, value):
        new_node = StackNode(value, value)
        if len(self.stack) > 0:
            last_min = self.stack[-1].min_before
            if last_min < new_node.value:
                new_node.min_before = last_min
        self.stack.append(new_node)
        return self

    def pop(self):
        return self.pop()

    def get_min(self):
        return self.stack[-1].min_before


if __name__ == '__main__':
    min_stack = StackMin()
    min_stack.push(1).push(2).push(3).push(4)
    print(min_stack.get_min())
