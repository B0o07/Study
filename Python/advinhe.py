from random import randint

adivinha = randint(0, 5)
print('-=-' * 11)
print("Bem-vindo ao jogo de adivinhação!")
print('-=-' * 11)
adv = int(input("Tente adivinhar o número que estou pensando, entre 0 e 5? "))

if adv == adivinha:
    print("Parabéns! Você acertou!")

else:
    print(f"Ganhei! O número correto era {adivinha}.")

print('-=-' * 11)
print("Obrigado por jogar!")
print('-=-' * 11)
