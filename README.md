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

    
2. Crie um arquivo chamado tasks.json na raiz do projeto:
    ```bash
        touch tasks.json
    ```
3. Adicione uma lista vazia ao arquivo, para evitar erros ao iniciar o programa:

    ```bash
        []
    ```

4. Execute o script principal:
    ```bash
        python main.py
    ```

Estrutura do projeto

    main.py: script principal com todas as funcionalidades do programa

    tasks.json: arquivo onde as tarefas são armazenadas (não incluído no repositório)