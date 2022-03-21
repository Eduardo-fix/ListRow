# 2010552 - Eduardo Max dos Reis Silva

#Criação da Fila
fila = [];

#Criação do Menu de opções
option_menu = 0;
while option_menu !=5:
    print('''
        MENU:

        [1] - Enfileirar
        [2] - Desenfileirar
        [3] - Limpar
        [4] - Mostrar Fila
        [5] - Sair
    ''')
    option_menu = int(input('Escolha uma opção: '));

#Adicionando itens a Fila
    if option_menu == 1:
        itens_fila = int(input('Quantos itens quer adicionar na fila? MAX. 100: '))
        if itens_fila > 100:
            print('Erro! Número de itens ultrapassa valor máximo.');
        else:
            for x in range(0, itens_fila):
                final = input('Insira os itens em sua fila: ');
                fila.append(final);
        print('Itens adicionados com sucesso!');
        print('Retornando ao menu...');

#Removendo itens da Fila
    if option_menu == 2:
        retira_fila = int(input('O primeiro item adicionado será removido! Confirmar? (1 - Sim/ 2- Não): '))
        if retira_fila == 1:
            item_removido = fila.pop(0);
            print('O primeiro item foi removido com sucesso!'); 
        else:
            print('Cancelando operação!');
        print('Retornando ao menu...');

#Limpando fila
    if option_menu == 3:
        limpar_fila = int(input('A fila será excluída! Confirmar? (1 - Sim/ 2- Não): '))
        if limpar_fila == 1:
            fila.clear();
            print('Limpeza concluída!'); 
        else:
            print('Cancelando operação!');
        print('Retornando ao menu...');

#Mostrando fila enumerada
    if option_menu == 4:
        for indice, dados in enumerate(fila):
            print('Indice:',indice, 'Elemento:',dados);
        print('Retornando ao menu...');

#Encerrando loop do menu
    if option_menu == 5:
        print('Encerrando programa!')
        break;
            
