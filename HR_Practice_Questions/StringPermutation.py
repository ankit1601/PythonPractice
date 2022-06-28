# Check if two strings are permutation of each other


def is_permutation(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    if len_str1 != len_str2:
        return False
    sorted_str1 = "".join(sorted(str1))
    sorted_str2 = "".join(sorted(str2))

    if sorted_str1 != sorted_str2:
        return False

    return True


if __name__ == '__main__':
    string1 = input()
    string2 = input()
    print(is_permutation(string1, string2))

    # inbuilt function return an
    # integer representing the Unicode code
    value = ord("A")

    # writing in ' ' gives the same result
    value1 = ord('a')

    # prints the unicode value
    print(value, value1)
    print(chr(97))