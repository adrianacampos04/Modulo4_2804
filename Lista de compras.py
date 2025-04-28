compras = []

while True:
    tarefa = input("Digite sua lista de compras (ou 'sair' para finalizar): ")
    if tarefa.lower() == "sair":
        break
    compras.append(tarefa)

while True:
    compras.sort()
    print("\nLista de Compras:")
    for t in compras:
        print(f"- {t}")

    adicionar_mais = input("\nDeseja adicionar mais itens? (sim/não): ").lower()
    if adicionar_mais == "sim":
        while True:
            novo_item = input("Digite um item para adicionar (ou 'voltar' para voltar): ")
            if novo_item.lower() == "voltar":
                break
            compras.append(novo_item)
    else:
        print("\nFinalizando lista de compras. Obrigado!")
        break

compras = []

while True:
    tarefa = input("Digite sua lista de compras (ou 'sair' para finalizar): ")
    if tarefa.lower() == "sair":
        break
    compras.append(tarefa)

while True:
    compras.sort()
    print("\nLista de Compras:")
    for t in compras:
        print(f"- {t}")

    adicionar_mais = input("\nDeseja adicionar mais itens? (sim/não): ").lower()
    if adicionar_mais == "sim":
        while True:
            novo_item = input("Digite um item para adicionar (ou 'voltar' para voltar): ")
            if novo_item.lower() == "voltar":
                break
            compras.append(novo_item)
    else:
        print("\nFinalizando lista de compras. Obrigado!")
        break

