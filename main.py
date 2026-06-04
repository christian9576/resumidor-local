nome = input("Qual é o seu nome? ").strip().title()

if nome == "":
    print("Você não digitou um nome. Rode o programa novamente.")
else:
    print(f"Olá, {nome}. Bem-vindo à sua jornada builder.")
