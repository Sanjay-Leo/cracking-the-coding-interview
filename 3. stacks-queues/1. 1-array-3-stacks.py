class ThreeStacks:
    def __init__(self):
        self.stacks = []
        self.top1 = 0
        self.top2 = 0

    def push(self, stack_id, value):
        if stack_id == 1:
            self.stacks.insert(self.top1, value)
            self.top1 += 1
            self.top2 += 1
        elif stack_id == 2:
            self.stacks.insert(self.top2, value)
            self.top2 += 1
        else:  # stack_id = 3
            self.stacks.append(value)
        return self

    def pop(self, stack_id):
        if stack_id == 1:
            return_value = self.stacks[self.top1 - 1]
            del self.stacks[self.top1 - 1]
            self.top1 -= 1
            self.top2 -= 1
            return return_value
        elif stack_id == 2:
            return_value = self.stacks[self.top2 - 1]
            del self.stacks[self.top2 - 1]
            self.top2 -= 1
            return return_value
        else:  # stack_id = 3
            return self.stacks.pop()

    def __repr__(self):
        return str(self.stacks)


if __name__ == '__main__':
    stacks = ThreeStacks()
    stacks.push(1, 0).push(2, 1).push(3, 2).push(1, 4).push(2, 5).push(3, 6)
    print(stacks)
    stacks.pop(1)
    stacks.pop(2)
    stacks.pop(3)
    print(stacks)
