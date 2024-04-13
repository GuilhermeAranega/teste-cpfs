![](https://github.com/GuilhermeAranega/teste-cpfs/blob/main/public/teste-cpf.gif)

# Teste de CPFs

Um projeto para testar CPFs feito em python para uma avaliação do Colégios Univap Unidade Centro. 
Após fazer a verificação, fornece as estatísticas como quantos CPFs foram testados, quantos foram válidos, quantos foram inválidos, a porcentagem de CPFs válidos e a porcentagem de CPFs inválidos

## Como usar:

1. Clone o repositório:
   
```bash
git clone https://github.com/GuilhermeAranega/teste-cpfs
cd ./teste-cpfs
```

2. Instale a dependência com **pip**:
```bash
pip install -r requirements.txt
```

3. (opcional) Entre no arquivo testarCpfs.csv e adicione os cpfs que você quer testar seguindo o seguinte formato:
```csv
CPF

<CPF que você quer testar>
<CPF que você quer testar>
<CPF que você quer testar>
...
```

4. Há duas formas de rodar o programa:

Rodar o programa testando os CPFs pelo arquivo csv:
```bash
python .\teste-cpf.py testarCpfs.csv
```

OU

Rodar o programa testando os CPFs um por um:
```bash
python .\teste-cpf.py
```
