from main import criar_saudacao


def test_criar_saudacao_com_nome():
    resultado = criar_saudacao("Christian")
    assert resultado == "Olá, Christian. Bem-vindo à sua jornada builder."


def test_criar_saudacao_sem_nome():
    resultado = criar_saudacao("")
    assert resultado == "Você não digitou um nome. Rode o programa novamente."


def main():
    test_criar_saudacao_com_nome()
    test_criar_saudacao_sem_nome()
    print("Todos os testes passaram.")


if __name__ == "__main__":
    main()
