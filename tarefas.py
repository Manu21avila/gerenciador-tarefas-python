tarefas = []

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)

    elif opcao == "2":
        for i, t in enumerate(tarefas):
            print(i, "-", t)

    elif opcao == "3":
        indice = int(input("Número da tarefa: "))
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)

    elif opcao == "4":
        break

    else:
        print("Opção inválida")
