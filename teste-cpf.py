r = 's'
cpfs = []
nValidos = 0
nInvalidos = 0
nCpfs = 0
while r == 's':
    cpf = input('Digite o cpf: ')
    while cpf == '' or not cpf.isnumeric() or len(cpf) != 11:
        cpf = input('Digite o cpf: ')

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
        top = {}
        top['CPF'] = int(cpf)
        top['VALIDACAO'] = 'VÁLIDO'
        cpfs.append(top)
        nValidos += 1
    else:
        print('cpf inválido')
        top = {}
        top['CPF'] = int(cpf)
        top['VALIDACAO'] = 'INVÁLIDO'
        cpfs.append(top)
        nInvalidos += 1

    nCpfs += 1

    r = input("Deseja testar outro cpf? ").lower()
    while r != 's' and r != 'n':
        r = input("Deseja testar outro cpf? ").lower()

porcentagemValidos = nInvalidos / nCpfs

print(f"\nQuantidade de cpfs testados: {nCpfs}")
print(f"\nQuantidade de cpfs válidos: {nValidos}")
print(f"Quantidade de cpfs inválidos: {nInvalidos}")
print(f"\nPorcentagem de cpfs válidos: {nInvalidos / nCpfs * 100:.1f}%")
print(f"Quantidade de cpfs inválidos: {nInvalidos / nCpfs * 100:.1f}%")
