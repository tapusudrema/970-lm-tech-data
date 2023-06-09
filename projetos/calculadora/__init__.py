#init
from funcoes import tipos_certos, soma, subtracao, multiplicacao, divisao
dictFuncoes = {
    'soma': soma, '+': soma,
    'subtracao': subtracao, '-': subtracao,
    'divisao': divisao, '/': divisao,
    'multiplicacao': multiplicacao, '*': multiplicacao
}
def calcule():
    a = input('primeiro número: ')
    b = input('segundo número: ')
    try:
        a, b = float(a), float(b)
        validacao = True
    except:
        validacao = tipos_certos(a, b)

    if validacao:
        metodo1(a, b)
        metodo2(a, b, dictFuncoes)
    print('fim.')

def metodo1(a, b):
    operacao = ''
    print('Usando listas e eval():')
    operacoes1 = ['soma', 'subtracao', 'divisao', 'multiplicacao']
    operacoes2 = ['+', '-', '/', '*']
    while operacao not in operacoes1 + operacoes2:
        operacao = input(
            'Qual operação? Opções válidas: soma, subtracao, divisao, multiplicacao, +, -, /, * ').strip().lower()
    if operacao in operacoes2:
        operacao = operacoes1[operacoes2.index(operacao)]
    print(eval(operacao)(a, b))


def metodo2(a, b, dictio):
    print('Usando dicionário:')
    operacao = ''
    while operacao not in dictio.keys():
        operacao = input(
            'Qual operação? Opções válidas: soma, subtracao, divisao, multiplicacao, +, -, /, * ').strip().lower()
    print(dictio[operacao](a, b))
