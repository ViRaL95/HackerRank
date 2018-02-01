def find_kth_non_repeating_character(string, k):
    """This method finds the kth non repeating character in a given string.
    It first creates a hash_map and inputs all characters into it, with its
    respective count. It then iterates through the string again to find the
    kth element in the hash_map with count 1

    Absurd Thoughts: I initially though I could iterate through the hash_map
    to find the kth occurence where a letter occurs only once, but remember 
    the hash_map sorts its data by key so you will not find the correct kth 
    occurence but rather alphabetically the kth occurrence

    Another thought was that I should use a set instead, thinking that the
    set will not include the second element twice. However in this case the
    set will just contain all elements of the string, which is not very
    useful
    """
    
    hash_map  = {}
    for element in string:
        if element in hash_map:
            hash_map[element] += 1
        else:
            hash_map[element] = 1
    count = 1
    
    for element in string:
        if hash_map[element] == 1:
            if count == k:
                return element
            count += 1
 

if __name__ == '__main__':
    print(find_kth_non_repeating_character("geeksforgeeks", 3))
    print(find_kth_non_repeating_character("geekforgeeks", 2))
    print(find_kth_non_repeating_character("geeksforgeeks", 4))
