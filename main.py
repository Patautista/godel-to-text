import godel

# Exemplo de uso da função:
for number in godel.decode_godel_number(200):
    a, r = godel.inverse_pair(number)
    b, c = godel.inverse_pair(r)
    print(godel.gerar_linha_de_codigo(a, b, c))