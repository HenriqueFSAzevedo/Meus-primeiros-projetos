from time import sleep
from random import randrange
jokenpo = ['JO', 'KEN', 'PÔ!']
emojis = ['👊', '🖐️', '✌️']
escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
print(f'\33[1;34m{'!!! VAMOS JOGAR JOKENPÔ !!!':🎆^81}')
sleep(1)
print('😄 😄 😄 Você deve escolher entre pedra, papel e tesoura e disputar comigo 😎 para ver quem vence!👊 👊 👊 ')
sleep(1)
while True:
    try:
        escpc = randrange(0,3)
        escjog = int(input('\33[34mDigite 0 se quiser escolher PEDRA, 1 se quiser escolher PAPEL e 2 se quiser escolher TESOURA, ' \
        'ou se quiser parar de brincar digite 3: '))
        sleep(1)
        if escjog < 0 or escjog > 3:
            print('\33[33m😥 😥 😥 Então temos um engraçadinho por aqui! Leia os comandos com atenção por favor!')
            sleep(0.5)
            continue
        if escjog == 3:
            break  
        for jogar in range(0,3):
            print(jokenpo[jogar], end = '  ')
            print(emojis[jogar])
            sleep(1)
        if escpc == escjog:
            print(f'\33[36mEu também escolhi {escolhas[escpc]}, então dessa vez deu empate! Vamos de novo!')
        elif escpc == 0:
            if escjog == 1:
                print(f'\33[32mEu escolhi {escolhas[escpc]} e você escolheu {escolhas[escjog]}.🎆 🎆 🎆 VOCÊ VENCEU! 🎆 🎆 🎆')
            elif escjog == 2:
                print(f'\33[35mEu escolhi {escolhas[escpc]} e você escolheu {escolhas[escjog]}.😅 😅 😅 VOCÊ PERDEU! 😅 😅 😅')
        elif escpc == 1:
            if escjog == 0:
                print(f'\33[35mEu escolhi {escolhas[escpc]} e você escolheu {escolhas[escjog]}.😅 😅 😅 VOCÊ PERDEU! 😅 😅 😅')
            elif escjog == 2:
                print(f'\33[32mEu escolhi {escolhas[escpc]} e você escolheu {escolhas[escjog]}.🎆 🎆 🎆 VOCÊ VENCEU! 🎆 🎆 🎆')
        elif escpc == 2:
            if escjog == 0:
                print(f'\33[32mEu escolhi {escolhas[escpc]} e você escolheu {escolhas[escjog]}.🎆 🎆 🎆 VOCÊ VENCEU! 🎆 🎆 🎆')
            elif escjog == 1:
                print(f'\33[35mEu escolhi {escolhas[escpc]} e você escolheu {escolhas[escjog]}.😅 😅 😅 VOCÊ PERDEU! 😅 😅 😅')
          
    except ValueError:
        sleep(1)
        print('\33[31m💢😠💢😠💢😠Aí não né!💢😠💢😠💢😠 Leia os comandos com atenção por favor!')
        sleep(0.5)
sleep(1)
print('😁 😁 😁 Foi divertido jogar com você, apareça de novo para jogarmos mais! 👋 👋 👋')