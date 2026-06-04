def tratar_nome(nome):
    return nome.strip().title()


def criar_saudacao(nome, tipo):
    if nome == "":
        return "Você não digitou um nome. Rode o programa novamente."
    elif tipo == "formal":
        return f"Olá, {nome}. Seja bem-vindo à sua jornada builder."
    elif tipo == "informal":
        return f"Olá, {nome}. Bem-vindo à sua jornada builder."
    else:
        return "Tipo de saudação inválido. Use 'formal' ou 'informal'."


def mostrar_cabecalho():
    print("=== Saudação com Nome ===")
    print("Escolha uma saudação formal ou informal.")


def pedir_tipo_saudacao():
    while True:
        tipo = input("Tipo de saudação (formal/informal): ").strip().lower()

        if tipo == "formal" or tipo == "informal" or tipo == "sair":
            return tipo
        else:
            print("Tipo de saudação inválido. Use 'formal' ou 'informal'.")


def main():
    mostrar_cabecalho()
    nome = input("Qual é o seu nome? ")

    if nome.strip().lower() == "sair":
        print("Programa encerrado.")
        return

    nome = tratar_nome(nome)
    tipo = pedir_tipo_saudacao()

    if tipo == "sair":
        print("Programa encerrado.")
        return

    print(criar_saudacao(nome, tipo))


if __name__ == "__main__":
    main()
