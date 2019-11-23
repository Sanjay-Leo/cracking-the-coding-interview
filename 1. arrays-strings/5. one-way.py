def one_way(base, modified):  # zero or one editions
    i, j = 0, 0
    editions = 0
    while i < len(base) and j < len(modified):
        if base[i] != modified[j]:
            editions += 1
            if i + 1 < len(base) and base[i + 1] == modified[j]: i += 1
        i += 1
        j += 1
    return editions <= 1

# TODO send improved response
if __name__ == '__main__':
    print(one_way('pale', 'ple'))
    print(one_way('pale', 'bale'))
    print(one_way('pale', 'bake'))
    print(one_way('pale', 'bala'))
