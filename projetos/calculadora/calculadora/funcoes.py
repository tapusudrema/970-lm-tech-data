#aqui meteré las funciones
def soma(a,b):
    if type(a) in [int, float] and type(b) in [int, float]:
        return a + b
    else:
        print(f'Os input `a` e `b` devem ser numéricos, recebido {a}, {type(a)}, {b} {type(b)}')


