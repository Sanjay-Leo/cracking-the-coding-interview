from itertools import permutations


def check_permutation(string1, string2):  # Time: O (n + m) and Space O(n), being n string 1 and m string 2
    counter1 = {}
    for char in string1:
        counter1[char] = counter1.get(char, 0) + 1

    for char in string2:
        if char in counter1 and counter1[char] > 0:
            new_char_quantity = counter1.get(char) - 1
            counter1[char] = counter1.get(char) - 1
            if new_char_quantity == 0:
                del counter1[char]
        else:
            return False

    return len(counter1) == 0


if __name__ == '__main__':
    print(check_permutation('joan', 'jona'))
    print(check_permutation('joan', 'naoj'))
    print(check_permutation('joan', 'noja'))
    print(check_permutation('joan', 'nojas'))
    print(check_permutation('joan', 'nojaaaa'))
