#aqui meteré las funciones
def tipos_certos(a, b):
    validacao = type(a) in [int, float] and type(b) in [int, float]
    if validacao:
        return True
    else:
        print(f'Os input `a` e `b` devem ser numéricos, recebido {a}, {type(a)}, {b} {type(b)}')
        return False


def soma(a, b):
    if tipos_certos(a, b):
        return a + b



def subtracao(a, b):
    if tipos_certos(a, b):
        return a - b


def multiplicacao(a, b):
    if tipos_certos(a, b):
        return a * b


def divisao(a, b):
    if tipos_certos(a, b):
        #divisão de a/b se b != 0; 0 se b = 0  return 0 if b == 0 else a/b
        #Exibe na tela uma mensagem de erro mencionando uma divisão inválida
        if b != 0:
            return a / b
        else:
            print('Divisão inválida, retornando como resultado o valor 0 ')
            return 0

