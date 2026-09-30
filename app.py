materiais = []
proximo_id = 1

def cadastrar_material():
    global proximo_id
    nome = input("Nome do material: ").strip()
    quantidade = int(input("Quantidade inicial: "))
    materiais.append({"id": proximo_id, "nome": nome, "quantidade": quantidade})
    print(f"Material cadastrado com sucesso! ID: {proximo_id}")
    proximo_id += 1

def listar_materiais():
    if not materiais:
        print("Nenhum material cadastrado.")
        return
    print("\n--- LISTA DE MATERIAIS ---")
    for mat in materiais:
        print(f"ID: {mat['id']} | Nome: {mat['nome']} | Quantidade: {mat['quantidade']}")

def atualizar_material():
    id_mat = int(input("Informe o ID do material a atualizar: "))
    for mat in materiais:
        if mat["id"] == id_mat:
            novo_nome = input(f"Novo nome ({mat['nome']}): ").strip()
            nova_qtd = input(f"Nova quantidade ({mat['quantidade']}): ").strip()
            if novo_nome:
                mat["nome"] = novo_nome
            if nova_qtd:
                mat["quantidade"] = int(nova_qtd)
            print("Material atualizado com sucesso!")
            return
    print("Material não encontrado.")

def excluir_material():
    id_mat = int(input("Informe o ID do material a excluir: "))
    for mat in materiais:
        if mat["id"] == id_mat:
            materiais.remove(mat)
            print("Material excluído com sucesso!")
            return
    print("Material não encontrado.")

def registrar_retirada():
    id_mat = int(input("Informe o ID do material para retirada: "))
    for mat in materiais:
        if mat["id"] == id_mat:
            qtd_retirada = int(input("Quantidade a retirar: "))
            mat["quantidade"] -= qtd_retirada
            print(f"Retirada de {qtd_retirada} unidades realizada. Saldo atual: {mat['quantidade']}")
            return
    print("Material não encontrado.")

def main():
    while True:
        print("\n=== SISTEMA DE ALMOXARIFADO ===")
        print("1. Cadastrar Material (Create)")
        print("2. Listar Materiais (Read)")
        print("3. Atualizar Material (Update)")
        print("4. Excluir Material (Delete)")
        print("5. Registrar Retirada")
        print("6. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_material()
        elif opcao == "2":
            listar_materiais()
        elif opcao == "3":
            atualizar_material()
        elif opcao == "4":
            excluir_material()
        elif opcao == "5":
            registrar_retirada()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()