import dados.listas_e_dicionarios as dados
import validacoes.validacoes as vali
import os

def cadastro_carona(usu_atual, email_usu):
    usuario = str(usu_atual)
    email = str(email_usu)
    inicio_caro = input('Digite qual local irá iniciar sua carona:')
    while vali.validar_nome(inicio_caro) == False:
        inicio_caro = input('Digite qual local irá iniciar sua carona:')

    destino_caro = input('Digite qual será o destino final da carona:')
    while vali.validar_nome(destino_caro) == False:
        destino_caro = input('Digite qual será o destino final da carona:')

    data_caro = input('Digite a data que será a carona(dd/mm/aaaa):')
    while vali.validar_data(data_caro) == False:
        data_caro = input('Digite a data que será a carona(dd/mm/aaaa):')

    hora_caro = input('Digite será horario da carona(00:00):')
    while vali.validar_hora(hora_caro) == False:
        hora_caro = input('Digite será horario da carona(00:00):')

    vagas_caro = input('Digite quantas vagas tem disponiveis no seu veiculo:')
    while vali.validar_numeros(vagas_caro) == False:
        vagas_caro = input('Digite quantas vagas tem disponiveis no seu veiculo:')

    preco_carp = input('Digite quanto será cobrado por cada vaga:')
    while vali.validar_numeros(preco_carp) == False:
        preco_carp = input('Digite quanto será cobrado por cada vaga:')

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
    return auxiliar

def continuacao_carona_motorista(auxiliar):
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

def mostrar_relatorios_caronas(usu_atual):
    naux = 0
    total_final = 0
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
            total = float(usu['preco_vaga']) * len(usu['passageiros'])
            total_final += total
            print(f'\n\033[1mO valor total é: R$ {total:.2f}\033[0m')
            if naux == len(dados.caronas):
                print(f'\n\033[1mAo todo seu ganho total será de: R$ {total_final:.2f}\033[0m')
            auxiliar = False
    return auxiliar

def relatorio_totalizador(auxiliar):
    if auxiliar == True:
        os.system('cls')
        print('Você não tem nenhuma carona cadastrada no momento\n\n[0] Voltar\n')
        confirmacao_apagar = input ('Digite o digito doque você deseja fazer: ')
        os.system('cls')
        print('=' * 70)
    if auxiliar == False:
        print('\nCaso queira, podemos salvar seu\nrelatório em um arquivo a parte!\n\n[1] Salvar Relatório\n[0] Voltar\n')
        confirmacao_apagar = input ('Digite o digito doque você deseja fazer: ')
        if confirmacao_apagar == '0':
            os.system('cls')
            print('=' * 70) 
        if confirmacao_apagar == '1':
            os.system('cls')
            print('=' * 70)
    return confirmacao_apagar

def salvar_relatorio(usuario):
    aux = 0
    total_final = 0
    with open (dados.caminho_relatorio,'w', encoding='utf-8') as arquivo:
        arquivo.write('=' * 18 + ' RELATORIO ' + '=' * 18 + '\n')
    for usu in dados.caronas:
        dados.chave.clear()
        dados.valor.clear()
        for chaves in usu.keys():
            dados.chave.append(chaves)
        for valores in usu.values():
            dados.valor.append(valores)
        if usuario in usu['motorista']:
            aux += 1
            with open (dados.caminho_relatorio,'a', encoding='utf-8') as arquivo:
                    arquivo.write(str(f'\n{aux}° Carona cadastrada:\n\n'))
            for i in range(len(dados.chave)):
                dado = str(f'{dados.traducao[dados.chave[i]]}: {dados.valor[i]}')
                with open (dados.caminho_relatorio,'a', encoding='utf-8') as arquivo:
                    arquivo.write(str(dado + '\n'))
            total = float(usu['preco_vaga']) * len(usu['passageiros'])
            t_em_texto = str(f'{total:.2f}')
            total_final += total
            with open (dados.caminho_relatorio,'a', encoding='utf-8') as arquivo:
                    arquivo.write(str('\n' + f'O valor total é: R$ {t_em_texto}' + '\n'))
    tf_em_texto = str(f'{total_final:.2f}')
    with open (dados.caminho_relatorio,'a', encoding='utf-8') as arquivo:
        arquivo.write(str('\n' + f'Ao todo seu ganho total será de: R$ {tf_em_texto}' + '\n'))
    print('Relatorio Salvo em: \033[1mdados/relatorio.txt\033[0m ')
    print('=' * 70)