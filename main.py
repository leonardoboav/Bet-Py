import random

MAX_LINHAS = 3
MAX_APOSTA = 100
MIN_APOSTA = 1

ROWS = 3
COLS = 3

contador = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

valor = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def checarGanhador(colunas, linhas, aposta, valores):
    ganhadores = 0
    linhaGanha = []
    for linha in range(linhas):
        contador = colunas[0][linha]
        for coluna in colunas:
            checarSymbol = coluna[linha]
            if contador != checarSymbol:
                break
            else:
                ganhadores += valores[contador] + aposta
                linhaGanha.append(linha + 1)

    return ganhadores, linhaGanha


def pegarSlotMachine(rows, cols, symbols):
    allContador = []
    for symbol, contador in symbols.items():
        for i in range(contador):
            allContador.append(symbol)

    colunas = []
    for col in range(cols):
        coluna = []
        currentContador = allContador[:]
        for now in range(rows):
            valor = random.choice(currentContador)
            currentContador.remove(valor)
            coluna.append(valor)

        colunas.append(coluna)
    
    return colunas   


def printSlotMachine(colunas):
    for row in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas) -1:
                print(coluna[row], end=" | ")
            else:
                print(coluna[row], end="")

        print()


def deposit():
    while True: 
        amount = input("Quanto você deseja depositar? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Quantidade deve ser maior que zero (0).")
        else:
            print("Por favor digite um número.")

    return amount    

def pegarNumeroLinhas():
    while True: 
        linhas = input("Coloque o número de linhas para (1-" + str(MAX_LINHAS) + ")?")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINHAS:
                break
            else:
                print("O número deve estar entre o intervalo (1-3). ")
        else:
            print("Por favor digite um número.")

    return linhas 

def pegarAposta():
    while True: 
        amount = input("Quanto você deseja apostar em cada linha? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_APOSTA <= amount <= MAX_APOSTA:
                break
            else:
                print(f"Quantidade deve estar entre ${MIN_APOSTA} - ${MAX_APOSTA}.")
        else:
            print("Por favor digite um número.")

    return amount


def jogo(balance):
    linhas = pegarNumeroLinhas()
    while True:
        aposta = pegarAposta()
        apostaTotal = aposta * linhas

        if apostaTotal > balance:
            print(f"Você não tem a quantidade necessária para apostar. Você possui: ${balance}")
        else:
            break

    print(f"Você está apostando ${aposta} em {linhas} linhas. Aposta total: ${apostaTotal}.")

    slot = pegarSlotMachine(ROWS, COLS, contador)
    printSlotMachine(slot)
    lucro, linhaGanha = checarGanhador(slot, linhas, aposta, valor)
    print(f"Parabéns! Você ganhou ${lucro}.")
    print(f"Você ganhou nas linhas:", *linhaGanha)

    return lucro - apostaTotal


def main():
    balance = deposit()
    while True:
        print(f"Sua quantia atual é ${balance}")
        roleta = input("Aperte enter para rodar (q para Sair). ")
        if roleta == "q":
            break

        balance += jogo(balance)

    print(f"Você saiu com ${balance}! Parabéns. ")    

main()
