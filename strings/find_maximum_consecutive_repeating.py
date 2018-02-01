def find_max_consecutive(string):
    """
    This method finds the largest consecutive characters in a string. It does this by
    having a previous and a current 'pointer' which checks if they are equal. If they 
    are equal we can increase a count and check if its value is greater than max_.
    If it is we update the new character that contains the longest consecutive
    characters and update max_.
    If the two characters are not equal we can update the value of the count
    to 1. Count is represented by the variable index in this code.
    """
    index = 1
    count = 0
    max_ = 1
    largest = string[0]
    while count < len(string) - 1:
        prev = string[count]
        current = string[count + 1]
        if prev == current:
            index += 1
        else:
            index = 1
        if index >= max_:
            max_ = index

            largest = string[count]
        count += 1
    return largest


if __name__ == '__main__':
    a = find_max_consecutive("geeekk")
    b = find_max_consecutive("aaaabbccbbb")
    c = find_max_consecutive("ab")
    d = find_max_consecutive("aaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbb")
    print(a)
    print(b)
    print(c)
    print(d)
