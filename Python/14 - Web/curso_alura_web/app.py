import os

restaurantes = [
    {'nome':'Hamburgueria do Super','categoria':'Lanche','ativo':True},
    {'nome':'Dominos','categoria':'Pizza','ativo':True},
    {'nome':'Chiquinhos Bar','categoria':'Bar','ativo':False}
]

def exibir_nome_do_programa():
    print('''
          ⟆Ꭿᑲ𝖮ᖇ ᕮⲭᖰᖇ∈⟆⟆
    ''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')
    print('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal.')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input('Digite a categoria do restaurante que deseja cadastrar: ')
    
    dados_do_restaurante = {
        'nome':nome_do_restaurante,
        'categoria':categoria_do_restaurante,
        'ativo':False
        }
    
    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()
    main()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    
    for idx,restaurante in enumerate(restaurantes,start=1):
        
        nome_resurante = restaurante['nome']
        categoria = restaurante['categoria']
        print(f'{idx}- {nome_resurante} | {categoria}')
        
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    main()
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()