name = input("Qual é o seu nome? ")
mat = int(input("Qual a sua nota em matemática? "))
port = int(input("Qual a sua nota em português? "))
hist = int(input("Qual a sua nota em história? "))
geo = int(input("Qual a sua nota em geografia? "))
ing = int(input("Qual a sua nota em inglês? "))
media = round((mat + port + hist + geo + ing) / 5)

if mat >= 5 and port >= 5 and hist >= 5 and geo >= 5 and ing >= 5:

    print(f"\n{name}, a sua média é: {media}\n")

    if media >= 7:
        print(f"Parabéns, {name}! Você foi aprovado!\n")

    else:
        print(f"Infelizmente, {name}, você não foi aprovado.\n")

if mat < 5 or port < 5 or hist < 5 or geo < 5 or ing < 5:
    print(f"Infelizmente, {name}, você não foi aprovado.\n")