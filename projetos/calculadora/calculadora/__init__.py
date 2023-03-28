#init

#aqui meteré las funciones
def soma(a,b):
    if type(a) in [int, float] and type(b) in [int, float]:
        return a + b
    else:
        print(f'Os input `a` e `b` devem ser numéricos, recebido {a}, {type(a)}, {b} {type(b)}')


def subtracao(a,b):
    if type(a) in [int, float] and type(b) in [int, float]:
        return a - b
    else:
        print(f'Os input `a` e `b` devem ser numéricos, recebido {a}, {type(a)}, {b} {type(b)}')


def multiplicacao(a,b):
    if type(a) in [int, float] and type(b) in [int, float]:
        return a * b
    else:
        print(f'Os input `a` e `b` devem ser numéricos, recebido {a}, {type(a)}, {b} {type(b)}')


def divisao(a,b):
    if type(a) in [int, float] and type(b) in [int, float]:
        #divisão de a/b se b != 0; 0 se b = 0  return 0 if b == 0 else a/b
        #Exibe na tela uma mensagem de erro mencionando uma divisão inválida
        if b!=0:
            return a / b
        else:
            print('Divisão inválida, retornando como resultado o valor 0 ')
            return 0
    else:
        print(f'Os input `a` e `b` devem ser numéricos, recebido {a}, {type(a)}, {b} {type(b)}')



def calcule():
    a = input('primeiro número: ')
    b = input('segundo número: ')
    operacao = ''
    operacoes1 = ['soma', 'subtracao', 'divisao', 'multiplicacao']
    operacoes2 = ['+', '-', '/', '*']
    while operacao not in operacoes1 + operacoes2:
        operacao = input('Qual operação? Opções válidas: soma, subtracao, divisao, multiplicacao, +, -, /, * ').strip().lower()
    if operacao in operacoes2:
        operacao = operacoes1[operacoes2.index(operacao)]
    print(eval(operacao)(a, b))
    print('fin')


