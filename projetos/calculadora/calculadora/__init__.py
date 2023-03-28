#init
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


