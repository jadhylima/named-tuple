from collections import namedtuple


def adicionar_contato():
    contato = namedtuple('Contato',['Nome','Telefone','Email'])
    nome = input('\nDigite o nome do contato: ').upper()
    telefone = str(input('Digite o número de telefone: '))
    email = input('Digite o email: ').upper()
    agenda.append(contato(nome, telefone, email))
    agenda_nomes.append(nome)
    print(f'\nO contato {nome} foi adiconado a sua agenda.')


def remover_contato(deletar):
    for contato in agenda:
        if contato[0] == deletar:
            print(f'{contato[0]} foi removido(a) da sua agenda.')
            agenda.remove(contato)
            agenda_nomes.remove(deletar)


def busca_nome(busca):
    encontrados = []
    for contato in agenda:
        if busca in contato[0]:
            encontrados.append(contato)
    for contatos in encontrados:
        print(contatos)


print('Agenda\n')
agenda = []
agenda_nomes = []
while True:
    escolha = int(input('\nMenu\n1 para adicionar um contato\n2 para remover um contato\n3 para listar todos os contatos\n'
                        '4 para listar os nomes dos contatos\n5 para buscar um contato utilizando o nome\n0 para sair\n--> '))
    
    if escolha == 1:
        adicionar_contato()

    elif escolha == 2:
        if not agenda:
            print('\nA sua agenda está vazia. Retornando ao Menu...')
            continue
        deletar = input('\nDigite o nome do contato que deseja remover: ').upper()
        remover_contato(deletar)

    elif escolha == 3:
        if not agenda:
            print('A sua agenda está vazia. Retornando ao Menu...')
            continue
        for pessoa in agenda:
            print(pessoa)
    
    elif escolha == 4:
        if not agenda_nomes:
            print('\nA sua agenda está vazia. Retornando ao Menu...')
            continue
        for pessoa in agenda_nomes:
            print('\n', pessoa)
    
    elif escolha == 5:
        busca = input('\nDigite o nome do contato: ').upper()
        busca_nome(busca)

    elif escolha == 0:
        print('\nEncerrando...')
        break
