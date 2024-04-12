import csv
import os
r = 's'
cpfs = []
nValidos = 0
nInvalidos = 0
nCpfs = 0
jaTestado = False

if os.path.exists('cpfs.csv'): 
    with open('cpfs.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cpfs.append(row)

def escreverCsv(cpf, validacao):
    with open('cpfs.csv', 'a') as file:
        writer = csv.writer(file)
        path = os.path.abspath('cpfs.csv')
        if os.stat(path).st_size == 0:
            writer.writerow(['CPF', 'VALIDACAO'])
        writer.writerow([cpf, validacao])

while r == 's':
    cpf = input('Digite o cpf: ')
    while cpf == '' or not cpf.isnumeric() or len(cpf) != 11:
        cpf = input('Digite o cpf: ')

    for i in cpfs:
        if i['CPF'] == cpf:
            print('CPF já testado')
            jaTestado = True
            break
    
    if jaTestado:
        r = input("Deseja testar outro cpf? (s/n) ").lower()
        while r != 's' and r != 'n':
            r = input("Deseja testar outro cpf? (s/n) ").lower()
        continue
    else:
        cpfInicial = cpf[:9]
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

        multiDigitoDois = 11
        cpfSomadoDigitoDois = 0

        cpfInicial += str(primeiroDigitoGerado)

        for i in cpfInicial:
            cpfSomadoDigitoDois += int(i) * multiDigitoDois
            multiDigitoDois -= 1

        restoDigitoDois = cpfSomadoDigitoDois % 11

        if restoDigitoDois <= 2:
            segundoDigitoGerado = 0
        else:
            segundoDigitoGerado = 11 - restoDigitoDois

        if (primeiroDigitoGerado == int(cpf[9]) and segundoDigitoGerado == int(cpf[10])):
            print('cpf válido')
            cpfs.append({'CPF': cpf, 'VALIDACAO': 'INVALIDO'})
            escreverCsv(cpf, 'VALIDO')
            nValidos += 1
        else:
            print('cpf inválido')
            escreverCsv(cpf, 'INVALIDO')
            cpfs.append({'CPF': cpf, 'VALIDACAO': 'VALIDO'})
            nInvalidos += 1

        nCpfs += 1
        jaTestado = False

        r = input("Deseja testar outro cpf? (s/n) ").lower()
        while r != 's' and r != 'n':
            r = input("Deseja testar outro cpf? (s/n) ").lower()

porcentagemValidos = nInvalidos / nCpfs

print(f"\nQuantidade de cpfs testados: {nCpfs}")
print(f"\nQuantidade de cpfs válidos: {nValidos}")
print(f"Quantidade de cpfs inválidos: {nInvalidos}")
print(f"\nPorcentagem de cpfs válidos: {nInvalidos / nCpfs * 100:.1f}%")
print(f"Quantidade de cpfs inválidos: {nInvalidos / nCpfs * 100:.1f}%")