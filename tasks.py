import json, os
from pathlib import Path

TASKS_FILE = Path("tasks.json")

def show_menu():
    print("=== Menu ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Completar tarefa")
    print("4. Apagar tarefa")
    print("5. Editar tarefa")
    print("6. Filtrar tarefas")
    print("7. Sair")

def load_tasks():
    if not os.path.exists("tasks.json") or os.path.getsize("tasks.json") == 0:
        return []
    
    with open("tasks.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_tasks(task):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(task, file, ensure_ascii=False, indent=2)

def add_tasks(title, tasks):
    tasks_dic = {
        "titulo": title,
        "concluída": False
    }

    tasks.append(tasks_dic)
    print("Tarefa adicionada!")
    show_menu()

def complete_task():
    tasks = load_tasks()

    if not tasks:
        print("Nenhuma tarefa encontrada")
        return
    
    list_tasks(tasks)

    try:
        index = int(input("Digite o número da tarefa que deseja concluir: "))
        if 0 <= index < len(tasks):
            tasks[index - 1]["concluída"] = True
            save_tasks(tasks)
            print("Tarefa concluída com sucesso!")
            show_menu()
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")

def delete_task():
    tasks = load_tasks()

    if not tasks:
        print("Nenhuma tarefa encontrada")
        return
    
    list_tasks(tasks)
    
    try:
        user_input = int(input("Digite o número da tarefa que deseja apagar: "))
        index = user_input - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("Tarefa deletada com sucesso!")
            show_menu()
        else:
            print("Número inválido, tente novamente")
    except ValueError:
        print("Por favor, digite um número válido")

def list_tasks(tasks):
    print("=== Tarefas ===")
    for count, task in enumerate(tasks, 1):
        if task["concluída"]:
            print(f"{count}. {task['titulo']} \u2705")
        else:
            print(f"{count}. {task['titulo']} \u274C")

def edit_task():
    tasks = load_tasks()

    if not tasks:
        print("Nenhuma tarefa encontrada")
        return
    
    list_tasks(tasks)

    try:
        user_input = int(input("Digite o número da tarefa que deseja editar: "))
        index = user_input - 1
        new_title = input("Digite o novo título da tarefa: ")

        if 0 <= index < len(tasks):
            tasks[index]["titulo"] = new_title
            tasks[index]["concluída"] = False
            print("Tarefa editada com sucesso! Status de 'concluída' foi reiniciado")
            save_tasks(tasks)
            show_menu()
        else:
            print("Número inválido, tente novamente")
    except ValueError:
        print("Por favor, digite um número válido")

def filter_tasks():
    tasks = load_tasks()

    if not tasks:
        print("Nenhuma tarefa encontrada")
        return
    