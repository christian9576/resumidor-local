TIPOS_VALIDOS = ["formal", "informal", "motivacional"]


def tratar_nome(nome):
    return nome.strip().title()


def deve_sair(texto):
    return texto.strip().lower() == "sair"


def tipo_valido(tipo):
    return tipo in TIPOS_VALIDOS


def criar_saudacao(nome, tipo):
    if nome == "":
        return "Você não digitou um nome. Rode o programa novamente."
    elif tipo == "formal":
        return f"Olá, {nome}. Seja bem-vindo à sua jornada builder."
    elif tipo == "informal":
        return f"Olá, {nome}. Bem-vindo à sua jornada builder."
    elif tipo == "motivacional":
        return f"Olá, {nome}. Continue construindo sua jornada builder."
    else:
        return "Tipo de saudação inválido. Use 'formal' ou 'informal'."
