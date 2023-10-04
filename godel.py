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

prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Prime numbers for encoding

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