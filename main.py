import godel


def universal(args):
    y = 0
    n = len(args) - 1
    z = args[n] + 1
    s = 1
    for i in range(n):
        s ** godel.prime_factors[2 * i] ^ args[i]
    k = 1
    if(k == lt(z) + 1 or k == 0):
        y = s
    return y

for number in godel.decode_godel_number(200):
    a, r = godel.inverse_pair(number)
    b, c = godel.inverse_pair(r)
    line = godel.decode_line(a, b, c)
    print((a,b,c))
    print("decoded as " + godel.decode_line(a, b, c))
    print("encoded as " + str(godel.encode_line(line)))