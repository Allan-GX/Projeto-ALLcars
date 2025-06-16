import dados.listas_e_dicionarios as dados
import validacoes.validacoes as vali
import os

def cadastro_usuario():
    nome = input('Digite seu nome:')
    while vali.validar_nome(nome) == False:
        nome = input('Digite seu nome:')

    email = input('Digite seu email:')
    while vali.validar_email(email) == False:
        email = input('Digite seu email:')

    senha = input('Digite sua senha:')
    while vali.validar_senha(senha) == True:
        senha = input('Digite sua senha:')

    palavra_recuperacao = input('Digite uma palavra chave para ser usada caso\nseja necessario recuperar sua senha: ')
    while vali.validar_nome(palavra_recuperacao) == False:
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

def usuarios_salvos(caminho):
    with open (caminho,'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def novos_usuarios(caminho, usuarios):
    with open (caminho,'w', encoding='utf-8') as arquivo:
        arquivo.write(str(usuarios))

def emails_salvos(emails,usuarios):
    for i in range(len(usuarios)):
        emails.append(usuarios[i]['email'])