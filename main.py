def tratar_nome(nome):
    return nome.strip().title()


def criar_saudacao(nome, tipo):
    if nome == "":
        return "Você não digitou um nome. Rode o programa novamente."
    elif tipo == "formal":
        return f"Olá, {nome}. Seja bem-vindo à sua jornada builder."
    else:
        return f"Olá, {nome}. Bem-vindo à sua jornada builder."


def mostrar_cabecalho():
    print("=== Saudação com Nome ===")


def main():
    mostrar_cabecalho()
    nome = input("Qual é o seu nome? ")
    nome = tratar_nome(nome)
    tipo = input("Tipo de saudação (formal ou informal): ").strip().lower()
    print(criar_saudacao(nome, tipo))


if __name__ == "__main__":
    main()
