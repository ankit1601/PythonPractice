def count_substring(string, sub_string):
    count = 0
    found_at = -1

    for i in range(len(string)):
        if i <= found_at:
            continue
        found_at = string[i:].find(sub_string)
        if found_at != -1:
            found_at = i + found_at
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count_ = count_substring(string, sub_string)
    print(count_)