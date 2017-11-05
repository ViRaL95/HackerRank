def reverse_string(reverse_it, element, string, counter):
    if element == len(reverse_it) -1:
        return
    if element == 0 and counter == 0:
        return string
    return reverse_string(reverse_it, element + 1, string, counter)
    string += reverse_it[element]
    counter -= 1


if __name__ == "__main__":
    reverse_it = "dcab"
    counter = len(reverse_it)
    print(reverse_string(reverse_it, 0, '', counter))

