def sort_stack(stack, helper):              
    while stack != []:
        if helper == [] or helper[-1]  <= stack[-1]:
            helper.append(stack.pop())
        else:
            element = stack.pop()
            count = 0
            while helper != [] and helper[-1] > element:
                stack.append(helper.pop())
                count += 1
            helper.append(element)
            while count > 0:
                helper.append(stack.pop())
                count -= 1


if __name__ == '__main__':
    stack = [4,5,0,3,9,1,6,2]
    helper = []
    sort_stack(stack, helper)
    print(helper)
