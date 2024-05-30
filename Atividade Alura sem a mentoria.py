""" 
- Criar um sistema que cadastra restaurante, lista eles falando todas as propriedades dele, 
ter a opção de ativar ou desativar o restaurante. Deve ser feito sem ver o codigo principal 
e sem ver a video aula
 """

import os
import random

banco_de_dados_dos_restaurantes = [{'id':'0001', 'nome': 'Reale', 'categoria': 'alemã', 'status': True},
                            {'id':'0002','nome': 'Il Pumo', 'categoria': 'Italiana', 'status': False},
                            {'id':'0003','nome': 'Mira', 'categoria': 'Sagados', 'status': False}]

def boas_vindas():
    print('Cunha-Food \n')
    print('Seja bem vindo ao Sistema Cunha-Food, neste exepcional sistema ') 
    print('você pode cadastrar seu restaurante, ver nossa lista de restaurante já cadastrados')
    print('e ativar seu restaurante para todos os nossos usuarios te ver e comprar seus produtos ;D \n')

def menu():
    print('Digite 1 para cadastrar o restaurante')
    print('Digite 2 para poder ver quais restaurantes estão trabalhando conosco')
    print('Digite 3 para Ativar o restaurante ou Desativar')
    print('Digite 4 sair do sistema')

def interação_com_o_menu():
    numero_digitado = int(input('\n digite a tecla referente a opção que deseja realizar ;D '))
    if numero_digitado == 1:
        cadastrar_restaurante()
    elif numero_digitado == 2:
        lista_de_restaurantes_cadastrados()
    elif numero_digitado == 3:
        ativacao_e_desativacao_de_restaurante()
    elif numero_digitado == 4:
        finalizar_sistema()
    else:
        opção_invalida()

def cadastrar_restaurante():
    os.system('cls')
    print('\n Seja bem vindo ao cadastro de restaurante e obrigado por estar trabalhando conosco')
    cadastro_do_nome = input('\n Por gentileza me diga o nome de seu restaurante ? ')
    cadastro_da_categoria_do_restaurante = input('\n Seu restaurante serve qual tipo de comida ? Italiano, Mediterrano, Humburgueria.....')
    print(f'\n O nome de seu restuarnte é {cadastro_do_nome} e a categoria alimentiacia é {cadastro_da_categoria_do_restaurante}?')
    try:
        confirmação_do_nome_e_categoria = int(input('\n O nome e a categoria esta correto ? caso esteja digite 1 por gentileza para darmos continuidade '))
        if confirmação_do_nome_e_categoria == 1:
            print ('maravilha, para darmos continuidade irei gerar um id do restaurante ')  
            #gera um numero de 1 até 9999
            id_do_restaurante = random.randint(1, 9999)
            # Formatar o ID para ter exatamente 4 dígitos
            id_formatado = str(id_do_restaurante).zfill(4)
            print(f'\n O id de seu restaurante é {id_formatado} ')
            dados_do_restaurante = {'id': id_formatado, 'nome': cadastro_do_nome, 'categoria': cadastro_da_categoria_do_restaurante, 'status':False}
            banco_de_dados_dos_restaurantes.append(dados_do_restaurante)
            main()
        else:
            os.system('cls')
            main()
    except:
        opção_invalida()

def lista_de_restaurantes_cadastrados():
    os.system('cls')
    print('Veja a lista de restaurantes parceiros de nossa empresa')
    print('id do restaurante'.ljust(20), '| nome do restaurante'.ljust(20), '| categoria'.ljust(20), 'status')
    for restaurantes in banco_de_dados_dos_restaurantes:
        id = restaurantes['id']
        nome = restaurantes['nome']
        categoria_do_restaurante = restaurantes['categoria']
        status_do_restaurante = restaurantes['status']
        print(f'{id.ljust(20)}| {nome.ljust(20)} | {categoria_do_restaurante.ljust(20)} | {"Ativo" if status_do_restaurante else "Inativo"}')
    try:
        volta_ao_menu = int(input('Caso seu restaurante não esteja listado ou esteja listado e queira voltar ao menu, digite o número 1 para poder voltar ao menu: '))
        if volta_ao_menu == 1:
            main()
        else:
            opção_invalida()
    except:
        opção_invalida()

def ativacao_e_desativacao_de_restaurante():
    pesquisa_id = input("\nDigite por gentileza o número de ID de seu restaurante: ")
    busca_do_restaurante = False

    for restaurante in banco_de_dados_dos_restaurantes:
        if pesquisa_id == restaurante['id']:
            busca_do_restaurante = True
            restaurante['status'] = not restaurante['status']
            print(f'Encontramos o restaurante {restaurante["nome"]}')
            habilitacao_e_desabilitacao = input('caso seja seu restaurante digite 1 caso não seja digite qualquer outra tecla ')
            if habilitacao_e_desabilitacao == '1':
                mensagem = f'O restaurante {restaurante["nome"]} foi {"ativado" if restaurante["status"] else "desativado"} com sucesso.'
                print(mensagem)
            else:
                main()
    if not busca_do_restaurante:
        print('Restaurante não foi encontrado.')
    volta_ao_menu_ou_encerra_o_programa()







def main():
    """aqui deve ficar todas as funções principais"""

    boas_vindas()
    menu()
    interação_com_o_menu()



def opção_invalida():
    print('Essa opção não existe, estamos voltando para o Menu inicial! ;D \n')
    input('Clique em qualquer tecla para voltar ao menu')
    main()

def finalizar_sistema():
    os.system('cls')
    print('programa encerrado \n')

def volta_ao_menu_ou_encerra_o_programa():
    encerra_ou_volta = int(input('se desejar voltar ao menu digite 1 caso deseja encerrar o programa digete qualquer outra letra '))
    if encerra_ou_volta == 1:
        os.system('cls')
        main()
    else: 
        finalizar_sistema()



if __name__ == '__main__':
    main()