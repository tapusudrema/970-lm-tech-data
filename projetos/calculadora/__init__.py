#init
from funcoes import tipos_certos, soma, subtracao, multiplicacao, divisao
dictFuncoes = {
    'soma': soma,
    'subtracao': subtracao,
    'divisao': divisao,
    'multiplicacao': multiplicacao,
    '+': soma,
    '-': subtracao,
    '/': divisao,
    '*': multiplicacao
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
        metodo1(a,b)
        metodo2(a,b,dictFuncoes)

def metodo1(a, b):
    operacao = ''
    operacoes1 = ['soma', 'subtracao', 'divisao', 'multiplicacao']
    operacoes2 = ['+', '-', '/', '*']
    while operacao not in operacoes1 + operacoes2:
        operacao = input(
            'Qual operação? Opções válidas: soma, subtracao, divisao, multiplicacao, +, -, /, * ').strip().lower()
    if operacao in operacoes2:
        operacao = operacoes1[operacoes2.index(operacao)]
    print(eval(operacao)(a, b))
    print('fim.')

def metodo2(a, b, dictio):
    operacao = ''
    while operacao not in dictio.keys():
        operacao = input(
            'Qual operação? Opções válidas: soma, subtracao, divisao, multiplicacao, +, -, /, * ').strip().lower()
    print(dictio)