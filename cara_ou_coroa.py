from random import randint
from time import sleep

def separar_linhas():
    print('- '*16)

print('=-=-= CARA OU COROA =-=-=')
win = defeat = 0
while True:
    jogar = str(input('Vamos jogar <s/n>? ')).lower().strip()[0]
    while jogar not in 'sn':
        print('\n[ERROR] Digite uma resposta válida.')
        jogar = str(input('\nVamos jogar? ')).lower().strip()[0]
    else:
        if jogar == 's':
            print('\nEntão vamos começar :)')
            sleep(1)
            
            while True:  # Resposta da máquina se vai ser cara ou coroa.
                computador = randint(1,2)
                if computador == 1:
                    computador = 'CARA'
                else:
                    computador = 'COROA'
                
                # Resposta do usuário e 
                resposta = str(input('\n- Você quer escolher cara ou coroa? ')).upper().strip()
                while resposta != 'CARA' and resposta != 'COROA':
                    print('\n[ERROR] Digite uma resposta válida.')
                    resposta = str(input('\n- Você quer escolher cara ou coroa? ')).upper().strip()
                else:
                    print('\n--- Jogando a moeda ---')
                    sleep(2)
                    if resposta == computador:
                        win += 1
                        print(f'\nVocê escolheu: {resposta} e o resultado foi: {computador}.')
                        print('\nParabénsss, você GANHOU!')
                        print(f'Você tem o total de {win} vitórias.')
                    else:
                        defeat += 1
                        print(f'\nVocê escolheu: {resposta} e o resultado foi: {computador}.') 
                        print('\nPoxa, você PERDEU. Mais sorte na próxima!')
                        print(f'Você tem o total de {defeat} derrotas.')  


                continuar = str(input('\nDeseja continuar <s/n>? ')).lower().strip()[0]
                while continuar not in 'sn':
                    print('[ERROR] Digite uma resposta válida.')
                    continuar = str(input('\nDeseja continuar <s/n>? ')).lower().strip()[0]
                else:
                    if continuar == 'n':
                        print('\nEncerrando..')
                        sleep(1)
                        print(f'\n- Você obteve um total de {win} vitória(s) e {defeat} derrota(s).')
                        print('Vejo você na próxima jogatina, até breve! :D')
                        break
        else:
            print('\nEncerrando..')
            sleep(2)
            print('\nAté depois, amigo. :)')
            print()
            break
    break
