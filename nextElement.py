def next_element_a():
    sequencia = [1, 3, 5, 7]
    next = sequencia[-1] + 2
    print("a) Próximo elemento:", next)

def next_element_b():
    sequencia = [2, 4, 8, 16, 32, 64]
    next = sequencia[-1] * 2
    print("b) Próximo elemento:", next)

def next_element_c():
    sequencia = [0, 1, 4, 9, 16, 25, 36]
    next = (len(sequencia))**2
    print("c) Próximo elemento:", next)

def next_element_d():
    sequencia = [4, 16, 36, 64]
    next = (len(sequencia) * 2 + 2) ** 2
    print("d) Próximo elemento:", next)

def next_element_e():
    sequencia = [1, 1, 2, 3, 5, 8]
    next = sequencia[-1] + sequencia[-2]
    print("e) Próximo elemento:", next)

def next_element_f():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    next = sequencia[-1] + 1
    print("f) Próximo elemento:", next)

next_element_a()
next_element_b()
next_element_c()
next_element_d()
next_element_e()
next_element_f()
