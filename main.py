import json
import os

ARQUIVO = "gastos.json"

def carregar_gastos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_gastos(gastos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)

def adicionar_gasto(gastos):
    valor = float(input("Valor do gasto: R$ "))
    categoria = input("Categoria: ")

    gasto = {
        "valor": valor,
        "categoria": categoria
    }

    gastos.append(gasto)
    salvar_gastos(gastos)
    print("✅ Gasto adicionado com sucesso!")

def listar_gastos(gastos):
    if not gastos:
        print("Nenhum gasto registrado.")
        return

    print("\n📋 Lista de gastos:")
    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. R$ {gasto['valor']:.2f} - {gasto['categoria']}")

def total_gastos(gastos):
    total = sum(gasto["valor"] for gasto in gastos)
    print(f"\n💰 Total gasto: R$ {total:.2f}")

def total_por_categoria(gastos):
    categorias = {}

    for gasto in gastos:
        cat = gasto["categoria"]
        categorias[cat] = categorias.get(cat, 0) + gasto["valor"]

    print("\n📊 Total por categoria:")
    for cat, total in categorias.items():
        print(f"{cat}: R$ {total:.2f}")

def menu():
    print("""
=== CONTROLE DE GASTOS ===
1 - Adicionar gasto
2 - Listar gastos
3 - Total gasto
4 - Total por categoria
0 - Sair
""")

def main():
    gastos = carregar_gastos()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_gasto(gastos)
        elif opcao == "2":
            listar_gastos(gastos)
        elif opcao == "3":
            total_gastos(gastos)
        elif opcao == "4":
            total_por_categoria(gastos)
        elif opcao == "0":
            print("Saindo... até mais 💸")
            break
        else:
            print("Opção inválida, tenta de novo.")

if __name__ == "__main__":
    main()
