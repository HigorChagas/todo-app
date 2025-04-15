# To-Do List em Python

Este é um projeto de lista de tarefas feito em Python, com o objetivo de praticar lógica de programação, manipulação de arquivos e criação de menus interativos no terminal.

## Funcionalidades

- Adicionar nova tarefa
- Listar tarefas com status (concluída ou pendente)
- Editar uma tarefa existente
- Marcar tarefa como concluída
- Apagar uma tarefa
- Filtrar tarefas por status (pendentes ou concluídas)
- Salvamento automático das tarefas em arquivo JSON

## Tecnologias usadas

- Python 3.x
- Módulos `json`, `os` e `pathlib`

## Como rodar o projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio

    Crie um arquivo chamado tasks.json na raiz do projeto:

touch tasks.json

Adicione uma lista vazia ao arquivo, para evitar erros ao iniciar o programa:

[]

Execute o script principal:

    python main.py

Estrutura do projeto

    main.py: script principal com todas as funcionalidades do programa

    tasks.json: arquivo onde as tarefas são armazenadas (não incluído no repositório)

Objetivo do projeto

Este projeto está sendo desenvolvido com foco em aprender programação na prática, implementando funcionalidades aos poucos através de missões.
Próximos passos

    Contar e exibir número de tarefas pendentes e concluídas

    Marcar tarefa como não concluída

    Melhorar a interface do menu

    Explorar possibilidade de interface gráfica no futuro