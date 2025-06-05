def calcular_custo_viagem(distancia, consumo, bio):
 
    
    preco_combustivel = 6
    consumo_em_litro = distancia / consumo
    custo_total = preco_combustivel * consumo_em_litro

    if bio:
        custo_total = custo_total - 20

    return custo_total

while True:
    try:
        distancia = float(input("Distância em (Km): "))
        if distancia <= 0:
            print("A distância deve ser maior que 0.")
            continue
        break
    except ValueError:
        print("Digite um valor numérico válido para a distância.")

while True:
    try:
        consumo = float(input("Consumo (Km/l): "))
        if consumo <= 0:
            print("O consumo deve ser maior que 0.")
            continue
        break
    except ValueError:
        print("Digite um valor numérico válido para o consumo.")

bio = input("Usa biocombustível? (True/False): ").strip().lower() == "true"

print(calcular_custo_viagem(distancia, consumo, bio))