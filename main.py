import godel

# Exemplo de uso da função:
for number in godel.decode_godel_number(200):
    a, b = godel.inverse_pair(number)
    print((a,  godel.inverse_pair(b)))