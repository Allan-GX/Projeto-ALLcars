import dados.listas_e_dicionarios as dados
import validacoes.validacoes as vali
import caronas.opcoes_motorista.opcoes_motorista as moto
import caronas.opcoes_passageiros.opcoes_passageiros as passa
import usuarios.cadastro as cad
import usuarios.login as logi
import os

while True:
    os.system('cls')
    print('=' * 70)
    print('Seja Bem vindo ao ALLcars!! Antes de utilizar o aplicativo\nentre em sua conta ou faça seu cadastro')
    print('=' * 70)
    print('\n[1] Cadastro\n[2] Login\n[3] Sobre o app\n[0] Sair\n')
    print('=' * 70)
    hub_1 = input('Digite oque você deseja fazer: ')
    os.system('cls')
    print('=' * 70)

    if hub_1 == '0':
        print ('Até logo!!')
        break

    elif hub_1 == '1':
        cad.cadastro_usuario()

    elif hub_1 == '2':
        usu,email= logi.login()
        os.system('cls')
        for log in dados.usuarios:
            if usu == log['nome']:
                aux2 = True
                while aux2 == True:
                    print(f'Seja bem vindo {log["nome"]} oque você deseja fazer?')
                    print('=' * 70)
                    print('\n[1] Ver Opções de Passageiro \
                    \n[2] Ver Opções de Condutor \
                    \n[0] Deslogar da conta\n')
                    print('=' * 70)
                    hub_2 = input('\nDigite sua opção de escolha:')
                    os.system('cls')
                    print('=' * 70)

                    if hub_2 == '0':
                        aux2 = vali.confirmacao_sair()

                    if hub_2 == '1':
                        print('Opções de Passageiros:')
                        print('=' * 70)
                        print('\n[1] Ver todas caronas disponiveis \
                        \n[2] Procurar caronas para você \
                        \n[3] Ver minhas reservas \
                        \n[0] Voltar\n')
                        print('=' * 70)
                        hub_3pass = input ('Digite o digito doque você deseja acessar: ')
                        os.system('cls')
                        print('=' * 70)

                        if hub_3pass == '0':
                            continue

                        elif hub_3pass == '1':
                            passa.mostrar_caronas(usu)
                            passa.marcar_carona(usu)

                        elif hub_3pass == '2':
                            passa.mostrar_caronas_expecificas(usu)
                            passa.marcar_carona(usu)

                        elif hub_3pass == '3':
                            conf = passa.reserva_marcadas(usu)
                            if conf == '1':
                                passa.apagar_reserva(usu)
                    
                    if hub_2 == '2':
                        print('Opções de Condutor:')
                        print('=' * 70)
                        print('\n[1] Cadastrar carona\
                        \n[2] Ver Caronas Cadastradas\
                        \n[0] Voltar\n')
                        print('=' * 70)
                        hub_3cond = input ('Digite o digito doque você deseja acessar: ')
                        os.system('cls')
                        print('=' * 70)

                        if hub_3cond == '0':
                            continue

                        elif hub_3cond == '1':
                            moto.cadastro_carona(usu,email)
                        
                        elif hub_3cond == '2':
                            conf = moto.mostrar_caronas_motorista(usu)
                            if conf == '1':
                                moto.apagar_carona(usu)
    
    elif hub_1 == '3':
        dados.textin_agradecimento()