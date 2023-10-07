def pair(x, y):
    return 2**x * (2*y + 1) - 1

def inverse_pair(result):
    result += 1
    x = 0
    while result % 2 == 0:
        result //= 2
        x += 1
    y = (result + 1) // 2 - 1
    if(y < 0):
        y = 0
    return x, y

prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

def encode_godel_number(lst):
    if not lst:
        return 0
    
    result = 1
    for i, element in enumerate(lst):
        result *= prime_factors[i % len(prime_factors)] ** (element)
    
    return result

def decode_godel_number(number):
    if number == 0:
        return []
        
    lst = []
    
    for prime in prime_factors:
        if(number != 1):
            power = 0
            while number % prime == 0:
                number //= prime
                power += 1
            lst.append(power)
        else: break
    
    return lst

def decode_line(a, b, c):
    label = ""
    if a > 0:
        letters = "ABCDE"
        label_number = (a - 1) // 5 + 1
        if(label_number == 1):
           label_number = "" 
        label_letter = letters[(a - 1) % 5]
        label = f"[{label_letter}{label_number}]"

    variables = ["Y", "X1", "Z1", "X2", "Z2", "X3", "Z3"]
    variable = variables[c]

    if b == 0:
        type = f"{variable} ← {variable}"
    elif b == 1:
        type = f"{variable} ← {variable} + 1"
    elif b == 2:
        type = f"{variable} ← {variable} - 1"
    else:
        label_number = b - 2
        type = f"IF {variable} != 0 GOTO [{label_letter}{label_number}]"

    line = f"{label} {type}"

    return line

def encode_line(line):
    # Split the line into parts (label and type)
    parts = line.split()
    label = parts[0]
    statement = []

    # Initialize variables
    a = 0
    b = 0
    c = 0

    # Decode the label (if present)
    if label.startswith("[") and label.endswith("]"):
        label_text = label[1:-1]
        if len(label_text) == 1:
            label_letter = label_text
            label_number = 1
        else:
            label_letter = label_text[0]
            label_number = label_text[1:]
        letters = "ABCDE"
        a = (letters.index(label_letter) + 1) + (int(label_number) - 1) * 5
        statement = parts[1:]
    else:
        statement = parts[0:]

    # Decode the type
    variable = statement[0]
    operator = statement[1]

    
    if len(statement) == 5:
        if operator == "←" and f"{statement[2]} {statement[3]} {statement[4]}" == f"{variable} + 1":
            b = 1
        elif operator == "←" and f"{statement[2]} {statement[3]} {statement[4]}" == f"{variable} - 1":
            b = 2
    elif operator == "←":
        b = 0
    elif operator == "IF":
        # Extract the label number
        label_letter = statement[3][1]
        label_number = statement[3][2:-1]
        label_index = letters.index(label_letter) + 1
        b = label_index + int(label_number) * 5 + 2

    # Decode the variable
    variables = ["Y", "X1", "Z1", "X2", "Z2", "X3", "Z3"]
    c = 0
    if(variable[0] == "Y"):
        c = 0
    elif(variable[1] == "X"):
        if(len(variable == 2)):
            c = int(variable[2]) * 2 - 1
        else:
            c = 1
    elif(variable[1] == "Z"):
        if(len(variable == 2)):
            c = int(variable[2]) * 2
        else:
            c = 2

    return a, b, c