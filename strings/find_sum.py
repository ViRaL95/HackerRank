#abc123def456
def find_sum(string):
    index = 0
    sum_of_elements = 0
    for element in string[::-1]:
        try:
            value = int(element)
            sum_of_elements += value*(10**index)
            index+=1
        except ValueError:
            index = 0
            continue
    return sum_of_elements

if __name__ == '__main__':
    string = "abc123def456"
    print(find_sum(string))

