import random

url = input("Qual a URL? ")
url_limpa = url.strip().lower()

if "admin" in url_limpa  or "login" in url_limpa:
    print("\033[1;31;40mEste site é um alvo de alta prioridade!\033[m")

else:
    print("\033[1;32;40mEste site é um alvo de baixa prioridade!\033[m")

print(f"Foi gerado {random.randint(1, 50)} relatórios sobre o alvo.")
