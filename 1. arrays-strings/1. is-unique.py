def is_unique(string):
    exists = {}
    for char in string:
        if exists.get(char, False):
            return False
        exists[char] = True
    return True


if __name__ == '__main__':
    print(is_unique('Joan'))
