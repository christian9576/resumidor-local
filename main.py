from saudacoes import criar_saudacao, deve_sair, tipo_valido, tratar_nome


def mostrar_cabecalho():
    print("=== Saudação com Nome ===")
    print("Escolha uma saudação formal ou informal.")


def pedir_tipo_saudacao():
    while True:
        tipo = input("Tipo de saudação (formal/informal): ").strip().lower()

        if tipo_valido(tipo) or deve_sair(tipo):
            return tipo
        else:
            print("Tipo de saudação inválido. Use 'formal' ou 'informal'.")


def deseja_continuar():
    resposta = input("Deseja criar outra saudação? (s/n): ").strip().lower()
    return resposta == "s"


def main():
    mostrar_cabecalho()

    while True:
        nome = input("Qual é o seu nome? ")

        if deve_sair(nome):
            print("Programa encerrado.")
            return

        nome = tratar_nome(nome)
        tipo = pedir_tipo_saudacao()

        if deve_sair(tipo):
            print("Programa encerrado.")
            return

        print(criar_saudacao(nome, tipo))

        if not deseja_continuar():
            print("Programa encerrado.")
            return


if __name__ == "__main__":
    main()
