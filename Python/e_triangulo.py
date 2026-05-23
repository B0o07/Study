r1 = int(input("Digite o valor do primeiro lado do triângulo: "))
r2 = int(input("Digite o valor do segundo lado do triângulo: "))
r3 = int(input("Digite o valor do terceiro lado do triângulo: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os valores formam um triângulo")

else:
    print("Os valores não formam um triângulo")