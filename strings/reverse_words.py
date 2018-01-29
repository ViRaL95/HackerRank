def reverse_words(string):
    final_string = ""
    print("yeah")
    for index, element in enumerate(string[::-1]):
        if element == ' ' or index==len(string) -1:
            if index == len(string) -1:
                d = index
            else:
                d = index + 1
            print("string d is {}".format(string[:(d+1)]))
            for index2, element2 in enumerate(string[:(d+1)]):
                print(element2)
                if element2 == ' ':
                    break
                final_string += element2
            final_string += " "
    return final_string

def reverse_words_in_one_line(string):
    return(' '.join(string.split(" ")[::-1]))

if __name__ == "__main__":
    string = "Blue Is Sky The"
    print(reverse_words(string))
    print(reverse_words_in_one_line(string))
