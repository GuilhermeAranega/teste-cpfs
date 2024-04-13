import csv
import os
import sys
from print_color import print

r = 's'
cpfs = []
nValidos = 0
nInvalidos = 0
nCpfs = 0
jaTestado = False

# ? Verifica se foi passado um argumento e se o arquivo existe, se sim, lê o arquivo e armazena os cpfs para testar
if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        cpfsParaTestar = []
        with open('testarCpfs.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cpfsParaTestar.append(row)

# ? Verifica se o arquivo "cpfs.csv" existe, se sim, lê o arquivo e armazena os cpfs já testados
if os.path.exists('cpfs.csv'): 
    with open('cpfs.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cpfs.append(row)

# ? Função para gerar o primeiro dígito verificador
def gerarPrimeiroDigito(cpfInicial):
    multiDigitoUm = 10
    cpfSomado = 0

    for i in cpfInicial:
        cpfSomado += int(i) * multiDigitoUm
        multiDigitoUm -= 1

    restoDigitoUm = cpfSomado % 11

    if restoDigitoUm < 2:
        primeiroDigitoGerado = 0
    else:
        primeiroDigitoGerado = 11 - restoDigitoUm

    return primeiroDigitoGerado

# ? Função para gerar o segundo dígito verificador
def gerarSegundoDigito(cpfInicial):
    multiDigitoDois = 11
    cpfSomadoDigitoDois = 0

    for i in cpfInicial:
        cpfSomadoDigitoDois += int(i) * multiDigitoDois
        multiDigitoDois -= 1

    restoDigitoDois = cpfSomadoDigitoDois % 11

    if restoDigitoDois <= 2:
        segundoDigitoGerado = 0
    else:
        segundoDigitoGerado = 11 - restoDigitoDois

    return segundoDigitoGerado

# ? Função para testar o cpf
def testarCpf(cpf, cpfs, nValidos, nInvalidos):
    cpfInicial = cpf[:9]
    primeiroDigitoGerado = gerarPrimeiroDigito(cpfInicial)
    cpfInicial += str(primeiroDigitoGerado)
    segundoDigitoGerado = gerarSegundoDigito(cpfInicial)

    if (primeiroDigitoGerado == int(cpf[9]) and segundoDigitoGerado == int(cpf[10]) and len(set(cpf)) != 1):
        print(f'{cpf}:', end=' ')
        print(f'VÁLIDO', color='green', format='bold')
        cpfs.append({'CPF': cpf, 'VALIDACAO': 'INVALIDO'})
        escreverCsv(cpf, 'VALIDO')
        nValidos += 1
    else:
        print(f'{cpf}:', end=' ')
        print(f'INVÁLIDO', color='red', format='bold')
        escreverCsv(cpf, 'INVALIDO')
        cpfs.append({'CPF': cpf, 'VALIDACAO': 'VALIDO'})
        nInvalidos += 1

    return cpfs, nValidos, nInvalidos

# ? Função para escrever no arquivo csv
def escreverCsv(cpf, validacao):
    with open('cpfs.csv', 'a') as file:
        writer = csv.writer(file)
        path = os.path.abspath('cpfs.csv')
        if os.stat(path).st_size == 0:
            writer.writerow(['CPF', 'VALIDACAO'])
        writer.writerow([cpf, validacao])

# ? Se nao for passado nenhum arquivo como argumento, pergunta o cpf para testar um por um
if len(sys.argv) == 1:
    while r == 's':
        cpf = input('Digite o cpf: ')
        while cpf == '' or not cpf.isnumeric() or len(cpf) != 11 or len(set(cpf)) == 1:
            cpf = input('Digite o cpf: ')

        for i in cpfs:
            if i['CPF'] == cpf:
                print('CPF já testado', color='yellow', format='bold')
                jaTestado = True
                break
        
        if jaTestado:
            r = input('Deseja testar outro cpf? (s/n) ').lower()
            while r != 's' and r != 'n':
                r = input('Deseja testar outro cpf? (s/n) ').lower()
            continue
        else:
            cpfInicial = cpf[:9]

            primeiroDigitoGerado = gerarPrimeiroDigito(cpfInicial)

            cpfInicial += str(primeiroDigitoGerado)

            segundoDigitoGerado = gerarSegundoDigito(cpfInicial)

            cpfs, nValidos, nInvalidos = testarCpf(cpf, cpfs, nValidos, nInvalidos)

            nCpfs += 1
            jaTestado = False

            r = input('Deseja testar outro cpf? (s/n) ').lower()
            while r != 's' and r != 'n':
                r = input('Deseja testar outro cpf? (s/n) ').lower()
# ? Se for passado um argumento
else:
    for cpf in cpfsParaTestar:
        if len(cpfs) != 0:
            for j in cpfs:
                if j['CPF'] == cpf['CPF']:
                    print(f'{cpf["CPF"]} já testado', color='yellow', format='bold')
                    jaTestado = True
                    break
                

        cpf = cpf['CPF']
        cpfInicial = cpf[:9]

        if not jaTestado:
            primeiroDigitoGerado = gerarPrimeiroDigito(cpfInicial)

            cpfInicial += str(primeiroDigitoGerado)

            segundoDigitoGerado = gerarSegundoDigito(cpfInicial)

            cpfs, nValidos, nInvalidos = testarCpf(cpf, cpfs, nValidos, nInvalidos)

            nCpfs +=1
        
if nCpfs > 0:
    print(f'\nQuantidade de cpfs testados: {nCpfs}')
    print(f'\nQuantidade de cpfs válidos: {nValidos}')
    print(f'Quantidade de cpfs inválidos: {nInvalidos}')
    print(f'\nPorcentagem de cpfs válidos: {nValidos / nCpfs * 100:.1f}%')
    print(f'Quantidade de cpfs inválidos: {nInvalidos / nCpfs * 100:.1f}%')
else:
    print('\n\nNenhum cpf testado!')