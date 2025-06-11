import dados.listas_e_dicionarios as dados
import os

def login():
    ifaux = True
    erros = 0
    while ifaux == True:
        email_log = input('Digite seu E-mail: ')
        senha_log = input('Digite sua senha: ')
        for log in dados.usuarios:
            if email_log == log['email'] and senha_log == log['senha']:
                usu_atual = log['nome']
                email_atual = log['email']
                ifaux = False
                break
        if ifaux == True:
            print ('Senha ou email incorretos!')
            erros += 1
            if erros >= 3:
                print('Você cometeu muitos erros seguidos\ndeseja recuperar sua senha?\n\n[1] Sim\n[0] Não\n')
                resposta = input('Digite o digito da sua escolha: ')
                if resposta == '0':
                    os.system('cls')
                    print('=' * 70)
                    continue
                if resposta == '1':
                    recuperar = input('Digite seu E-mail: ')
                    pchave = input('Digite a palvra chave pra a recuperação: ')
                    aux = True
                    aux2 = 0
                    for usu in dados.usuarios:
                        if (recuperar in usu['email']) and (pchave in usu['pchave']):
                            aux2 = True
                            while aux2 == True:
                                nova_senha= input('Digite sua nova senha:')
                                if len(nova_senha) < 6:
                                    print('A senha precisa ter pelomenos 6 digitos')
                                if len(nova_senha) >= 6:
                                    aux2 = False
                            dados.usuarios[aux2]['senha'] = nova_senha
                            os.system('cls')
                            print ('Sehna redefinida!')
                            print('=' * 70)
                            erros = 0
                            aux = False
                        aux2 += 1
                    if aux == True:
                        print('Não existe nenhum cadastro com este e-mail.')
                        break
        else:
            break
    return usu_atual,email_atual
