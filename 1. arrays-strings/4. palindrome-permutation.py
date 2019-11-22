def palindrome_permutation(string):
    counter = {}
    for char in counter:
        new_quantity = counter.get(char, 0) + 1
        if new_quantity == 2:
            del counter[char]
        else:
            counter[char] = new_quantity

    return len(counter) <= 1


if __name__ == '__main__':
    print(palindrome_permutation('anita lava la tina'))
    print(palindrome_permutation('atani aval la tina'))
