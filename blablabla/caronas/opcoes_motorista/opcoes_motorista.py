import dados.listas_e_dicionarios as dados
import os

def cadastro_carona(usu_atual, email_usu):
    usuario = str(usu_atual)
    email = str(email_usu)
    inicio_caro = input('Digite qual local irá iniciar sua carona:')
    destino_caro = input('Digite qual será o destino final da carona:')
    aux = True
    while aux == True:
        mes30 = (4,6,9,11)
        mes31 = (1,3,5,7,8,10,12)
        data_caro = input('Digite a data que será a carona(dd/mm/aaaa):')
        dia = int(data_caro[0:2])
        mes = int(data_caro[3:5])
        ano = int(data_caro[6:10])
        validado = False
        Bissexto = False
        if(ano % 4 == 0):
            Bissexto = True
            if(ano % 100 == 0 and ano % 400 != 0):
                Bissexto = False
        if(mes in mes31):
            if(dia >= 1 and dia <= 31):
                validado = True
        elif(mes in mes30):
            if(dia >= 1 and dia <= 30):
                validado = True
        elif(mes == 2):
            if(Bissexto == True and dia >= 1 and dia <= 29):
                validado = True
            elif(dia >= 1 and dia <= 28):
                validado = True
        if(validado == True):
            print('Data válida!')
            aux = False
        else:
            print("Data invalida ,digite novamente!")
    aux = True
    while aux == True:
        verificacao = list(range(24))
        verificacao2 = list(range(60))
        validado = False
        hora_caro = input('Digite o horario o qual você irá dar a carona(00:00):')
        hora = int(hora_caro[0:2])
        minuto = int(hora_caro[3:5])
        if (hora in verificacao) and (minuto in verificacao2):
            validado = True
        if validado == True:
            print ('Horario válido!')
            aux = False
        else:
            print('Horário invalido, digite novamente!')
    
    vagas_caro = int(input('Digite quantas vagas tem disponiveis no seu veiculo:'))
    preco_carp = float(input('Digite quanto será cobrado por cada vaga:'))
    motorista = usuario
    email_moto = email
    carona = {
    'inicio' : inicio_caro,
    'destino' : destino_caro,
    'data' : data_caro,
    'hora' : hora_caro,
    'vagas' : vagas_caro,
    'preco_vaga' : preco_carp,
    'motorista' : motorista,
    'email do motorista' : email_moto,
    'passageiros' : []
    }
    dados.caronas.append (carona)
    dados.datas.append(carona['data'])
    dados.horas.append(carona['hora'])
    for usu in dados.caronas:
        for chaves in usu.keys():
            dados.chave.append(chaves)
        for valores in usu.values():
            dados.valor.append(valores)
    os.system('cls')
    print('Carona cadastrada com sucesso!')
    print('=' * 70)

def mostrar_caronas_motorista(usu_atual):
    naux = 0
    usuario = str(usu_atual)
    auxiliar = True
    for usu in dados.caronas:
        dados.chave.clear()
        dados.valor.clear()
        for chaves in usu.keys():
            dados.chave.append(chaves)
        for valores in usu.values():
            dados.valor.append(valores)
        if usuario in usu['motorista']:
            naux += 1
            print(f'\n\n{naux}° carona disponivel:\n')
            for i in range(len(dados.chave)):
                print (f'{dados.traducao[dados.chave[i]]}: {dados.valor[i]}')
            auxiliar = False
    if auxiliar == True:
        os.system('cls')
        print('Você não tem nenhuma carona cadastrada no momento\n\n[0] Voltar\n')
        confirmacao_apagar = input ('Digite o digito doque você deseja fazer: ')
        os.system('cls')
        print('=' * 70)
    if auxiliar == False:
        aux5 = True
        while aux5 == True:
            print('\n[1] Remover uma carona cadastrada\n[0] Voltar\n')
            confirmacao_apagar = input ('Digite o digito doque você deseja fazer:')
            if confirmacao_apagar == '0':
                os.system('cls')
                print('=' * 70)                                    
                aux5 = False
            elif confirmacao_apagar == '1':
                aux5 = False
                return confirmacao_apagar

def apagar_carona(usu_atual):
    usuario = str(usu_atual)
    data_p_exclusao = input ('Digite qual a data da carona que você deseja remover: ')
    hora_p_esclusao = input ('Digite qual o horario de inicio da corrida que você deseja remover: ')
    ifaux2 = True
    for usu in dados.caronas:
        if usuario in usu['motorista']:
            if (data_p_exclusao in dados.datas) and (hora_p_esclusao in dados.horas):
                dados.caronas.remove(usu)
                os.system('cls')
                print('Carona removida com sucesso!!')
                print('=' * 70)  
                ifaux2 = False
    if ifaux2 == True:
        print(f'carona com data {data_p_exclusao} e horario {hora_p_esclusao} não encontrados!')