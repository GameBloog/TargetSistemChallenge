def count_a(s):
    return s.lower().count('a')

string = input("Informe uma string: ")

quantity = count_a(string)
print(f"A letra 'a' aparece {quantity} vezes na string.")
