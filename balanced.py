def balanced(input_string):
    print(input_string)

    parenCount = 0
    for c in input_string:
        if c == '{':
            parenCount += 1
            continue
        if c == '}':
            if parenCount == 0:
                return False
            parenCount -= 1

    if parenCount == 0:
        return True

    return False

#testing