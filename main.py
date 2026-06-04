def tratar_nome(nome):
    return nome.strip().title()


def criar_saudacao(nome):
    if nome == "":
        return "Você não digitou um nome. Rode o programa novamente."
    else:
        return f"Olá, {nome}. Bem-vindo à sua jornada builder."


def main():
    nome = input("Qual é o seu nome? ")
    nome = tratar_nome(nome)
    print(criar_saudacao(nome))


if __name__ == "__main__":
    main()
