from main import criar_saudacao, tratar_nome


def test_criar_saudacao_com_nome():
    resultado = criar_saudacao("Christian")
    assert resultado == "Olá, Christian. Bem-vindo à sua jornada builder."


def test_criar_saudacao_sem_nome():
    resultado = criar_saudacao("")
    assert resultado == "Você não digitou um nome. Rode o programa novamente."


def test_tratar_nome_com_espacos():
    resultado = tratar_nome("   christian frank   ")
    assert resultado == "Christian Frank"


def test_tratar_nome_sem_nome():
    resultado = tratar_nome("   ")
    assert resultado == ""


def main():
    test_criar_saudacao_com_nome()
    test_criar_saudacao_sem_nome()
    test_tratar_nome_com_espacos()
    test_tratar_nome_sem_nome()
    print("Todos os testes passaram.")


if __name__ == "__main__":
    main()
