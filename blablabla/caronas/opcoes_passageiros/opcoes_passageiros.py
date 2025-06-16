import dados.listas_e_dicionarios as dados
import validacoes.validacoes as vali
import os

def mostrar_caronas(usu_atual):
    naux = 0
    usuario = str(usu_atual)
    for usu in dados.caronas:
        dados.chave.clear()
        dados.valor.clear()
        for chaves in usu.keys():
            dados.chave.append(chaves)
        for valores in usu.values():
            dados.valor.append(valores)
        if (usuario not in usu['motorista']) and (usu['vagas'] != 0):
            naux += 1
            print(f'\n\n{naux}° carona disponivel:\n')
            for i in range(len(dados.chave)):
                print (f'{dados.traducao[dados.chave[i]]}: {dados.valor[i]}')

def mostrar_caronas_expecificas(usu_atual):
    print ('Olá usuario, aqui você poderá procurar a carona que você precisa!!\nBasta colocar a origem e destino da sua carona desejada.')
    print('=' * 70)
    procura_origem = input('Digite em qual local você deseja iniciar sua carona:')
    procura_destino = input('Agora digite em qual local você deseja chegar:')
    naux = 0
    usuario = str(usu_atual)
    ifaux = True
    for usu in dados.caronas:
        dados.chave.clear()
        dados.valor.clear()
        for chaves in usu.keys():
            dados.chave.append(chaves)
        for valores in usu.values():
            dados.valor.append(valores)
            
        if (procura_origem == usu['inicio']) and (procura_destino == usu['destino']) and (usuario not in usu['motorista']) and (usu['vagas'] != 0):
            naux += 1
            print(f'\n\n{naux}° carona disponivel:\n')
            for i in range(len(dados.chave)):
                print (f'{dados.traducao[dados.chave[i]]}: {dados.valor[i]}')
                ifaux = False
    if ifaux == True:
        os.system('cls')
        print('Infelizmente não encontramos nenhuma caro para você no momento!\n\n[0] Voltar\n')
        confirmacao_apagar = input ('Digite o digito doque você deseja fazer: ')
        os.system('cls')
        print('=' * 70)

def marcar_carona(usu_atual):
    aux5 = True
    usuario = str(usu_atual)
    while aux5 == True:
        confirmacao = input('\nVocê deseja reservar uma vaga em alguma dessas caronas? (s/n)\n\nDigite:').lower()
        
        if confirmacao == 's':
            conf_data = input ('Qual a data da carona que você deseja?\n\nDigite:')
            conf_email_motorista = input('Digite o email do motorista dessa carona:')
            ifaux = True
            for usu in dados.caronas:
                if (conf_data in usu['data']) and (conf_email_motorista in usu['email do motorista']):
                    posicao_salva = dados.caronas.index(usu)
                    vagas_numero = (dados.caronas[posicao_salva]['vagas'])
                    vagas_numero -= 1
                    dados.caronas[posicao_salva].update({'vagas' : vagas_numero})
                    dados.caronas[posicao_salva]['passageiros'].append(usuario)
                    os.system('cls')
                    print ('\nReserva para carona marcada!\n')
                    print('=' * 70)
                    ifaux = False
                    aux5 = False
            if ifaux == True:
                os.system('cls')
                print('Motorista e/ou data de carona não encontrados!')
                print('=' * 70)
                aux5 = False
        else: 
            os.system('cls')
            aux5 = False

def reserva_marcadas(usu_atual):
    naux = 0
    usuario = str(usu_atual)
    ifaux = True
    for usu in dados.caronas:
        dados.chave.clear()
        dados.valor.clear()
        for chaves in usu.keys():
            dados.chave.append(chaves)
        for valores in usu.values():
            dados.valor.append(valores)
        if (usuario in usu['passageiros']):
            ifaux = False
            naux += 1
            print(f'\n\n{naux}° carona disponivel:\n')
            for i in range(len(dados.chave)):
                print (f'{dados.traducao[dados.chave[i]]}: {dados.valor[i]}')
    if ifaux == True:
        os.system('cls')
        print('Você não tem nenhuma reserva no momento\n\n[0] Voltar\n')
        confirmacao_apagar = input ('Digite o digito doque você deseja fazer: ')
        os.system('cls')
        print('=' * 70)
    if ifaux == False:
        aux5 = True
        while aux5 == True:
            print('\n[1] Remover uma reserva\n[0] Voltar\n')
            confirmacao_apagar = input ('Digite o digito doque você deseja fazer: ')
            if confirmacao_apagar == '0':
                aux5 = False
                os.system('cls')
                print('=' * 70)
            if confirmacao_apagar == '1':
                aux5 = False
                return confirmacao_apagar

def apagar_reserva(usu_atual):
    usuario = str(usu_atual)
    conf_data = input ('Digite a data da carona que você deseja apagar:')
    conf_email_motorista = input ('Digite o email do motorista dessa carona:')
    ifaux2 = True
    for usu in dados.caronas:
        if (conf_data in usu['data']) and (conf_email_motorista in usu['email do motorista']):
            posicao_salva = dados.caronas.index(usu)
            vagas_numero = int(dados.caronas[posicao_salva]['vagas'])
            vagas_numero += 1
            dados.caronas[posicao_salva].update({'vagas' : vagas_numero})
            dados.caronas[posicao_salva]['passageiros'].remove(usuario)
            os.system('cls')
            print ('Reserva para carona desmarcada!')
            print('=' * 70)
            ifaux2 = False
    if ifaux2 == True:
        os.system('cls')
        print('Motorista e/ou data de carona não encontrados!')
        print('=' * 70)