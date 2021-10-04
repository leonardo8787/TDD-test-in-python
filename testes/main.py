from calcula import soma
#testando resultados da calculadora
print('Usando números')
print(soma(10, 20))
print(soma(-10, 20))
print(soma(1.5, 2.5))

print('-------------------------')
try:
    print(soma('15', 15))
except TypeError as e:
    print('Conta inválida, string detectada')
    print(e)
print('-------------------')

#print(soma('15', 2))

print('OI')
print('--------------------')

print('Conta', soma(25, 25))

print('--------------------')
"""
try:
    print(soma('15', 15))
except AssertionError as e:
    print(f'Conta inválida: {e}')
"""
print(soma(1,1))

