def count_substrings_same_first_last_character(string):
    """ This method counts the substrings with the same first and last character.
    """
    count = 0
    for index, element in enumerate(string):
        for index2 in range(index, len(string)):
            substring = string[index : index2 + 1]
            if substring.endswith(substring[0]):
                count += 1   
    return count

def count_unique_substrings_same_first_last_character(string):
    """ This method counts the unique substrings using the same first and last character
    """
    count = 0
    hash_set = set()
    for index, element in enumerate(string):
        for index2 in range(index, len(string)):
            substring = string[index : index2 + 1]
            if substring.endswith(substring[0]) and substring not in hash_set:
                hash_set.add(substring)
                count += 1   
    return count





if __name__ == '__main__':
    count = count_substrings_same_first_last_character("abcab")
    print(count)
    count = count_unique_substrings_same_first_last_character("abcab")
    print(count)

