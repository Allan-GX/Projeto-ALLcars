usuarios = []
caronas = []
veiculos = []
emails = []
datas = []
horas = []
chave = []
valor = []

usuarioadm = {
    'nome': 'adm',
    'email': 'a@me.com',
    'senha': '123',
    'pchave' : 'ADM'
}

usuarioadm2 = {
    'nome': 'adm2',
    'email': 'ad@me.com',
    'senha': '654321',
    'pchave' : 'ADM2'
}

carona_pre_cadastrada = {
    'inicio' : 'Cajazeiras',
    'destino' : 'João Pessoa',
    'data' : '30/05/2025',
    'hora' : '00:00',
    'vagas' : 3,
    'preco_vaga' : '500,00',
    'motorista' : 'Kleber',
    'email do motorista' : 'kleb@icloud.com',
    'passageiros' : []
                            
}

carona_pre_cadastrada2 = {
    'inicio' : 'Cajazeiras',
    'destino' : 'Boqueirão',
    'data' : '28/06/2025',
    'hora' : '22:30',
    'vagas' : 30,
    'preco_vaga' : '50,00',
    'motorista' : 'Guilherme Estevo',
    'email do motorista' : 'guilwilliano@hotmail.com',
    'passageiros' : []
                            
}

traducao = {
    'inicio' : 'Início',
    'destino' : 'Destino',
    'data' : 'Data',
    'hora' : 'Horario',
    'vagas' : 'Vagas Restantes',
    'preco_vaga' : 'Preço por vaga',
    'motorista' : 'Motorista',
    'email do motorista' : 'E-mail do Motorista',
    'passageiros' : 'passageiros'
}

usuarios.append(usuarioadm)
usuarios.append(usuarioadm2)
emails.append(usuarioadm['email'])
emails.append(usuarioadm2['email'])
datas.append(carona_pre_cadastrada['data'])
datas.append(carona_pre_cadastrada2['data'])
horas.append(carona_pre_cadastrada['hora'])
horas.append(carona_pre_cadastrada2['hora'])
caronas.append(carona_pre_cadastrada)
caronas.append(carona_pre_cadastrada2)

def textin_agradecimento():
    print("""
Para todos que lerem essa mensagem agradeçemos profundamente, enfim
sejam bens vindos ao ALLcars V.2, nos estamos fazendo umas mundanças
no código do app então estamos abertos a possiveis problemas, qualquer
um queira nos dar apoio, este é um projeto de código aberto, mas sobre 
as mudanças, adicionamos algumas funcionalidades extras, como ver o
valor total ganho nas corridas pelos motoristas, e algumas correções
de bugs, ainda só continuamos trabalhando com endereços emails para
usos pessoais da Microsoft,Google e Apple, mas em breve iremos expan-
dir as opções de cadastro, e com toda certeza essa versão também NÃO
foi feita as Pressas por um aluno que já se imaginava de ferias.\n
No mais esperamos que continue aproveitando nossos serviços!!(☞ﾟヮﾟ)☞
""")
    print('=' * 70)
    input('\n[0] Voltar\n\nDigite:')