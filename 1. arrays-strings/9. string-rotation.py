def is_a_rotation(base, rotated):
    for i, char in enumerate(base):
        if char == rotated[-1]:
            # print(base[i + 1:] + base[:i + 1])
            if (base[i + 1:] + base[:i + 1]) == rotated:
                return True
    return False


if __name__ == '__main__':
    print(is_a_rotation('waterbottle', 'erbottlewat'))
