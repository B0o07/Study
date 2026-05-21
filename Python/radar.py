vel = int(input("Digite a velocidade do veículo: "))
multa = (vel - 80) * 7

if vel <= 80:
    print("Velocidade dentro do limite permitido.")
else:
    print(f"Velocidade acima do limite. Multa: R$ {multa:.2f}")
    
