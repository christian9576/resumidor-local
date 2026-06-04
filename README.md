# Saudação com Nome

## O que o programa faz

Este projeto é uma mini CLI que pede o nome do usuário no terminal e mostra uma saudação.

O programa mostra um cabeçalho, remove espaços no começo e no fim do nome e formata as palavras com letra inicial maiúscula.

## Como rodar no terminal

```bash
python main.py
```

## Como rodar os testes

Os testes ficam no arquivo `test_main.py`.

```bash
python test_main.py
```

## Exemplo de uso

```text
=== Saudação com Nome ===
Qual é o seu nome? christian frank
Olá, Christian Frank. Bem-vindo à sua jornada builder.
```

Se o usuário não digitar um nome, o programa mostra uma mensagem avisando para rodar novamente.

## Estrutura do código

- `tratar_nome(nome)`: remove espaços no começo/fim e formata o nome com iniciais maiúsculas.
- `criar_saudacao(nome)`: devolve a mensagem correta.
- `main()`: coordena o fluxo do programa.

## Conceitos aprendidos até agora

- Usar `input()` para receber dados do usuário.
- Usar `.strip()` para remover espaços extras.
- Usar `.title()` para formatar nomes.
- Usar `if` e `else` para tomar decisões.
- Usar `print()` e f-strings para mostrar mensagens.
