input_value = input()
enqueue = []
dequeue = []
for index in range(0, int(input_value)):
    input_value = input()
    if (len(input_value.split(" ")) == 2):
        [operation, element] = input_value.split(" ")
    else:
        operation = input_value.split(" ")[0]
    if operation == '1':
        enqueue.append(element)
    elif operation == '2':
        if len(dequeue) == 0:
            while (len(enqueue) > 0):
                popped_element = enqueue.pop()
                dequeue.append(popped_element)
        dequeue.pop()
    elif operation == '3':
        if len(dequeue) == 0:
            while (len(enqueue) > 0):
                popped_element = enqueue.pop()
                dequeue.append(popped_element)
        print(dequeue[len(dequeue) -1])
