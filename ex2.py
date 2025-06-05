def calcular_preco_ingresso(tipo_evento, qtd_eventos, eh_estudante):
    if tipo_evento == 1:
        preco_base = 50.00  # show
    else:
        preco_base = 30.00  # palestra

    custo_total = preco_base * qtd_eventos

    if eh_estudante:
        custo_total *= 0.5  # 50% de desconto

    return round(custo_total, 2)

print("Bem-vindo ao Simulador de Preço de Ingresso!")

# Validação do tipo de evento
while True:
    try:
        tipo_evento = int(input("Tipo de evento [1: Show, 2: Palestra]: "))
        if tipo_evento in [1, 2]:
            break
        else:
            print("Tipo inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite 1 ou 2.")

# Validação da quantidade de eventos
while True:
    try:
        qtd_eventos = int(input("Quantidade de eventos: "))
        if qtd_eventos > 0:
            break
        else:
            print("A quantidade deve ser maior que zero. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro maior que zero.")

# Validação se é estudante
while True:
    resposta = input("Você é estudante? [S/N]: ").strip().upper()
    if resposta in ['S', 'N']:
        eh_estudante = resposta == 'S'
        break
    else:
        print("Resposta inválida. Digite S para sim ou N para não.")

# Chamada da função
preco = calcular_preco_ingresso(tipo_evento, qtd_eventos, eh_estudante)

# Resultado final
tipo_str = "Show" if tipo_evento == 1 else "Palestra"
print(f"\nResumo:")
print(f"Tipo de evento: {tipo_str}")
print(f"Quantidade de eventos: {qtd_eventos}")
print(f"Estudante: {'Sim' if eh_estudante else 'Não'}")
print(f"Preço final: R$ {preco:.2f}")
