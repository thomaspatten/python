def binarycalc(a, b, operator):
    if operator == "+":
        answer = a + b
    elif operator == "-":
        answer = a - b
    elif operator == "*":
        answer = a * b
    elif operator == "/":
        answer = a / b        

    binarynum = []

    while answer >= 0:
        binarynum.append(answer % 2)
        answer = int(answer / 2)
        if answer == 0:
            break
    
    binarynum.reverse()

    return binarynum
