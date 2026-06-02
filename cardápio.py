
# ==========================
# CARDÁPIO INTELIGENTE
# ==========================

total = 0
pedidos = []

while True:

    print("\n===== CARDÁPIO INTELIGENTE =====")

    nome = input("Digite seu nome: ")

    vegetariano = input("Você é vegetariano? (sim/nao): ").lower()
    dieta = input("Você faz dieta? (sim/nao): ").lower()

    print("\nAnalisando preferências...")

    # VEGETARIANO
    if vegetariano == "sim" and dieta == "nao":

        print("\nPratos recomendados:")

        print("1 - Risoto de Cogumelo Trufado - R$44,90")
        print("2 - Lasanha de Berinjela - R$39,90")

        opcao = int(input("Escolha um prato: "))

        if opcao == 1:
            prato = "Risoto de Cogumelo Trufado"
            valor = 44.90
        else:
            prato = "Lasanha de Berinjela"
            valor = 39.90

    # DIETA
    elif vegetariano == "nao" and dieta == "sim":

        print("\nPratos recomendados:")

        print("1 - Filé de Frango Grelhado com Legumes - R$38,90")
        print("2 - Salmão ao Limão Siciliano - R$64,90")

        opcao = int(input("Escolha um prato: "))

        if opcao == 1:
            prato = "Filé de Frango Grelhado com Legumes"
            valor = 38.90
        else:
            prato = "Salmão ao Limão Siciliano"
            valor = 64.90

    # NÃO É NENHUM
    elif vegetariano == "nao" and dieta == "nao":

        print("\nPratos recomendados:")

        print("1 - Medalhão de Mignon ao Molho Madeira - R$62,90")
        print("2 - Fettuccine Alfredo com Filé Mignon - R$54,90")

        opcao = int(input("Escolha um prato: "))

        if opcao == 1:
            prato = "Medalhão de Mignon ao Molho Madeira"
            valor = 62.90
        else:
            prato = "Fettuccine Alfredo com Filé Mignon"
            valor = 54.90

    # É AMBOS
    else:

        print("\nPratos recomendados:")

        print("1 - Bowl Fit Mediterrâneo - R$32,90")
        print("2 - Salada Proteica de Quinoa - R$34,90")

        opcao = int(input("Escolha um prato: "))

        if opcao == 1:
            prato = "Bowl Fit Mediterrâneo"
            valor = 32.90
        else:
            prato = "Salada Proteica de Quinoa"
            valor = 34.90

    pedidos.append(prato)
    total += valor

    print(f"\n{prato} adicionado ao pedido!")
    print(f"Valor atual: R${total:.2f}")

    continuar = input(
        "\nDeseja pedir mais algum prato? (sim/nao): "
    ).lower()

    if continuar != "sim":
        break

    mesmo_cliente = input(
        "\nÉ o mesmo cliente? (sim/nao): "
    ).lower()

    if mesmo_cliente != "sim":
        print("\nNovo atendimento iniciado!")

# ==========================
# PAGAMENTO
# ==========================

print("\n===== PAGAMENTO =====")

print("1 - Dinheiro (5% desconto)")
print("2 - Cartão")
print("3 - Pix (10% desconto)")

pagamento = int(input("Escolha a forma de pagamento: "))

desconto = 0

if pagamento == 1:
    desconto = total * 0.05
    forma = "Dinheiro"

elif pagamento == 2:
    forma = "Cartão"

elif pagamento == 3:
    desconto = total * 0.10
    forma = "Pix"

valor_final = total - desconto

# ==========================
# CUPOM FISCAL
# ==========================

print("\n==============================")
print("        CUPOM FISCAL")
print("==============================")

print(f"Cliente: {nome}")

print("\nPratos escolhidos:")

for item in pedidos:
    print("-", item)

print(f"\nSubtotal: R${total:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Forma de pagamento: {forma}")

print(f"\nTOTAL A PAGAR: R${valor_final:.2f}")

print("\nPedido finalizado com sucesso!")