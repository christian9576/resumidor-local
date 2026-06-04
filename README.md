# Saudação com Nome

## O que o programa faz

Este projeto é uma mini CLI que pede o nome do usuário no terminal e mostra uma saudação informal, formal ou motivacional.

O programa mostra um cabeçalho, remove espaços no começo e no fim do nome, formata as palavras com letra inicial maiúscula e permite criar várias saudações na mesma execução.

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
Escolha uma saudação formal ou informal.
Qual é o seu nome? christian frank
Tipo de saudação (formal/informal): motivacional
Olá, Christian Frank. Continue construindo sua jornada builder.
Deseja criar outra saudação? (s/n): n
Programa encerrado.
```

O tipo de saudação aceita `informal`, `formal` ou `motivacional`.

A opção `motivacional` mostra: `Olá, [nome]. Continue construindo sua jornada builder.`

Se o usuário digitar outro valor, o programa avisa e pergunta novamente.

O usuário pode digitar `sair` na pergunta do nome ou na pergunta do tipo de saudação para encerrar o programa.

Depois de mostrar uma saudação, o programa pergunta `Deseja criar outra saudação? (s/n): `. Se o usuário responder `s`, o fluxo recomeça. Qualquer outra resposta encerra o programa.

Se o usuário não digitar um nome, o programa mostra uma mensagem avisando para rodar novamente.

## Estrutura do código

- `main.py`: entrada da CLI, responsável por `input()`, `print()` e fluxo do programa.
- `saudacoes.py`: contém as regras de saudação, validação e tratamento.
- `test_main.py`: contém os testes automatizados simples.
- `README.md`: documentação do projeto.
- `.gitignore`: ignora arquivos automáticos do Python.

## Conceitos aprendidos até agora

- Usar `input()` para receber dados do usuário.
- Usar `.strip()` para remover espaços extras.
- Usar `.title()` para formatar nomes.
- Usar `if` e `else` para tomar decisões.
- Usar `print()` e f-strings para mostrar mensagens.
