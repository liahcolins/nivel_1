#PDV com descontos por idade e por valor da compra.
#o programa termina quando o valor da compra informado for 0.

historico = []

while True:
    valor = float(input("digite o valor da compra (0 para encerrar): R$ "))

    if valor < 0:
        print("o valor da compra não pode ser negativo, tente novamente")
        continue

    if valor == 0:
        break

    while True:
        idade = int(input("digite a idade do cliente: "))

        if idade < 0:
            print("a idade não pode ser negativa, digite novamente")
            continue

        break

    valor_original = round(valor, 2)
    desconto_idade = 0.0
    desconto_valor = 0.0

    if idade >= 65:
        desconto_idade = round(valor_original * 0.20, 2)

    valor_apos_idade = round(valor_original - desconto_idade, 2)

    if valor_apos_idade > 100:
        desconto_valor = round(valor_apos_idade * 0.10, 2)

    valor_final = round(valor_apos_idade - desconto_valor, 2)
    desconto_total = round(valor_original - valor_final, 2)

    historico.append({
        "valor_original": valor_original,
        "idade": idade,
        "desconto_idade": desconto_idade,
        "desconto_valor": desconto_valor,
        "desconto_total": desconto_total,
        "valor_final": valor_final,
    })

    print(f"desconto por idade: R$ {desconto_idade:.2f}")
    print(f"desconto por valor: R$ {desconto_valor:.2f}")
    print(f"valor final: R$ {valor_final:.2f}")
    print("-" * 40)

quantidade_compras = len(historico)
total_bruto = 0.0
total_descontos = 0.0
total_final = 0.0

for compra in historico:
    total_bruto += compra["valor_original"]
    total_descontos += compra["desconto_total"]
    total_final += compra["valor_final"]

total_bruto = round(total_bruto, 2)
total_descontos = round(total_descontos, 2)
total_final = round(total_final, 2)

print("\n========== RESUMO DO DIA ==========")
print(f"quantidade de compras: {quantidade_compras}")
print(f"total bruto: R$ {total_bruto:.2f}")
print(f"total de descontos: R$ {total_descontos:.2f}")
print(f"total final: R$ {total_final:.2f}")
print("===================================")