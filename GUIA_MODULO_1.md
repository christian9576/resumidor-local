# Guia do Módulo 1 — Primeiros passos como builder com IA

## 1. Objetivo do módulo

O objetivo deste módulo foi aprender o ciclo básico de desenvolvimento usando Python, Codex, Git, GitHub e testes.

A ideia não era criar um sistema grande. O foco foi entender como um projeto nasce pequeno, ganha organização aos poucos e passa a ter um fluxo mais profissional: escrever código, executar no terminal, testar, revisar mudanças, salvar no Git e enviar para o GitHub.

Este projeto começou como uma saudação simples em Python e evoluiu para uma mini CLI organizada. Isso mostra um modelo importante: projetos reais não precisam nascer completos. Eles podem evoluir por pequenas melhorias.

## 2. O que foi construído

Foi criada uma mini CLI de saudação. CLI significa "interface de linha de comando", ou seja, um programa usado pelo terminal.

O programa permite:

- pedir o nome do usuário
- escolher entre saudação informal, formal e motivacional
- usar a opção `sair`
- repetir o fluxo para criar várias saudações
- validar entradas digitadas pelo usuário
- rodar testes automatizados simples

Na prática, o usuário executa o programa, responde perguntas no terminal e recebe uma mensagem de saudação como resultado.

## 3. Estrutura final do projeto

O projeto ficou separado em arquivos com responsabilidades diferentes:

- `main.py`: ponto de entrada da CLI. É o arquivo que conversa com o usuário usando `input()` e `print()`. Também organiza o fluxo do programa.
- `saudacoes.py`: arquivo com a lógica principal das saudações. Ele concentra regras, tratamento de texto e validações.
- `test_main.py`: arquivo com testes automatizados simples para conferir se o programa se comporta como esperado.
- `README.md`: documentação principal do projeto. Explica o que o programa faz, como rodar e como testar.
- `.gitignore`: arquivo que diz ao Git quais arquivos ou pastas devem ser ignorados, como arquivos automáticos do Python.

Essa separação ajuda a manter o projeto mais fácil de entender. A interface fica em um lugar, a lógica fica em outro e os testes ficam separados.

## 4. Linha do tempo do projeto

A evolução aproximada do projeto foi:

- `print()` simples
- `input()` para pedir o nome
- validação de nome vazio
- uso de `strip()`, `title()` e `lower()`
- criação de funções
- uso de `main()`
- padrão `if __name__ == "__main__"`
- testes com `assert`
- criação de `.gitignore`
- tipos de saudação
- opção `sair`
- múltiplas saudações na mesma execução
- separação da lógica em `saudacoes.py`

Essa linha do tempo é útil porque mostra que o projeto não ficou melhor de uma vez. Ele melhorou por etapas pequenas, cada uma adicionando um aprendizado.

## 5. Conceitos de terminal

O terminal é o lugar onde chamamos programas por comandos.

Quando digitamos:

```bash
python main.py
```

estamos pedindo ao Python para executar o arquivo `main.py`.

Quando digitamos:

```bash
python test_main.py
```

estamos pedindo ao Python para executar os testes que estão em `test_main.py`.

Existe uma diferença importante entre abrir um arquivo e executar um arquivo:

- abrir um arquivo: ver ou editar o conteúdo no VS Code
- executar um arquivo: pedir para o computador rodar aquele código

No VS Code, você pode estar olhando para `main.py`, mas isso não significa que o programa está rodando. Para rodar, você precisa executar o comando no terminal.

## 6. Conceitos de Python aprendidos

### Variáveis

Variáveis guardam valores para serem usados depois.

Exemplo mental: uma variável é uma caixinha com nome. Dentro dela pode estar um texto, um número ou outro valor.

### Constantes

Constantes também guardam valores, mas representam algo que não deve mudar durante o programa.

Em Python, por convenção, nomes de constantes costumam ficar em letras maiúsculas.

### `input()`

`input()` serve para receber texto digitado pelo usuário no terminal.

### `print()`

`print()` serve para mostrar informações no terminal.

### Funções

Funções são blocos de código com nome. Elas ajudam a organizar o programa e evitar repetição.

Uma função pode receber dados, processar esses dados e devolver um resultado.

### Parâmetros

Parâmetros são as entradas de uma função.

Se a função fosse uma pequena máquina, os parâmetros seriam aquilo que colocamos dentro dela para trabalhar.

### `return`

`return` é a saída de uma função. Ele devolve um valor para quem chamou a função.

### `if` / `else`

`if` e `else` permitem tomar decisões.

Exemplo mental:

```text
se isso acontecer, faça uma coisa
caso contrário, faça outra
```

### `while`

`while` cria repetição enquanto uma condição for verdadeira.

No projeto, esse conceito aparece na ideia de repetir o fluxo para criar novas saudações.

### Listas

Listas guardam vários valores em uma mesma estrutura.

Elas são úteis quando queremos representar um conjunto de opções ou dados relacionados.

### Métodos de texto

Alguns métodos importantes usados ou discutidos:

- `strip()`: remove espaços no começo e no fim de um texto
- `title()`: coloca as palavras com letra inicial maiúscula
- `lower()`: transforma o texto em letras minúsculas

Esses métodos ajudam a tratar entradas do usuário, porque pessoas podem digitar com espaços extras ou letras em formatos diferentes.

### `import`

`import` permite usar código que está em outro arquivo.

No projeto, isso ajuda a separar a lógica em `saudacoes.py` e usar essa lógica a partir de `main.py` ou dos testes.

### `assert`

`assert` é usado em testes para verificar se uma condição é verdadeira.

Exemplo mental:

```text
eu espero que o resultado seja X
se não for, o teste deve falhar
```

### Mock e patch

`mock` e `patch` ajudam a simular comportamentos durante testes.

No caso de uma CLI, eles podem ser usados para simular respostas do usuário ao `input()`, sem precisar digitar manualmente toda vez que o teste roda.

## 7. Modelos mentais importantes

### Entrada -> tratamento -> lógica -> saída

Esse é um modelo simples para entender programas:

- entrada: o que vem de fora, como o nome digitado pelo usuário
- tratamento: limpeza e padronização, como `strip()`, `title()` ou `lower()`
- lógica: as regras do programa
- saída: aquilo que o programa mostra ou devolve

### Função = máquina pequena

Uma função pode ser vista como uma pequena máquina.

Você entrega algo para ela, ela trabalha internamente e depois entrega um resultado.

### Parâmetros = entradas da função

Parâmetros são os dados que você passa para uma função trabalhar.

### `return` = saída da função

`return` é o resultado que sai da função.

### Interface diferente de lógica

Interface é a parte que conversa com o usuário. Neste projeto, isso acontece principalmente com `input()` e `print()`.

Lógica é a parte que decide o que fazer com os dados.

Separar interface e lógica deixa o código mais fácil de testar, reaproveitar e modificar.

### Resposta do Codex = hipótese

A resposta do Codex deve ser tratada como uma hipótese.

Ela pode estar correta, mas precisa ser revisada e testada. O Codex ajuda a acelerar o trabalho, mas o builder continua responsável por validar o resultado.

### Teste no terminal = validação

Rodar o programa no terminal confirma se ele funciona na prática.

Rodar os testes confirma se partes importantes continuam funcionando depois das mudanças.

### Commit = ponto seguro

Um commit é um ponto salvo no histórico do projeto.

Ele funciona como um marco: "até aqui, essa versão fazia sentido".

### Push = enviar histórico para o GitHub

`push` envia os commits locais para o GitHub.

O commit salva no Git local. O push publica esse histórico no repositório remoto.

## 8. Workflow com Codex

Um bom ciclo de trabalho com Codex é:

1. Pedir uma mudança pequena.
2. Revisar o diff.
3. Testar manualmente no terminal.
4. Rodar os testes automatizados.
5. Só depois salvar no Git.

Esse fluxo evita acumular muitas mudanças sem entender o que aconteceu.

Também existe uma regra importante:

Quando for só dúvida, peça ao Codex para explicar e diga: "não altere nenhum arquivo".

Isso deixa claro que você quer aprendizado ou orientação, não edição no projeto.

## 9. Workflow com Git e GitHub

Git é a ferramenta que controla o histórico do projeto na sua máquina.

GitHub é a plataforma online onde você pode guardar e compartilhar esse histórico.

Comandos importantes:

- `git status`: mostra o estado atual do projeto
- `git add`: coloca arquivos na área de preparação para o commit
- `git commit`: salva um ponto no histórico local
- `git push`: envia commits locais para o GitHub
- `git log --oneline`: mostra o histórico de commits de forma resumida
- `git restore`: descarta mudanças em arquivos quando você quer voltar ao último estado salvo

Diferença entre commit e push:

- commit: salva no histórico local
- push: envia esse histórico para o GitHub

Ciclo padrão:

```bash
git status
git add arquivo
git commit -m "mensagem"
git push
git status
```

Esse ciclo ajuda a trabalhar com calma: olhar o estado, preparar arquivos, salvar, enviar e conferir de novo.

## 10. Erros e aprendizados importantes

### Arquivo não salvo no VS Code

Se o arquivo foi editado, mas não salvo, o terminal pode executar uma versão antiga.

Antes de testar, confira se o arquivo está salvo.

### `main.py` laranja ou modificado

No VS Code, um arquivo marcado como modificado indica que há alterações ainda não salvas no Git.

Isso não é necessariamente um problema. É apenas um sinal de que o arquivo mudou.

### Diff

Diff é a comparação entre o que existia antes e o que mudou agora.

Revisar o diff é uma das melhores formas de aprender, porque mostra exatamente o que foi alterado.

### Arquivo untracked

Um arquivo untracked é um arquivo novo que o Git ainda não está acompanhando.

Ele aparece no `git status` até você decidir adicioná-lo com `git add` ou ignorá-lo.

### `__pycache__` e `.gitignore`

`__pycache__` é uma pasta automática criada pelo Python.

Ela não faz parte do código que você escreve. Por isso, normalmente deve ficar no `.gitignore`.

### Aviso "file is newer" no VS Code

Esse aviso pode aparecer quando o arquivo no disco está mais novo do que a versão aberta no editor.

Isso significa que alguma mudança aconteceu fora daquela aba do VS Code.

### Cuidado com Overwrite

Overwrite significa sobrescrever.

Se você sobrescrever sem conferir, pode perder mudanças.

### Usar Compare antes de sobrescrever

Quando houver conflito entre versões, use Compare antes de sobrescrever.

Comparar permite ver as diferenças e escolher com mais segurança o que manter.

## 11. O que eu já consigo fazer depois deste módulo

Depois deste módulo, eu já consigo:

- criar um projeto Python simples
- rodar arquivos pelo terminal
- usar Codex com escopo pequeno e bem definido
- revisar diff antes de aceitar uma mudança
- testar manualmente o programa no terminal
- criar testes simples com `assert`
- usar `git status`, `git add`, `git commit` e `git push`
- publicar um projeto no GitHub
- manter `README.md` e guias de estudo atualizados

Essa lista serve como um lembrete prático: o Módulo 1 não foi só sobre Python. Ele também treinou o ciclo de trabalho de um projeto pequeno.

## 12. Checklist para projetos futuros

- Definir um MVP pequeno.
- Criar a estrutura inicial do projeto.
- Rodar o programa manualmente no terminal.
- Fazer uma mudança por vez.
- Revisar o diff antes de continuar.
- Criar testes simples para as regras principais.
- Rodar os testes depois de mudanças importantes.
- Fazer commits pequenos e com mensagens claras.
- Manter o `README.md` atualizado.
- Manter guias de estudo atualizados quando o projeto evoluir.
- Enviar commits para o GitHub.
- Conferir o `git status` no final.

## 13. Ponte para o Módulo 2

O próximo módulo será um organizador de notas local.

O foco será aprender persistência de dados usando arquivos. Em vez de o programa apenas receber dados e mostrar uma resposta no terminal, ele também vai salvar informações para serem usadas depois.

Esse é um passo importante: sair de programas que "esquecem tudo" quando terminam e começar a criar ferramentas que mantêm dados entre execuções.
