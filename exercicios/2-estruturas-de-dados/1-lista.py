# Crie uma lista apenas com elementos numéricos
numeros = [1,2,3,4,5,6,7,8,9,10]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
variado = [20, 7.77, 'String', False, [10,20,30], numeros, None]
# Imprima na tela apenas os 5 primeiros elementos da lista
print(variado[:5])
print(variado)
print(type(variado[6]))

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(variado[::2])
# Remova da lista o último item
variado.pop()
print(variado)
# Insira na lista um novo item
variado.append("Item novo")
print(variado)
# Remova da lista um item específico
variado.remove(False)
print(variado)