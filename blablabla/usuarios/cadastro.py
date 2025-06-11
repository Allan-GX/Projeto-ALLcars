import dados.listas_e_dicionarios as dados
import os

def cadastro_usuario():
    nome = input('Digite seu nome:')
    aux1 = True
    while aux1 == True:
        email = input('Digite seu email:')
        ifaux = True
        if ifaux == True:
            if (email not in dados.emails) and (email.endswith('@gmail.com')\
                or email.endswith('@hotmail.com')\
                or email.endswith('@outlook.com')\
                or email.endswith('@live.com')\
                or email.endswith('@icloud.com')\
                or email.endswith('@mac.com')\
                or email.endswith('@me.com')\
                    ):
                    print ('E-Mail válido')
                    ifaux = False
                    aux1 = False
            else:
                print ('E-Mail inválido ou já cadastrado, digite novamente.')
                ifaux = False
                continue
    aux2 = True
    while aux2 == True:
        senha = input('Digite sua senha:')
        if len(senha) < 6:
            print('A senha precisa ter pelomenos 6 digitos')
        if len(senha) >= 6:
            aux2 = False
            break
    palavra_recuperacao = input('Digite uma palavra chave para ser usada caso\nseja necessario recuperar sua senha: ')
    cadastro = {
        'nome' : nome,
        'email': email,
        'senha' : senha,
        'pchave' : palavra_recuperacao
        }
    dados.usuarios.append (cadastro)
    dados.emails.append(email)
    os.system('cls')
    print('=' * 70)
    print('Cadastro Realizado com Sucesso!')