#EDGE CASES: Uneven number of opening and closing brackets but test cases pass: 
#CASE 1: {{}. Contains more opening brackets. Stack will still contain elements after loop
#CASE 2: {}}  Stack will be empty when popping last element. Check that stack is not empty before popping. If it is then you know that there are more closing brackets
import sys

def balanced_brackets(values):
    stack = []
    balanced = []
    comparisons = {'{': '}', '[': ']', '(': ')'}
    for value in values:
        balanced_or_not = "TRUE"
        stack = []
        for expression in value:
            if expression in comparisons.keys():
                stack.append(expression)
            else:
                if stack == []:
                    balanced_or_not = "FALSE"
                elif comparisons[stack.pop()] != expression:
                    balanced_or_not = "FALSE"
        if stack != []:
            balanced_or_not = "FALSE"
        balanced.append(balanced_or_not)
    return balanced


if __name__ == '__main__':
    values = ['{{()}}', '{{', '{{}', '}}', '', '([{{{}}}])']
    print(balanced_brackets(values))
