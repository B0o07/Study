salario = float(input("Digite o salário atual: "))
aumento = float(salario) * 0.10
aumentoInf = float(salario) * 0.15

if salario >= 1250:
    print(f"O aumento é R${aumento:.2f} e o novo salário é R${salario + aumento:.2f}")
else:
    print(f"O aumento é R${aumentoInf:.2f} e o novo salário é R${salario + aumentoInf:.2f}")