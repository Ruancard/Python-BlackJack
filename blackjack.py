import random

jogadores = []


def __pegarcarta__(soma):
    n1= random.randrange(1,14)

    match n1:
        case 1:
            print('vc tirou As')
        case 11:
            print('vc tirou um valete')
        case 12:
            print('vc tirou uma rainha')
        case 13:
            print('vc tirou um rei')
        case _:
            print(f'vc tirou um {n1}')

    if n1 > 10:
        n1 = 10

    soma += n1
    return soma

def jogada(soma):
    if soma < 21:
        print(f'\n\n<<<<<<<  e a soma de seus pontos é: {soma}  >>>>>>>>>>\n\n')

        escolha = int(input('\n\n0-parar\n1-comprar mais uma carta\ndigite uma das opções:'))
        if escolha == 0:
            print(f'\n\n<<<<<<<<<<  vc ficou com {soma} pontos >>>>>>>>>>\n\n')
            return soma
        elif escolha == 1:
            soma = __pegarcarta__(soma)
            jogada(soma)
        else:
            print('error')
    elif soma == 21:
        print('n\n<<<<<<<<<<  vc ganhou  >>>>>>>>>>\n\n')
        return soma
    else:
        print('\n\n<<<<<<<<<<  vc estourou  >>>>>>>>>>\n\n')
        return soma
    return soma
    

def jogo():
    soma = 0
    print('\n\n<<<<<<<<<<  novo jogo  >>>>>>>>>>\n\n')
    soma = __pegarcarta__(soma)
    soma = __pegarcarta__(soma)

    ponto_final = jogada(soma)

    return ponto_final

def main(jogadores):
    ponto_final = jogo()
    if ponto_final != None:
        jogadores.append(ponto_final)
        escolha = int(input('\n\n0-proximo jogador\n1-novo jogo\n2-encerrar jogo\ndigite uma das opções:'))
        if escolha == 0:
            return jogadores
        elif escolha == 1:
            print(f'\n\n<<<<< o Resultado foi:{jogadores} >>>>>\n\n')
            jogadores = []
            return jogadores
        else:
            print(f'\n\n<<<<< o Resultado foi:{jogadores} >>>>>\n\n')
            print(f'\n\n<<<<< fim de jogo >>>>>\n\n')
            jogadores = ['end']
            return jogadores

while not 'end' in jogadores:
    jogadores = main(jogadores)