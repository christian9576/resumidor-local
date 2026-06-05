# Guia do Módulo 1 — Primeiros passos como builder com IA

## 1. Objetivo do módulo

O objetivo deste modulo foi aprender o ciclo basico de desenvolvimento usando Python, Codex, Git, GitHub e testes.

A ideia nao era criar um sistema grande. O foco foi entender como um projeto nasce pequeno, ganha organizacao aos poucos e passa a ter um fluxo mais profissional: escrever codigo, executar no terminal, testar, revisar mudancas, salvar no Git e enviar para o GitHub.

Este projeto comecou como uma saudacao simples em Python e evoluiu para uma mini CLI organizada. Isso mostra um modelo importante: projetos reais nao precisam nascer completos. Eles podem evoluir por pequenas melhorias.

## 2. O que foi construído

Foi criada uma mini CLI de saudacao. CLI significa "interface de linha de comando", ou seja, um programa usado pelo terminal.

O programa permite:

- pedir o nome do usuario
- escolher entre saudacao informal, formal e motivacional
- usar a opcao `sair`
- repetir o fluxo para criar varias saudacoes
- validar entradas digitadas pelo usuario
- rodar testes automatizados simples

Na pratica, o usuario executa o programa, responde perguntas no terminal e recebe uma mensagem de saudacao como resultado.

## 3. Estrutura final do projeto

O projeto ficou separado em arquivos com responsabilidades diferentes:

- `main.py`: ponto de entrada da CLI. E o arquivo que conversa com o usuario usando `input()` e `print()`. Tambem organiza o fluxo do programa.
- `saudacoes.py`: arquivo com a logica principal das saudacoes. Ele concentra regras, tratamento de texto e validacoes.
- `test_main.py`: arquivo com testes automatizados simples para conferir se o programa se comporta como esperado.
- `README.md`: documentacao principal do projeto. Explica o que o programa faz, como rodar e como testar.
- `.gitignore`: arquivo que diz ao Git quais arquivos ou pastas devem ser ignorados, como arquivos automaticos do Python.

Essa separacao ajuda a manter o projeto mais facil de entender. A interface fica em um lugar, a logica fica em outro e os testes ficam separados.

## 4. Conceitos de terminal

O terminal e o lugar onde chamamos programas por comandos.

Quando digitamos:

```bash
python main.py
```

estamos pedindo ao Python para executar o arquivo `main.py`.

Quando digitamos:

```bash
python test_main.py
```

estamos pedindo ao Python para executar os testes que estao em `test_main.py`.

Existe uma diferenca importante entre abrir um arquivo e executar um arquivo:

- abrir um arquivo: ver ou editar o conteudo no VS Code
- executar um arquivo: pedir para o computador rodar aquele codigo

No VS Code, voce pode estar olhando para `main.py`, mas isso nao significa que o programa esta rodando. Para rodar, voce precisa executar o comando no terminal.

## 5. Conceitos de Python aprendidos

### Variaveis

Variaveis guardam valores para serem usados depois.

Exemplo mental: uma variavel e uma caixinha com nome. Dentro dela pode estar um texto, um numero ou outro valor.

### Constantes

Constantes tambem guardam valores, mas representam algo que nao deve mudar durante o programa.

Em Python, por convencao, nomes de constantes costumam ficar em letras maiusculas.

### `input()`

`input()` serve para receber texto digitado pelo usuario no terminal.

### `print()`

`print()` serve para mostrar informacoes no terminal.

### Funcoes

Funcoes sao blocos de codigo com nome. Elas ajudam a organizar o programa e evitar repeticao.

Uma funcao pode receber dados, processar esses dados e devolver um resultado.

### Parametros

Parametros sao as entradas de uma funcao.

Se a funcao fosse uma pequena maquina, os parametros seriam aquilo que colocamos dentro dela para trabalhar.

### `return`

`return` e a saida de uma funcao. Ele devolve um valor para quem chamou a funcao.

### `if` / `else`

`if` e `else` permitem tomar decisoes.

Exemplo mental:

```text
se isso acontecer, faca uma coisa
caso contrario, faca outra
```

### `while`

`while` cria repeticao enquanto uma condicao for verdadeira.

No projeto, esse conceito aparece na ideia de repetir o fluxo para criar novas saudacoes.

### Listas

Listas guardam varios valores em uma mesma estrutura.

Elas sao uteis quando queremos representar um conjunto de opcoes ou dados relacionados.

### Metodos de texto

Alguns metodos importantes usados ou discutidos:

- `strip()`: remove espacos no comeco e no fim de um texto
- `title()`: coloca as palavras com letra inicial maiuscula
- `lower()`: transforma o texto em letras minusculas

Esses metodos ajudam a tratar entradas do usuario, porque pessoas podem digitar com espacos extras ou letras em formatos diferentes.

### `import`

`import` permite usar codigo que esta em outro arquivo.

No projeto, isso ajuda a separar a logica em `saudacoes.py` e usar essa logica a partir de `main.py` ou dos testes.

### `assert`

`assert` e usado em testes para verificar se uma condicao e verdadeira.

Exemplo mental:

```text
eu espero que o resultado seja X
se nao for, o teste deve falhar
```

### Mock e patch

`mock` e `patch` ajudam a simular comportamentos durante testes.

No caso de uma CLI, eles podem ser usados para simular respostas do usuario ao `input()`, sem precisar digitar manualmente toda vez que o teste roda.

## 6. Modelos mentais importantes

### Entrada -> tratamento -> logica -> saida

Esse e um modelo simples para entender programas:

- entrada: o que vem de fora, como o nome digitado pelo usuario
- tratamento: limpeza e padronizacao, como `strip()`, `title()` ou `lower()`
- logica: as regras do programa
- saida: aquilo que o programa mostra ou devolve

### Funcao = maquina pequena

Uma funcao pode ser vista como uma pequena maquina.

Voce entrega algo para ela, ela trabalha internamente e depois entrega um resultado.

### Parametros = entradas da funcao

Parametros sao os dados que voce passa para uma funcao trabalhar.

### `return` = saida da funcao

`return` e o resultado que sai da funcao.

### Interface diferente de logica

Interface e a parte que conversa com o usuario. Neste projeto, isso acontece principalmente com `input()` e `print()`.

Logica e a parte que decide o que fazer com os dados.

Separar interface e logica deixa o codigo mais facil de testar, reaproveitar e modificar.

### Resposta do Codex = hipotese

A resposta do Codex deve ser tratada como uma hipotese.

Ela pode estar correta, mas precisa ser revisada e testada. O Codex ajuda a acelerar o trabalho, mas o builder continua responsavel por validar o resultado.

### Teste no terminal = validacao

Rodar o programa no terminal confirma se ele funciona na pratica.

Rodar os testes confirma se partes importantes continuam funcionando depois das mudancas.

### Commit = ponto seguro

Um commit e um ponto salvo no historico do projeto.

Ele funciona como um marco: "ate aqui, essa versao fazia sentido".

### Push = enviar historico para o GitHub

`push` envia os commits locais para o GitHub.

O commit salva no Git local. O push publica esse historico no repositorio remoto.

## 7. Workflow com Codex

Um bom ciclo de trabalho com Codex e:

1. Pedir uma mudanca pequena.
2. Revisar o diff.
3. Testar manualmente no terminal.
4. Rodar os testes automatizados.
5. So depois salvar no Git.

Esse fluxo evita acumular muitas mudancas sem entender o que aconteceu.

Tambem existe uma regra importante:

Quando for so duvida, peca ao Codex para explicar e diga: "nao altere nenhum arquivo".

Isso deixa claro que voce quer aprendizado ou orientacao, nao edicao no projeto.

## 8. Workflow com Git e GitHub

Git e a ferramenta que controla o historico do projeto na sua maquina.

GitHub e a plataforma online onde voce pode guardar e compartilhar esse historico.

Comandos importantes:

- `git status`: mostra o estado atual do projeto
- `git add`: coloca arquivos na area de preparacao para o commit
- `git commit`: salva um ponto no historico local
- `git push`: envia commits locais para o GitHub
- `git log --oneline`: mostra o historico de commits de forma resumida
- `git restore`: descarta mudancas em arquivos quando voce quer voltar ao ultimo estado salvo

Diferença entre commit e push:

- commit: salva no historico local
- push: envia esse historico para o GitHub

Ciclo padrao:

```bash
git status
git add arquivo
git commit -m "mensagem"
git push
git status
```

Esse ciclo ajuda a trabalhar com calma: olhar o estado, preparar arquivos, salvar, enviar e conferir de novo.

## 9. Erros e aprendizados importantes

### Arquivo nao salvo no VS Code

Se o arquivo foi editado, mas nao salvo, o terminal pode executar uma versao antiga.

Antes de testar, confira se o arquivo esta salvo.

### `main.py` laranja ou modificado

No VS Code, um arquivo marcado como modificado indica que ha alteracoes ainda nao salvas no Git.

Isso nao e necessariamente um problema. E apenas um sinal de que o arquivo mudou.

### Diff

Diff e a comparacao entre o que existia antes e o que mudou agora.

Revisar o diff e uma das melhores formas de aprender, porque mostra exatamente o que foi alterado.

### Arquivo untracked

Um arquivo untracked e um arquivo novo que o Git ainda nao esta acompanhando.

Ele aparece no `git status` ate voce decidir adiciona-lo com `git add` ou ignora-lo.

### `__pycache__` e `.gitignore`

`__pycache__` e uma pasta automatica criada pelo Python.

Ela nao faz parte do codigo que voce escreve. Por isso, normalmente deve ficar no `.gitignore`.

### Aviso "file is newer" no VS Code

Esse aviso pode aparecer quando o arquivo no disco esta mais novo do que a versao aberta no editor.

Isso significa que alguma mudanca aconteceu fora daquela aba do VS Code.

### Cuidado com Overwrite

Overwrite significa sobrescrever.

Se voce sobrescrever sem conferir, pode perder mudancas.

### Usar Compare antes de sobrescrever

Quando houver conflito entre versoes, use Compare antes de sobrescrever.

Comparar permite ver as diferencas e escolher com mais seguranca o que manter.

## 10. Checklist para projetos futuros

- Definir um MVP pequeno.
- Criar a estrutura inicial.
- Rodar manualmente no terminal.
- Criar testes.
- Revisar o diff.
- Fazer commits pequenos.
- Manter o README atualizado.
- Enviar para o GitHub.

## 11. Ponte para o Módulo 2

O proximo modulo sera um organizador de notas local.

O foco sera aprender persistencia de dados usando arquivos. Em vez de o programa apenas receber dados e mostrar uma resposta no terminal, ele tambem vai salvar informacoes para serem usadas depois.

Esse e um passo importante: sair de programas que "esquecem tudo" quando terminam e comecar a criar ferramentas que mantem dados entre execucoes.
