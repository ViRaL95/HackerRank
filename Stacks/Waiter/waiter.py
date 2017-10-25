#!/bin/python3

import sys

n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
number = list(map(int, input().strip().split(' ')))
#this is the nth prime number essentially this should stop when it hits the iteration number
nth_prime_number = 0
#this is the first variable we are checking to see if prime or not 
check_this_number = 2
#this is the prime # we are looking for
prime_number = 0
B = []
for iteration in range(1, q + 1):
    #compute iteration'th prime
    temp_b = []
    while (True):
        prime = True
        for index in range(2, check_this_number + 1):
            if check_this_number % index == 0 and index != check_this_number:
                prime = False
                break
        if (prime):
            nth_prime_number += 1
            if nth_prime_number == iteration:
                prime_number = check_this_number
                check_this_number += 1
                break;
        check_this_number += 1
    for index, element in reversed(list(enumerate(number))):
        if(element % (check_this_number - 1) == 0):
            number.pop(index)
            temp_b.append(element)
    temp_b.reverse()
    B = B + temp_b
for element in B:
    print(element)
for element in reversed(number):
    print(element)
