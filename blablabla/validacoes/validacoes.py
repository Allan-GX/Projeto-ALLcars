import os

def confirmacao_sair():
    aux3 = True
    while aux3 == True:
        confirmacao = input ('Você tem certeza que deseja deslogar da sua conta?(s/n)\n\nDigite:')
            
        if confirmacao == 's':
            os.system('cls')
            print('=' * 70)
            aux2 = False
            aux3 = False
        elif confirmacao == 'n':
            aux2 = True
            aux3 = False
    return aux2

def data():
    print
def hora():
    print
def nomes():
    print
def vagas():
    print