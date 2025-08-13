import random
from time import sleep
print(f'\33[1;34m{'!!!JOGO DA ADIVINHAÇÃO!!!':🎆^53}')
sleep(1)
print(f'{'!!!😄Vamos jogar o jogo da adivinhação😄!!!':🎇^60}')
sleep(1)
print('🤔🤔 Irei pensar em um número entre 0 e 9 e você tenta adivinhar 🤔🤔, 👍 beleza?')
sleep(1)
for suspense in range(0,3):
    print('🥁   🥁   🥁')
    sleep(1)
print('😎😎!!!Pronto!!! Já pensei em um número, agora é a sua vez de tentar adivinhar!👊')
sleep(0.5)
while True:
    try:
        numpc = random.randrange(1,10)
        numjog = int(input('\33[34mDigite aqui o número que você acha que eu pensei: '))
        if numpc  == numjog:
            sleep(1)
            print(f'\33[32m🎆🎆🎆!!!Parabéns!!!🎆🎆🎆 Eu realmente pensei em {numpc}!')
            break
        elif numjog < 0 or numjog > 9:
            sleep(1)
            print('\33[33m😞😞 Engraçadinho! 😞😞 Eu disse que pensaria num número de 0 à 9! Tente de novo!')
        else:
            sleep(1)
            print(f'\33[36m😇😇😇Que pena!😇😇😇 Você disse {numjog}, mas na verdade eu pensei em {numpc}, tente de novo!')
    except ValueError:
        sleep(1)
        print('\33[31m😡😡😡 !Ei! 😡😡😡 Isso daí nem é um número! Tente digitar um número entre 0 e 9!')
sleep(1)
print('\33[34m😀😀😀 Foi divertido jogar com você! 😀😀😀 Apareça de novo para jogarmos mais!😉')