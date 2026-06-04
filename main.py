def criar_saudacao(nome):
    if nome == "":
        return "Você não digitou um nome. Rode o programa novamente."
    else:
        return f"Olá, {nome}. Bem-vindo à sua jornada builder."


def main():
    nome = input("Qual é o seu nome? ").strip().title()
    print(criar_saudacao(nome))


if __name__ == "__main__":
    main()
