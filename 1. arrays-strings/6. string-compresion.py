def compress_string(string):
    compressed = ''
    last_char, counter = '', 0
    for char in string:
        if char == last_char:
            counter += 1
        else:
            if counter != 0:
                compressed += last_char + str(counter)
            last_char = char
            counter = 1
    compressed += last_char + str(counter)

    return compressed


if __name__ == '__main__':
    print(compress_string('aabb'))
    print(compress_string('aaaacccc'))
    print(compress_string('aabbscccc'))
