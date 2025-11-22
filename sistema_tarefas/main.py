tarefas = []
def adicionar_tarefa():
    print('===== ADICIONAR TAREFA =====')
    tarefa = input('Qual tarefa você deseja adicionar? ').strip()
    if tarefa == '':
        print('Você não pode adicionar uma tarefa vazia.')
        return
    tarefas.append(tarefa)
    print(f'"{tarefa}" adicionada à lista.')
def listar_tarefas():
    print('===== LISTA DE TAREFAS =====')
    if not tarefas:
        print('Não há tarefas no momento.\n')
        return  # impede o for desnecessário
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'{i} - {tarefa}')
    print()  # quebra de linha estética
def remover_tarefa():
    print('===== REMOVER TAREFA ======')
    if not tarefas:
        print('A lista está vazia. Nada para remover.\n')
        return
    listar_tarefas()
    while True:
        opcao = input('Digite o índice que deseja remover: ')
        if not opcao.isdigit():
            print('Digite apenas números.')
            continue
        opcao = int(opcao)
        if 1 <= opcao <= len(tarefas):
            removida = tarefas.pop(opcao - 1)
            print(f'"{removida}" removida com sucesso!\n')
            break
        else:
            print('Índice inválido, tente novamente.')
def menu():
    while True:
        print('===== TAREFAS =====')
        print('1 - Adicionar tarefa')
        print('2 - Listar tarefas')
        print('3 - Remover tarefa')
        print('4 - Sair')
        opcao = input('Digite a opção desejada: ')
        if not opcao.isdigit():
            print('Digite apenas números.\n')
            continue
        opcao = int(opcao)
        if opcao == 1:
            adicionar_tarefa()
        elif opcao == 2:
            listar_tarefas()
        elif opcao == 3:
            remover_tarefa()
        elif opcao == 4:
            print('Saindo...')
            break
        else:
            print('Opção inválida.\n')
menu()
