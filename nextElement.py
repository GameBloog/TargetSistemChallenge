def proximo_elemento_a():
    # Sequência de números ímpares consecutivos
    sequencia = [1, 3, 5, 7]
    proximo = sequencia[-1] + 2
    print("a) Próximo elemento:", proximo)

def proximo_elemento_b():
    # Sequência de potências de 2
    sequencia = [2, 4, 8, 16, 32, 64]
    proximo = sequencia[-1] * 2
    print("b) Próximo elemento:", proximo)

def proximo_elemento_c():
    # Sequência de quadrados perfeitos
    sequencia = [0, 1, 4, 9, 16, 25, 36]
    proximo = (len(sequencia))**2
    print("c) Próximo elemento:", proximo)

def proximo_elemento_d():
    # Sequência de quadrados de números pares
    sequencia = [4, 16, 36, 64]
    proximo = (len(sequencia) * 2 + 2) ** 2
    print("d) Próximo elemento:", proximo)

def proximo_elemento_e():
    # Sequência de Fibonacci
    sequencia = [1, 1, 2, 3, 5, 8]
    proximo = sequencia[-1] + sequencia[-2]
    print("e) Próximo elemento:", proximo)

def proximo_elemento_f():
    # Sequência de números consecutivos com saltos
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    proximo = sequencia[-1] + 1
    print("f) Próximo elemento:", proximo)

# Chamando as funções para calcular e imprimir o próximo elemento
proximo_elemento_a()
proximo_elemento_b()
proximo_elemento_c()
proximo_elemento_d()
proximo_elemento_e()
proximo_elemento_f()
