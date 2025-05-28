agenda = {}

def adicionar():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    agenda[nome] = telefone

def buscar():
    nome = input("Nome para buscar: ")
    if nome in agenda:
        print(f"{nome}: {agenda[nome]}")
    else:
        print("Contato não encontrado.")

def remover():
    nome = input("Nome para remover: ")
    if nome in agenda:
        del agenda[nome]
        print("Removido.")
    else:
        print("Contato não encontrado.")

while True:
    print("\n1-Adicionar 2-Buscar 3-Remover 4-Sair")
    opcao = input("Escolha: ")
    if opcao == '1': adicionar()
    elif opcao == '2': buscar()
    elif opcao == '3': remover()
    elif opcao == '4': break
