import os

restaurantes_cadastrados = [{'nome': 'Reale', 'categoria': 'alemã', 'status': True},
                            {'nome': 'Il Pumo', 'categoria': 'Italiana', 'status': False},
                            {'nome': 'Mira', 'categoria': 'Sagados', 'status': False}]


def bem_vindo():
    print('Seja bem vindo ao sistema de cadastro de restaurante')
    print('Como posso te ajudar ?\n')


def opções_do_programa():
    print('opção 1: Cadastrar restaurante ')
    print('opção 2: Listar restaurantes disponiveis')
    print('opção 3: Ativar/Desativar Restaurante')
    print('opção 4: Sair do programa\n')


def opção_escolhida():
    try:
        opção_escolhida = int(input('Qual opção deseja realizar ? '))
        if opção_escolhida == 1:
            cadastrar_restaurante()
        elif opção_escolhida == 2:
            lista_restaurantes()
        elif opção_escolhida == 3:
            ativação_e_desativação_de_restaurante()
        elif opção_escolhida == 4:
            finalizar_sistema()
        else:
            opção_invalida()
    except:
        opção_invalida()


def cadastrar_restaurante():
    os.system('cls')
    print('Seja bem vindo ao cadastro de restaurantes!\n')
    nome_do_restaurante = input('Digite o nome de seu restaurante por favor: ')
    categoria = input(f'Qual a categoria do seu restaurante? (Ex: Italiano, Mediterrâneo, Pizzaria, Self-service) {nome_do_restaurante}:\n ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'status': False}
    print(f'O nome de seu restaurante é {nome_do_restaurante} e a sua categoria alimentícia é {categoria}')
    try:
        confirmação_de_dados = int(input('Os dados de seu restaurante estão corretos? Se sim, digite 1. Se não, aperte qualquer tecla diferente para recadastrar: '))
        if confirmação_de_dados == 1:
            restaurantes_cadastrados.append(dados_do_restaurante)
            main()
        else:
            os.system('cls')
            cadastrar_restaurante()
    except:
        opção_invalida()


def lista_restaurantes():
    os.system('cls')
    print('Bem vindo à listagem de restaurantes. Atualmente temos os seguintes restaurantes cadastrados:\n')
    print('Nome dos Restaurantes'.ljust(20), '| Categoria'.ljust(20), '| Status')
    for restaurante in restaurantes_cadastrados:
        nome = restaurante['nome']
        categoria_do_restaurante = restaurante['categoria']
        status_do_restaurante = restaurante['status']
        print(f'{nome.ljust(20)} | {categoria_do_restaurante.ljust(20)} | {"Ativo" if status_do_restaurante else "Inativo"}')

    try:
        volta_ao_menu = int(input('Caso seu restaurante não esteja listado ou esteja listado e queira voltar ao menu, digite o número 1 para poder voltar ao menu: '))
        if volta_ao_menu == 1:
            main()
        else:
            opção_invalida()
    except:
        opção_invalida()


def ativação_e_desativação_de_restaurante():
    restaurante_buscado = input('Qual o nome do restaurante que deseja ativar ou desativar? ')
    busca_restaurante = False

    for nome_do_restaurante in restaurantes_cadastrados:
        if restaurante_buscado == nome_do_restaurante['nome']:
            busca_restaurante = True
            nome_do_restaurante['status'] = not nome_do_restaurante ['status']
            mensagem = f'O restaurante {restaurante_buscado} foi ativado com sucesso' if nome_do_restaurante ['status'] else f'O restaurante {restaurante_buscado} foi desativado com sucesso'
            print(mensagem)
    if not busca_restaurante:
        print('Restaurante não foi encontrado')


def opção_invalida():
    print('Essa opção não existe, estamos voltando para o Menu inicial! ;D \n')
    input('Clique em qualquer tecla para voltar ao menu')
    main()


def finalizar_sistema():
    os.system('cls')
    print('Encerrando o programa\n')


def main():
    os.system('cls')
    bem_vindo()
    opções_do_programa()
    opção_escolhida()


if __name__ == '__main__':
    main()

