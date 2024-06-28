Agenda de Contatos

Este é um programa simples em Python para gerenciar uma agenda de contatos. Ele permite adicionar, remover, listar e buscar contatos pelo nome. O programa utiliza a biblioteca collections para criar uma estrutura de dados nomeada (namedtuple) para armazenar os contatos.

Funcionalidades:
1. Adicionar Contato: Adiciona um novo contato à agenda.
2. Remover Contato: Remove um contato existente da agenda.
3. Listar Contatos: Exibe todos os contatos armazenados na agenda.
4. Listar Nomes dos Contatos: Exibe apenas os nomes dos contatos armazenados na agenda.
5. Buscar Contato pelo Nome: Permite buscar contatos pelo nome.

ESTRUTURA DO CÓDIGO

Funções:
1. adicionar_contato(): Solicita ao usuário as informações do contato (nome, telefone e email), cria um novo contato e o adiciona à agenda.
2. remover_contato(deletar): Remove um contato da agenda pelo nome.
3. busca_nome(busca): Busca e exibe contatos cujo nome contém a string fornecida.

Variáveis Globais:
1. agenda: Lista que armazena todos os contatos.
2. agenda_nomes: Lista que armazena apenas os nomes dos contatos para facilitar a busca e listagem.

Fluxo Principal:
O programa exibe um menu de opções e executa a ação correspondente conforme a escolha do usuário. As opções incluem adicionar, remover, listar contatos, listar nomes e buscar contatos. O programa continua em execução até que o usuário escolha a opção de sair.

Como Executar:
1. Execute o script Python.
2. Siga as instruções no menu para adicionar, remover, listar ou buscar contatos.
3. Para sair do programa, escolha a opção 0 no menu.

Exemplo de Uso
---------------------------------------------------------------------------------
Menu
1. para adicionar um contato
2. para remover um contato
3. para listar todos os contatos
4. para listar os nomes dos contatos
5. para buscar um contato utilizando o nome
6. para sair
--> 
---------------------------------------------------------------------------------
Requisitos:
Python 3.x

Notas:
1. Os nomes dos contatos são armazenados em letras maiúsculas para facilitar a busca e evitar duplicidades.
2. O programa não salva os contatos em um arquivo; os dados são perdidos quando o programa é encerrado.

Melhorias Futuras:
1. Implementar a funcionalidade de salvar e carregar contatos de um arquivo.
2. Adicionar validação de entrada para números de telefone e emails.
3. Melhorar a interface do usuário com um menu mais intuitivo.
