# Função contar com while
def contador_while():
    i = 0

    while i < 10:
        print(i+1)
        i += 1


# Função contar com for
def contador_for():

    for j in range(0, 10):
        print(j+1)


# Percorrendo uma lista
lista = [10, 20, 30, 40, 50, 60]

def percorre_lista():

    print(lista[:])         # Apresenta a lista inteira
    print(lista[0:2])       # Apresenta a lista do índice 0 ao 2
    print(lista[::2])       # Apresenta a lista pulando de 2 em 2
    print(lista[3:])        # Apresenta a lista do índice 3 ao final
    print(lista[::-1])      # Apresenta a lista de trás para frente
    print(lista[3:0:-1])    # Apresenta a lista do índice 3 ao 0, de trás para frente


# Soma de números
numero_a = input("Insira o primeiro número: ")
numero_b = input("Insira o segundo número: ")

soma = int(numero_a) + int(numero_b)

def resultado():
    print(numero_a + " + " + numero_b + " = " + str(soma))


# Chamando funções
print("Contador com while: ")
contador_while()

print("\nContador com for: ")
contador_for()

print("\nApresentando lista: ")
percorre_lista()

print("\nCalculadora de soma: ")
resultado()