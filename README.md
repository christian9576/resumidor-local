# Saudação com Nome

## O que o programa faz

Este projeto é uma mini CLI que pede o nome do usuário no terminal e mostra uma saudação informal, formal ou motivacional.

O programa mostra um cabeçalho, remove espaços no começo e no fim do nome, formata as palavras com letra inicial maiúscula e permite escolher o tipo de saudação.

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
Tipo de saudação: motivacional
Olá, Christian Frank. Continue construindo sua jornada builder.
```

O tipo de saudação aceita `informal`, `formal` ou `motivacional`.

A opção `motivacional` mostra: `Olá, [nome]. Continue construindo sua jornada builder.`

Se o usuário digitar outro valor, o programa avisa e pergunta novamente.

O usuário pode digitar `sair` na pergunta do nome ou na pergunta do tipo de saudação para encerrar o programa.

Se o usuário não digitar um nome, o programa mostra uma mensagem avisando para rodar novamente.

## Estrutura do código

- `TIPOS_VALIDOS`: lista com os tipos de saudação aceitos.
- `tipo_valido(tipo)`: verifica se o tipo informado está entre os tipos aceitos.
- `deve_sair(texto)`: verifica se o usuário digitou `sair`.
- `tratar_nome(nome)`: limpa e formata o nome.
- `criar_saudacao(nome, tipo)`: devolve a mensagem correta.
- `pedir_tipo_saudacao()`: pede o tipo até receber uma opção válida ou `sair`.
- `main()`: coordena o fluxo do programa.

## Conceitos aprendidos até agora

- Usar `input()` para receber dados do usuário.
- Usar `.strip()` para remover espaços extras.
- Usar `.title()` para formatar nomes.
- Usar `if` e `else` para tomar decisões.
- Usar `print()` e f-strings para mostrar mensagens.
