import dados.listas_e_dicionarios as dados
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

def validar_data(data_caro):
    valido = False
    mes30 = (4,6,9,11)
    mes31 = (1,3,5,7,8,10,12)
    if (len(data_caro) == 10) and data_caro[0:2].isdigit() == True and data_caro[3:5].isdigit() == True and data_caro[6:10].isdigit() == True:
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
            valido = True
        else:
            print("Data invalida ,digite novamente!")
    else:
        print("Data invalida ,digite novamente!")
    return valido

def validar_hora(hora_caro):
    verificacao = list(range(24))
    verificacao2 = list(range(60))
    valido = False
    validado = False
    if (len(hora_caro) == 5) and hora_caro[0:2].isdigit() == True and hora_caro[3:5].isdigit() == True:
        hora = int(hora_caro[0:2])
        minuto = int(hora_caro[3:5])
        if (hora in verificacao) and (minuto in verificacao2):
            validado = True
        if validado == True:
            valido = True
        else:
            print('Horário invalido, digite novamente!')
    else:
            print('Horário invalido, digite novamente!')
    return valido

def validar_nome(nome):
    valido = False
    if len(nome) > 1:
        valido = True
    else:
        print('nome invalido!')
    return valido

def validar_numeros(numero):
    valido = False
    if numero.isdigit() == True:
        if int(numero) > 0:
            valido = True
        else:
            print('numero invalido!')
    else:
            print('digito invalido!')
    return valido

def validar_email(email):
    valido = False
    if (email not in dados.emails) and (email.endswith('@gmail.com')\
        or email.endswith('@hotmail.com')\
        or email.endswith('@outlook.com')\
        or email.endswith('@live.com')\
        or email.endswith('@icloud.com')\
        or email.endswith('@mac.com')\
        or email.endswith('@me.com')\
            ):
            valido = True
    else:
        print ('E-Mail inválido ou já cadastrado, digite novamente.')
    return valido

def validar_senha(senha):
    valido = False
    senha = input('Digite sua senha:')
    if len(senha) < 6:
        print('A senha precisa ter pelomenos 6 digitos')
    else:
        valido = True
    return valido