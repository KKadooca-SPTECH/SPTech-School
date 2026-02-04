# Lista: é MUTÁVEL, ordenado e indexado de 0..n
list = [10,20,30]

# Tupla: é IMUTÁVEL, ordenado e indexado de 0..n
tupla = (10,20,30)

# Dicionário: é MUTÁVEL, ordenado a partir da versão 3.7, e indexado a partir da chave
dicionario = {"num01": 10, "num02": 20, "num03": 30}
dicionario["num02"] = 25

# Matriz: é MUTÁVEL, ordenado e indexado de 0...n / vetor dentro de vetor n vezes
matriz = [[10,20,30],
          [40,50,60],
          [70,80,90]]

print(type(list))
print(type(tupla))
print(type(dicionario))
print(type(matriz))