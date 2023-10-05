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

def gerar_linha_de_codigo(a, b, c):
    # Primeiro, vamos tratar a parte do rótulo
    rotulo = ""
    if a > 0:
        letras = "ABCDE"
        numero_rotulo = (a - 1) // 5 + 1
        if(numero_rotulo == 1):
           numero_rotulo = "" 
        letra_rotulo = letras[(a - 1) % 5]
        rotulo = f"[{letra_rotulo}{numero_rotulo}]"

    # Agora, vamos tratar a parte da variável
    variaveis = ["Y", "X1", "Z1", "X2", "Z2", "X3", "Z3"]  # Lista de variáveis
    variavel = variaveis[c]

    # Em seguida, tratamos o tipo de declaração
    if b == 0:
        tipo = f"{variavel} ← {variavel}"
    elif b == 1:
        tipo = f"{variavel} ← {variavel} + 1"
    elif b == 2:
        tipo = f"{variavel} ← {variavel} - 1"
    else:
        numero_rotulo = b - 2
        tipo = f"IF {variavel} != 0 GOTO [{letra_rotulo}{numero_rotulo}]"

    # Combinamos todas as partes em uma linha de código
    linha_de_codigo = f"{rotulo} {tipo}"

    return linha_de_codigo