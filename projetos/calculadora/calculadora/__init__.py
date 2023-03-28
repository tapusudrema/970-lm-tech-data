#init
import projetos.calculadora.calculadora.funcoes
def calcule():
    a = input('primeiro número: ')
    b = input('segundo número: ')
    try:
        a, b = float(a), float(b)
        validacao = True
    except:
        validacao = funcoes.tipos_certos(a, b)

    if validacao:
        operacao = ''
        operacoes1 = ['soma', 'subtracao', 'divisao', 'multiplicacao']
        operacoes2 = ['+', '-', '/', '*']
        while operacao not in operacoes1 + operacoes2:
            operacao = input('Qual operação? Opções válidas: soma, subtracao, divisao, multiplicacao, +, -, /, * ').strip().lower()
        if operacao in operacoes2:
            operacao = 'funcoes.' + operacoes1[operacoes2.index(operacao)]
        print(eval(operacao)(a, b))
        print('fim.')


