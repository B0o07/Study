via = int(input("Digite a distância da viagem em km: "))
menor = via * 0.50
maior = via * 0.45

if via <= 200:
    print(f"O valor da passagem é R$ {menor:.2f}")
else:
    print(f"O valor da passagem é R$ {maior:.2f}")