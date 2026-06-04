from unittest.mock import patch

from main import criar_saudacao, deve_sair, pedir_tipo_saudacao, tratar_nome


def test_criar_saudacao_informal():
    resultado = criar_saudacao("Christian", "informal")
    assert resultado == "Olá, Christian. Bem-vindo à sua jornada builder."


def test_criar_saudacao_formal():
    resultado = criar_saudacao("Christian", "formal")
    assert resultado == "Olá, Christian. Seja bem-vindo à sua jornada builder."


def test_criar_saudacao_tipo_invalido():
    resultado = criar_saudacao("Christian", "alegre")
    assert resultado == "Tipo de saudação inválido. Use 'formal' ou 'informal'."


def test_criar_saudacao_sem_nome():
    resultado = criar_saudacao("", "formal")
    assert resultado == "Você não digitou um nome. Rode o programa novamente."


def test_tratar_nome_com_espacos():
    resultado = tratar_nome("   christian frank   ")
    assert resultado == "Christian Frank"


def test_tratar_nome_sem_nome():
    resultado = tratar_nome("   ")
    assert resultado == ""


def test_deve_sair():
    assert deve_sair("sair") == True
    assert deve_sair(" Sair ") == True
    assert deve_sair("formal") == False


def test_pedir_tipo_saudacao_tenta_ate_ser_valido():
    with patch("builtins.input", side_effect=["banana", "formal"]), patch("builtins.print"):
        resultado = pedir_tipo_saudacao()

    assert resultado == "formal"


def test_pedir_tipo_saudacao_aceita_sair():
    with patch("builtins.input", return_value=" Sair "):
        resultado = pedir_tipo_saudacao()

    assert resultado == "sair"


def main():
    test_criar_saudacao_informal()
    test_criar_saudacao_formal()
    test_criar_saudacao_tipo_invalido()
    test_criar_saudacao_sem_nome()
    test_tratar_nome_com_espacos()
    test_tratar_nome_sem_nome()
    test_deve_sair()
    test_pedir_tipo_saudacao_tenta_ate_ser_valido()
    test_pedir_tipo_saudacao_aceita_sair()
    print("Todos os testes passaram.")


if __name__ == "__main__":
    main()
